import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gs

from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit


 
def lc_check(data, components,div_vals, LCA_fit = False):
    
    lcf_dic = {}
    # Extract energy and remove the first column from data and components
    energy = data[:, 0]
    data = np.delete(data, 0, 1)
    components = np.delete(components, 0, 1)
    
    X = components
    Y = data
    
    num_scans = data.shape[1]
    colnum = components.shape[1]
    conc = np.empty((num_scans, colnum))
    
    
    for i in range(num_scans):
        scan = data[:, i]
        reg = LinearRegression(positive=True).fit(components,scan)
        conc[i, :] = reg.coef_
    
    # Plot references
    plt.figure(figsize=(7, 8), dpi=300)
    for i in range(colnum):
        plt.plot(energy, components[:, i], label=str(i + 1))
    plt.title('Imported references')
    plt.ylabel(r'Normalized $\mu$')
    plt.xlabel('Energy')
    plt.legend()
    plt.show()
    
    # plot concentrations
    plt.figure(figsize=(10, 4), dpi=300)
    for i in range(colnum):
        plt.plot(conc[:, i], label=f'Component {i+1}')
    
    if div_vals is not None:
        # Get the colormap and the number of colors in it
        colormap = cm.get_cmap('Pastel1')
        num_colors = colormap.N

        # Generate a list of colors by cycling through the colormap
        colors = [colormap(i % num_colors) for i in range(len(div_vals))]
        
        for i in range(len(div_vals)):
            if i == 0:
                plt.axvspan(0, div_vals[i], facecolor=colors[i], alpha=0.5)
            else:
                plt.axvspan(div_vals[i-1], div_vals[i], facecolor=colors[i], alpha=0.5)
    plt.xlabel('Scans')
    plt.ylabel('Concentration')
    plt.legend()
    plt.show()
    
    diff = (data - (np.matmul(components, conc.T)))**2
    diff = diff.sum(axis = 0)/10000
    
    r_factor_top = ((data - (np.matmul(components, np.transpose(conc)))))**2
    r_factor_top = r_factor_top.sum(axis = 0)
    r_factor_bottom = data**2
    r_factor_bottom = r_factor_bottom.sum(axis=0)
    r_factor = r_factor_top/r_factor_bottom
    
    plt.figure(figsize = (10,4),dpi=300)
       
    plt.plot(r_factor, label = str(i+1)+' component')
    plt.xlabel('Scans')
    plt.ylabel('R-factor')
    
    if div_vals is not None:
        # Get the colormap and the number of colors in it
        colormap = cm.get_cmap('Pastel1')
        num_colors = colormap.N

        # Generate a list of colors by cycling through the colormap
        colors = [colormap(i % num_colors) for i in range(len(div_vals))]
    
        for i in range(len(div_vals)):
            if i == 0:
                plt.axvspan(0, div_vals[i], facecolor=colors[i],alpha=0.5)
            else:
                plt.axvspan(div_vals[i-1], div_vals[i],facecolor=colors[i], alpha=0.5)
            
    plt.show()
    
    lcf_dic['R-factor'] = r_factor
    lcf_dic['Concentration'] = conc
    lcf_dic['Components']= components
    
    if LCA_fit == True:
        while True:
            scan_input = input("Please select a scan number for the MCR fit (or 'q' to quit): ")
            
            if scan_input.lower() == 'q':
                break

            scan_input = int(scan_input)
        
            fig = plt.figure(figsize=(8, 7),dpi=300)
            g = gs.GridSpec(2, 1, height_ratios=[5, 1])
            ax1 = fig.add_subplot(g[0])
            ax2 = fig.add_subplot(g[1])
            ax2.set_xlabel('Energy', size=12)
            ax1.set_ylabel('Intensity', size=12)
            ax2.set_ylabel('Residuals', size=12)
            ax1.set_title('LCF Fit', size=15)
            
            
            line, = ax1.plot(energy, data[:,scan_input], color='black', label='Spectrum: '+str(scan_input))
            line1, = ax1.plot(energy, np.matmul(components, np.transpose(conc))[:,scan_input], color='blue', label="LCA")
            residuals = data[:, scan_input] - np.matmul(components, np.transpose(conc))[:,scan_input]
            line2, = ax2.plot(energy, residuals)
            ax1.legend()
            plt.show()
            
    return lcf_dic

