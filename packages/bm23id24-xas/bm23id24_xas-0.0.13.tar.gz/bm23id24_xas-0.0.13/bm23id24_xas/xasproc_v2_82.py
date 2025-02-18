# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:37:25 2023

@author: LOMACHEN
"""


# Modules

import h5py
import os 
import numpy as np
from datetime import datetime
import copy

from itertools import cycle

from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter as savgol

import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import FormatStrFormatter

import tkinter as tk
from tkinter import filedialog

import larch
from larch import Group
from larch.xafs import *

import importlib.util

def load_params(file_path):
    spec = importlib.util.spec_from_file_location("params", file_path)
    params = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(params)
    
    # Load all variables from the module directly into the global scope
    globals().update({key: value for key, value in params.__dict__.items() if not key.startswith("__")})


def etok(e):
    k = np.sqrt((e/3.81))
    return k

def ktoe(k):
    e = k**2*3.81
    return e

def load_file(path):
    '''
    Loads an HDF5 (.h5) file and returns relevant information including the directory,
    filename, file extension, and the dataset from the file.

    Parameters:
    ----------
    path : str or None
        The full file path to the HDF5 (.h5) file. If None, a file dialog will open 
        for the user to select a file manually.

    Returns:
    -------
    directory : str
        The directory where the selected file is located.
        
    filename : str
        The name of the file without its extension.
        
    file_extension : str
        The file extension (e.g., `.h5`).
        
    dataset : h5py.File object
        The dataset opened from the HDF5 file in read mode.

    Notes:
    -----
    - If `path` is not provided (i.e., None), a file dialog will prompt the user to select a file.
    - This function uses the `h5py` library to open the file and `tkinter` for the file dialog.
    - The function sets the directory to the folder where the selected file is located.
    
    '''
    
    ### Choosing the file
    if path == None:
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(title="Select a file", filetypes=(("h5 files", "*.h5"), ("All files", "*.*")))       # full path containing filename
            
    ### Saving directory 
    directory=str(os.path.dirname(path))  # that will save to the directory of the .h5 file
    print(f'Directory set to: {directory}')        
    
    ### Setting filename   
    filename, file_extension = os.path.splitext(os.path.basename(path))
    print(f'Working with file: {filename}{file_extension}')         
        
    ### Opening the file 
    dataset = h5py.File(path,mode ='r')
    
    return directory, filename, file_extension, dataset
    


def create_raw(dataset, directory, filename, n_first, n_last, skiplist, merge):
    
    if skiplist is None:
        skiplist = []
    
    description = filename # for now CHANGE THAT!

            
    if n_last == None:
        n_last = len(dataset)    
    
    data={}    #initialize the dictionary

    first_scan=True    # To discriminate between the first and the consequent scans for alignment

    for scan_number in range (n_first, n_last + 1):
        
        if scan_number in skiplist:
            continue
        
        scan_label = '/'+str(scan_number)+'.1'
        scan_data=dataset[scan_label]
              
        
        if "scans.exafs_" in str(scan_data['title'][()]) or "contscan.motor" in str(scan_data['title'][()]) or "trigscan" in str(scan_data['title'][()]):
            
            try:
                repeats = scan_data['instrument']['fscan_parameters']['nscans'][()]
                npoints_theor = scan_data['instrument']['fscan_parameters']['npoints'][()] + 1 # value defined in the beginning of the scan
            except:
                repeats = 1
                npoints_theor = 0  # This is just to avoid getting the error. The value is not used if repeats = 1 
            
            if repeats != 1:
                print(f'Scan {scan_number} contains {repeats} repeats\n')

            for rep in range (1,repeats+1):
            
                scan_address = f'{scan_number}.{rep}'
                
                print(f'Extracting scan {scan_address}')
                
                try:
                    energy = scan_data['measurement'][energy_counter][()]           
                    if np.max(energy)<100:
                        energy=energy*1000                                  
                except:
                    print(f'Scan {scan_number} cannot be read, skipping it')
                    continue
                
                if max(energy) < e0 + norm2:
                    print(f'Scan {scan_address}: WARNING, data range smaller than normalization range')
                if min(energy) > e0 + pre1:
                    print(f'Scan {scan_address}: WARNING, data range smaller than pre-edge range')

                npoints_total = len(energy)
                
                
                try:
                    if repeats != 1:                        
                        energy = energy[int((rep-1)*npoints_theor + 2) : int(rep*npoints_theor) - 2] #skipping the first and last two points of every scan
                    else:                        
                        energy = energy[2:-2]
                
                    if energy[-1] < energy[0]: # Invert for "back" scans in back'n'forth mode                        
                        energy = energy[::-1]
                        need_to_invert = True
                        print('It is a "back" scan: inverting the energy scale')
                    else:
                        need_to_invert = False
                    
                except:
                    print(f'Scan {scan_address} does not exist, skipping it')
                    continue
                
                
                
                # Load other counters
                def load_counter(scan_data, counter, repeats, rep, npoints_theor,need_to_invert):
                    '''
                    Extracts and processes data from a specified counter within a scan dataset. It trims the data 
                    based on repeat count, optionally inverts the order, and handles any NaN or infinity values 
                    by replacing them with zeros.

                    '''

                    counter_data = scan_data['measurement'][counter][()]                              
                    if repeats != 1:                    
                        counter_data = counter_data[int((rep-1)*npoints_theor + 2) : int(rep*npoints_theor) - 2]
                    else:
                        counter_data = counter_data[2:-2]                
                    if need_to_invert:
                        counter_data = counter_data[::-1]                    
                    counter_data[np.isnan(counter_data)] = 0.0  # Replaces NaNs by 0
                    counter_data[np.isinf(counter_data)] = 0.0  # Replaces infs by 0

                    return counter_data                
                
                mu = load_counter(scan_data, mu_counter, repeats, rep, npoints_theor, need_to_invert)                
                ref = load_counter(scan_data, ref_counter, repeats, rep, npoints_theor, need_to_invert)                
                
                try:
                    timer_trig = load_counter(scan_data, 'timer_trig', repeats, rep, npoints_theor, need_to_invert)                
                except:
                    timer_trig = 'No timer_trig available' # This will happen with the old data
             
                # Calculate gradients
                
                mu_prime = np.gradient(mu, energy)
                ref_prime = np.gradient(ref, energy)
                ref_prime_smoothed = savgol(ref_prime,7,2)
                                                
                
                try:
                    comment = scan_data['instrument']['comment'][()]
                except:
                    comment = ''
                                
                start_time = scan_data['start_time'][()]
                end_time = scan_data['end_time'][()]
                
                if isinstance(start_time, bytes):                        # This is to be compatible with different versions of (?) h5py 
                    start_time = start_time.decode('ascii', 'replace')
                    end_time = end_time.decode('ascii', 'replace')
                start_time = datetime.strptime(start_time,'%Y-%m-%dT%H:%M:%S.%f%z')
                end_time = datetime.strptime(end_time,'%Y-%m-%dT%H:%M:%S.%f%z')
                
                if repeats != 1:
                    start_time = start_time + (rep-1)* (end_time-start_time)/repeats * npoints_theor * repeats/npoints_total    # Only approximate estimation for the scans that are not finished
                        
                if first_scan:
                    zero_time = start_time
                    number = 0
                    first_scan = False
                    
                    
                rel_time = (start_time - zero_time).total_seconds()
                number += 1 # Order number of the scan
                print(f'Number of the scan in the series: {number}')
    
                try:
                    temperature = scan_data['instrument']['EurothermNanodac']['measure'][()]
                except:
                    temperature = 0
    
                # Fill the dictionary
                
                data[scan_address] = {}
                data[scan_address]['filename'] = filename
                data[scan_address]['description'] = description                
                data[scan_address]['directory'] = directory    
                
                data[scan_address]['energy'] = energy
                data[scan_address]['mu'] = mu
                data[scan_address]['ref'] = ref
                data[scan_address]['timer_trig'] = timer_trig
                
                data[scan_address]['mu_prime'] = mu_prime
                data[scan_address]['ref_prime'] = ref_prime
                data[scan_address]['ref_prime_smoothed'] = ref_prime_smoothed
                
                data[scan_address]['comment'] = comment
                data[scan_address]['start_time'] = start_time
                data[scan_address]['rel_time'] = rel_time
                data[scan_address]['number'] = number
                
                data[scan_address]['temperature'] = temperature
    
    print('')
    return data

def calibrate_spectra(calibrate, data, radius_calib, acceptable_error, Eref):
    result = copy.deepcopy(data)
    
    if not calibrate:
        print(f'Skipping calibration\n')
        return result
    
    print(f'Calibrating the maximum of the smoothed derivative of reference scans to Eref = {Eref} eV')
    calibration_shift = 0
    for scan in result:
        energy = result[scan]['energy']
        ref_prime_smoothed = result[scan]['ref_prime_smoothed']
        
        ref_prime_max_energy = energy[np.argmax(ref_prime_smoothed)]                    
        
        grid = np.linspace(ref_prime_max_energy - radius_calib, ref_prime_max_energy + radius_calib, 1000) 
        ref_prime_smoothed_fine = interp1d(energy, ref_prime_smoothed, kind= 'quadratic')(grid)                                            
        ref_prime_max_energy = grid[np.argmax(ref_prime_smoothed_fine)]     
        calibration_error = ref_prime_max_energy - Eref
        
        
        if abs(calibration_error) < acceptable_error:
            calibration_shift = - calibration_error
            print(f'Scan {scan}: reference E0 found at {ref_prime_max_energy:.3f} eV. The scan shifted by {calibration_shift:.3f} eV to match Eref = {Eref}')
        else:
            print(f'Scan {scan}: reference E0 found at {ref_prime_max_energy:.3f} eV, which is more than {acceptable_error: .1f} eV away from reference value of Eref = {Eref}. Apply calibration shift of {calibration_shift:.3f} eV from the previous scan.')                                         
        energy = energy + calibration_shift                                                            
        
        result[scan]['energy'] = energy
        result[scan]['calibration_shift'] = calibration_shift
        
        if 'total shift' in result[scan]:
            result[scan]['total_shift'] += calibration_shift
        else:
            result[scan]['total_shift'] = calibration_shift
    
    print('')
    return result

def align_spectra(align, data, radius_align, Ealign):         
    result = copy.deepcopy(data)
        
    if align == False or align == 'False' or align == 'false':
        print ('Skipping alignment\n')
        return result
    
    print('Aligning the spectra using the smoothed derivatives of reference scans')                               
    first_scan = list(result.keys())[0]
    
    if align == 'load':
        std_energy = np.loadtxt("align_ref_prime.txt")[:,0]
        std_ref_prime = np.loadtxt("align_ref_prime.txt")[:,1]        
    elif align == 'save' or align == 'Save' or align == True or align == 'True' or align == 'true':
        std_energy = result[first_scan]['energy']
        std_ref_prime = result[first_scan]['ref_prime_smoothed']
        
        if align == 'save' or align == 'Save':
            saved = np.column_stack((std_energy, std_ref_prime))
            np.savetxt("align_ref_prime.txt", saved)
            print(f'Smoothed ref derivative of scan {first_scan} was saved as a reference in the file align_ref_prime.txt.')                 
    else:
        print('Wrong value of the align keyword. No alignment is done\n')                                   
        return result
    
    for scan in result:
        energy = result[scan]['energy']
        ref_prime_smoothed = result[scan]['ref_prime_smoothed']
        
        grid = np.linspace(Ealign - radius_align, Ealign + radius_align, 1000) 
        standard = interp1d(std_energy, std_ref_prime, kind= 'quadratic') 
        spectrum = interp1d(energy, ref_prime_smoothed, kind= 'quadratic') 
        
        def alignment_function(x, E):
            return spectrum(x - E)                
        
        best_vals, covar = curve_fit(alignment_function, grid, standard(grid), p0=0)                
        alignment_shift = best_vals[0]                                
        
        if align == 'load':
            print(f'Scan {scan} shifted by {alignment_shift :.3f} eV to match the loaded reference.')        
        else:                
            print(f'Scan {scan} shifted by {alignment_shift :.3f} eV to match the scan {first_scan}.')        
            
        energy = energy + alignment_shift
        
        result[scan]['energy'] = energy
        result[scan]['alignment_shift'] = alignment_shift
        
        if 'total_shift' in result[scan]:
            result[scan]['total_shift'] += alignment_shift
        else:
            result[scan]['total_shift'] = alignment_shift
    
    print('')
    return result

def interpolate_spectra(interpolate, data):                           
    result = copy.deepcopy(data)
    
    first_scan = list(result.keys())[0]
    
    if interpolate == False or interpolate == 'False' or interpolate == 'false':
        print('Skipping interpolation\n')
        return result
        
    print('Interpolating the scans to a unique energy grid')
    
    if interpolate == 'load' or interpolate == 'Load':            
        try:
            std_energy = np.loadtxt("align_ref_prime.txt")[:,0]
            interp_grid = np.linspace(std_energy[0], std_energy[-1], len(std_energy))                 
            print('Using the energy grid from align_ref_prime.txt file used also for alignment')
        except FileNotFoundError:
            try:
                interp_grid = np.loadtxt('interp_energy_grid.txt')                  
                print('Using the energy grid from interp_energy_grid.txt file')    
            except FileNotFoundError:
                raise FileNotFoundError ('Neither align_ref_prime.txt nor interp_energy_grid.txt were found, run with align  = "save" or interpolate = "save" first')                                
    
    elif interpolate == 'save' or interpolate == 'Save' or interpolate == True or interpolate == 'True' or interpolate == 'true':                             
        print(f'Interpolating all scans to the energy grid from the scan {first_scan}.')    
        energy = result[first_scan]['energy']
        interp_grid = np.linspace(energy[0], energy[-1], len(energy))     
        
        if interpolate == 'save' or interpolate == 'Save':
            np.savetxt("interp_energy_grid.txt", interp_grid)
    else:
        print('Wrong value of the interpolate keyword. No interpolation is done\n')                                   
        return result
    
    for scan in result:
        energy = result[scan]['energy']
        mu = result[scan]['mu']
        mu_prime = result[scan]['mu_prime']
        ref = result[scan]['ref']
        ref_prime = result[scan]['ref_prime']
        timer_trig = result[scan]['timer_trig']
        ref_prime_smoothed = result[scan]['ref_prime_smoothed']                        
        
        result[scan]['mu'] = interp1d(energy, mu, bounds_error = False, fill_value = 'extrapolate')(interp_grid)
        result[scan]['mu_prime'] = interp1d(energy, mu_prime, bounds_error = False, fill_value = 'extrapolate')(interp_grid)
        result[scan]['ref'] = interp1d(energy, ref, bounds_error = False, fill_value = 'extrapolate')(interp_grid)
        result[scan]['ref_prime'] = interp1d(energy, ref_prime, bounds_error = False, fill_value = 'extrapolate')(interp_grid)
        try:
            result[scan]['timer_trig'] = interp1d(energy, timer_trig, bounds_error = False, fill_value = 'extrapolate')(interp_grid)
        except:
            pass
        result[scan]['ref_prime_smoothed'] = interp1d(energy, ref_prime_smoothed, bounds_error = False, fill_value = 'extrapolate')(interp_grid)    
        result[scan]['energy'] = interp_grid
    
    print('')                    
    return result

def merge_spectra(data, merge):
    result = copy.deepcopy(data)
    
    if merge != 1:
        print(f'Merging every {merge} spectra')
    else:
        print(f'No merging is performed')
        
    scan_list = list(result.keys())    
    
    energy = result[scan_list[0]]['energy']
    
    
    for scan in range (len(scan_list)):       
        if merge == 1:
            result[scan_list[scan]]['merge'] = merge
            
        else:
            energy_temp = result[scan_list[scan]]['energy']           
            
            if not np.array_equal(energy, energy_temp):        
                raise Exception("Energy grid of the scans to be averaged is not the same. You must interpolate the spectra")            
            
            if (scan + 1) % merge == 1: # first scan of the merged group
                
                start_time_temp = result[scan_list[scan]]['start_time']
                rel_time_temp = result[scan_list[scan]]['rel_time']            
                mu_temp = result[scan_list[scan]]['mu']                        
                ref_temp = result[scan_list[scan]]['ref']
                timer_trig_temp = result[scan_list[scan]]['timer_trig']                
                temperature_temp = result[scan_list[scan]]['temperature']                
                del result[scan_list[scan]]
                                       
            
            elif (scan + 1) % merge != 0: # other scans of the merged group
                mu_temp += result[scan_list[scan]]['mu']
                ref_temp += result[scan_list[scan]]['ref']
                timer_trig_temp += result[scan_list[scan]]['timer_trig']
                temperature_temp += result[scan_list[scan]]['temperature']                
                del result[scan_list[scan]]
                
            
            else: # Time to merge                
                mu_temp += result[scan_list[scan]]['mu']
                mu = mu_temp / merge
    
                ref_temp += result[scan_list[scan]]['ref']
                ref = ref_temp / merge                
                
                timer_trig_temp += result[scan_list[scan]]['timer_trig']
                
                try:
                    timer_trig = timer_trig_temp / merge                
                except:
                    timer_trig = 'No timer_trig'
                
                temperature_temp += result[scan_list[scan]]['temperature']
                temperature = temperature_temp / merge                    
                    
                mu_prime = np.gradient(mu, energy)           
                ref_prime = np.gradient(ref, energy)                
                
                result[scan_list[scan]]['start_time'] = start_time_temp
                result[scan_list[scan]]['rel_time'] = rel_time_temp
                result[scan_list[scan]]['mu'] = mu
                result[scan_list[scan]]['ref'] = ref
                result[scan_list[scan]]['timer_trig'] = timer_trig
                result[scan_list[scan]]['temperature'] = temperature
                result[scan_list[scan]]['mu_prime'] = mu_prime
                result[scan_list[scan]]['ref_prime'] = ref_prime
                result[scan_list[scan]]['merge'] = merge
                
    print('')
    return result

def larch_spectra(data, exafs, e0, step, pre1, pre2, norm1, norm2, nnorm, nvict, make_flat, 
                  rbkg, nknots, splinekmin, splinekmax, splinekweight, kstep, clamp_lo, clamp_hi,
                  ftkmin, ftkmax, ftkweight, ftdk):
    
    print('Doing processing with Larch')
    
    result = copy.deepcopy(data)
    
    for scan in result:    
        print (f'Processing scan {scan}')
        energy = result[scan]['energy']
        mu = result[scan]['mu']
        
        larch_group = Group()
        pre_edge(energy, mu, group = larch_group, e0=e0, step=step, pre1=pre1, pre2=pre2, norm1=norm1, norm2=norm2, nnorm=nnorm, nvict=nvict, make_flat=make_flat)
        
        flat = larch_group.flat
        edge_step = larch_group.edge_step
        flat_prime = np.gradient(flat, energy)
        
        xaq = larch_group.pre_edge[np.argmin(abs(energy-(e0+(pre1+pre2)/2)))] # To check. Also, it may be different with new Larch
        
        result[scan]['flat'] = flat 
        result[scan]['edge_step'] = edge_step
        result[scan]['flat_prime'] = flat_prime
        result[scan]['xaq'] = xaq
            
        if exafs:                
            autobk(energy, mu, larch_group, rbkg=rbkg, 
                            e0=e0, nknots=nknots, kmin=splinekmin, 
                            kmax=splinekmax, kweight=splinekweight, 
                            clamp_lo=clamp_lo, clamp_hi=clamp_hi)
            
            k = larch_group.k
            
            chik_default = larch_group.chi
            chik_default_weighted = larch_group.chi*k**ftkweight # Default chik in Larch is too noisy if the data are oversampled. Better use the different rebinning scheme below 
            
            # Do manual rebinning in k starting from chie. This yields lower noise compared to default scheme
            k_raw = etok(energy - e0) 
            chik_raw = larch_group.chie
            
            chik_raw = chik_raw[~np.isnan(k_raw)] # TODO: maybe safer to use condition energy>e0 instead
            k_raw = k_raw[~np.isnan(k_raw)]       # TODO: maybe safer to use condition energy>e0 instead
            
            chik_raw = np.insert(chik_raw,0,0)
            k_raw = np.insert(k_raw,0,0)
            
            
            chik_raw_rebinned = []            
            for k_val in k:                
                indices = (k_raw >= k_val - kstep/2) & (k_raw < k_val + kstep/2)
                if len(chik_raw[indices]) > 2:
                    chik_new = np.mean(chik_raw[indices])
                    chik_raw_rebinned.append(chik_new)
                else:
                    chik_new = interp1d(k_raw,chik_raw)(k_val)
                    chik_raw_rebinned.append(chik_new)            
            chik_raw_rebinned = np.array(chik_raw_rebinned)
            chik_raw_rebinned_weighted = chik_raw_rebinned*k**ftkweight
            

            
            xftf(larch_group.k, chik_raw_rebinned, larch_group, kmin = ftkmin, kmax = ftkmax, 
                             kweight = ftkweight, dk1 = ftdk, dk2 = ftdk, window = window)
            r = larch_group.r
            chir_mag = larch_group.chir_mag
            chir_im = larch_group.chir_im
            
            
            
            result[scan]['k'] = k
            result[scan]['chik_default'] = chik_default_weighted
            result[scan]['chik'] = chik_raw_rebinned_weighted

            result[scan]['r'] = r
            result[scan]['chir_mag'] = chir_mag
            result[scan]['chir_im'] = chir_im
                        

    print('')        
    return result

def calculate_edge(data, e0, radius_edge, tolerance):
    print('Calculating edge positions')
    
    result = copy.deepcopy(data)
    
    for scan in result:
        
        print(f'Calculate edge position for scan {scan}')
        energy = result[scan]['energy']
        flat_prime = result[scan]['flat_prime'] 
        
        flat_prime_max_index = np.argmax(flat_prime)
        flat_prime_max_energy = energy[flat_prime_max_index]
        
        
        if np.isclose(flat_prime_max_energy, e0, atol = tolerance):
            edge_estimate = flat_prime_max_energy
            edge_estimate_index = flat_prime_max_index
        else:
            edge_estimate = e0
            edge_estimate_index = np.argmin(abs(energy-e0))               
    
        flat_prime_smoothed = savgol(flat_prime,7,2)                
        grid_edge = np.linspace(edge_estimate - radius_edge, edge_estimate + radius_edge, 1000) 
        flat_prime_smoothed_fine = interp1d(energy, flat_prime_smoothed, kind= 'quadratic')(grid_edge)
                                                
        flat_prime_max_energy = grid_edge[np.argmax(flat_prime_smoothed_fine)]
        
        edge_energy = flat_prime_max_energy
        
        
        result[scan]['edge_energy'] = edge_energy
        result[scan]['flat_prime_smoothed'] = flat_prime_smoothed
    
    print('')
    
    return result

def calculate_noise(data, e0, norm1, norm2, width_savgol):
    print('Calculating noise')
    result = copy.deepcopy(data)
    
    for scan in result:
        print(f'Calculating noise for scan {scan}')
        energy = result[scan]['energy']
        mu = result[scan]['mu']
        edge_step = result[scan]['edge_step']
    
    
        mu_smoothed = savgol(mu,width_savgol,2)                       
        noise = abs(mu - mu_smoothed)
        noise_start_index = np.argmin(abs(energy - (e0 + norm1))) 
        noise_end_index = np.argmin(abs(energy - (e0 + norm2)))            
        noise_mean = np.sqrt(np.mean((noise[noise_start_index : noise_end_index])**2))
        noise_mean_norm = noise_mean/edge_step
                    
        result[scan]['mu_smoothed'] = mu_smoothed
        result[scan]['noise'] = noise
        result[scan]['noise_mean'] = noise_mean
        result[scan]['noise_mean_norm'] = noise_mean_norm
        
    print('')
    return result




def xas(n_first = 1, n_last = None, skiplist = None, path = None, calibrate = False, align = False, interpolate = False, exafs = False, merge = 1):
    
        
    ### Opening the file
    directory, filename, file_extension, dataset = load_file(path)

    ### Reading params.py file
    try:
        load_params(directory+"/params.py")
    except:
        load_params(directory+"\params.py")
    
    
    ### Creating the dictionary and filling it with raw data
    
    data = create_raw(dataset, directory, filename, n_first, n_last, skiplist, merge)

    #Calibration of the spectra          
    data = calibrate_spectra(calibrate, data, radius_calib = 5, acceptable_error = 10, Eref = Eref)
    
    # Alignment of the spectra            
    data = align_spectra(align, data, radius_align = 50, Ealign = Ealign )            
                
    # Interpolation of energy axis
    if merge !=1:
        if interpolate == False or interpolate == 'False' or interpolate == 'false':
            print(f'Merging without interpolation may lead to wrong results. Forcing interpolation anyway (interpolate = True)\n')
            interpolate = True
    data = interpolate_spectra(interpolate, data)            
    
    # Merging the spectra
    data = merge_spectra(data, merge)
    
    # Larch processing
    data = larch_spectra(data, exafs, e0, step, pre1, pre2, norm1, norm2, nnorm, nvict, make_flat, 
                      rbkg, nknots, splinekmin, splinekmax, splinekweight, kstep, clamp_lo, clamp_hi,
                      ftkmin, ftkmax, ftkweight, ftdk)
                
    # Calculate edge position
    data = calculate_edge(data, e0, radius_edge = 5, tolerance = 10)
                
    # Calculate noise
    data = calculate_noise(data, e0, norm1, norm2, width_savgol = 5)            
                
    
    return data
        

# Averages multiple processed datasets that have the same number of scans. The datasets must be aligned and calibrated using the same energy scale 
def average(datasets, exafs = False):    
    averaged_data = {}
        
    for scan in datasets[0]: # loop over the scans (1.1, 1.2, 1.3, ...)
        averaged_data[scan] = {}                                               
        
        description = f'Merge of {len(datasets)} datasets:'
        for d in datasets:
            description += fr' {d[scan]["filename"]}'    
        
        filename = f'Merge of {len(datasets)} datasets'
        
        directory = datasets[0][scan]['directory']
        
        number = datasets[0][scan]['number']
        
        merge = datasets[0][scan]['merge']
        
        
        #Energy
        energy = np.array([d[scan]['energy'] for d in datasets])
        for i in range(1,len(datasets)):
            if not np.array_equal(energy[0,:], energy[i,:]):        
                raise Exception("Energy scale of the scans to be averaged is not the same. You must set interpolate = 'load' in the xas function to prepare the datasets.")            
        energy = np.mean(energy, axis=0)
        
        # Mu
        mu = np.array([d[scan]['mu'] for d in datasets])
        mu = np.mean(mu, axis=0)
        
        # ref
        ref = np.array([d[scan]['ref'] for d in datasets])
        ref = np.mean(ref, axis=0)
        
        # timer_trig
        timer_trig = np.array([d[scan]['timer_trig'] for d in datasets])
        timer_trig = np.mean(timer_trig, axis=0)
        
        # temperature
        temperature = np.array([d[scan]['temperature'] for d in datasets])
        temperature = np.mean(temperature, axis=0)
        
        # primes
        mu_prime = np.gradient(mu, energy)
        ref_prime = np.gradient(ref, energy)
        ref_prime_smoothed = savgol(ref_prime,7,2)
        
        averaged_data[scan]['filename'] = filename
        averaged_data[scan]['directory'] = directory
        averaged_data[scan]['description'] = description             
        
        averaged_data[scan]['energy'] = energy
        averaged_data[scan]['mu'] = mu
        averaged_data[scan]['ref'] = ref
        averaged_data[scan]['timer_trig'] = timer_trig
        averaged_data[scan]['temperature'] = temperature
        
        averaged_data[scan]['mu_prime'] = mu_prime
        averaged_data[scan]['ref_prime'] = ref_prime
        averaged_data[scan]['ref_prime_smoothed'] = ref_prime_smoothed
        
        averaged_data[scan]['comment'] = None
        averaged_data[scan]['start_time'] = None
        averaged_data[scan]['rel_time'] = None
        averaged_data[scan]['number'] = number
        averaged_data[scan]['merge'] = merge
        
        
    # Larch processing
    averaged_data = larch_spectra(averaged_data, exafs, e0, step, pre1, pre2, norm1, norm2, nnorm, nvict, make_flat, 
                      rbkg, nknots, splinekmin, splinekmax, splinekweight, kstep, clamp_lo, clamp_hi,
                      ftkmin, ftkmax, ftkweight, ftdk)
                
    # Calculate edge position
    averaged_data = calculate_edge(averaged_data, e0, radius_edge = 5, tolerance = 10)
                
    # Calculate noise
    averaged_data = calculate_noise(averaged_data, e0, norm1, norm2, width_savgol = 5)            
        
    
  
    return averaged_data
                    
        
def concatenate(datasets, exafs = False, merge = 1):
    result = {}
    counter = 1

    for dataset in datasets:
        for key, value in dataset.items():
            new_key = f"{counter}"
            result[new_key] = value
            counter += 1
    
    # Merging the spectra
    result = merge_spectra(result, merge)
    
    # Larch processing
    result = larch_spectra(result, exafs, e0, step, pre1, pre2, norm1, norm2, nnorm, nvict, make_flat, 
                      rbkg, nknots, splinekmin, splinekmax, splinekweight, kstep, clamp_lo, clamp_hi,
                      ftkmin, ftkmax, ftkweight, ftdk)
                
    # Calculate edge position
    result = calculate_edge(result, e0, radius_edge = 5, tolerance = 10)
                
    # Calculate noise
    result = calculate_noise(result, e0, norm1, norm2, width_savgol = 5)                        
          
    

    return result
   



def gaussian(x, amp, cen, wid):
            return amp * np.exp(-(x-cen)**2 / wid)




    
    
    