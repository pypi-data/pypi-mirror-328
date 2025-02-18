bm23id24_xas is a python library based on xraylarch, pyfitit and pymca
It is created on BM23 and ID24 beamlines of the European Synchrotron Radiation Facility (ESRF)
It provides tools for analysis of X-ray Absorption spectroscopy data 

bm23id24_xas consists of 4 modules:
 - xas
 - pca_estimator
 - MCR-ALS 
 - LCA
 
 xas allows to load the data in .h5 format (the standart format for BM23 and ID24 beamlines after 2020 ESRF upgrade), perform calibration, alignment, interpolation, merge, normalization and EXAFS extraction. The result is a dictionary contatining scan numbers as keys and arrays with processed data as sub-dictionaries. The result is a dictionary.

 xas exist in an old xas_v2_6 and new xasproc_v2_82 forms to test the new form
 
 pca_estimator works with the dictionary produced by xas but can also work with an independent txt file contatining energy as the first column and normalized XAS spectra as 2nd and other columns. It allows to interactivelly perform PCA. The function is based on pyfitit, but readapted for the needs of the beamline users. The result is a dictionary.
 
 MCR-ALS works with the dictionary produced by xas, but can also work with an independent txt file contatining energy as the first column and normalized XAS spectra as 2nd and other columns. It allows to interactivelly perform MCR-ALS analysis. It is possible to provide reference spectra if needed as dictionaries produced by xas or txt files if needed. The result is a dictionary.
 
 LCA works with the dictionary produced by xas, but can also work with txt files for both, data and references.
 
