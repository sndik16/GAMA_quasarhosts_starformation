#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from astropy.table import Table, join
from astropy import units as u


# In[ ]:


# combine CIGALE and MAGPHYS table data for normal galaxies based on CATAID.

def controlgxs_join_magphys_cigale_results(cigale_file, magphys_file, id_col='id'):
    
    """
    Join CIGALE and MAGPHYS tables for normal galaxies.
    
    Parameters
    ----------
    cigale_file : str
        Path to the CIGALE results table.
    magphys_file : str
        Path to the MAGPHYS results table.
    id_col : str
        Column name in the CIGALE table to match with MAGPHYS (default 'id').
    
    
    Returns
    -------
    astropy.table.Table
        Joined table with all data.
    """
    
    # Open the CIGALE results table for normal galaxies.
    
    data_cigale = Table.read(cigale_file)

    # We need to change the ID column name to 'CATAID', so that it matches 
    # the second datatable, so that we can combine the datatables based on
    # the CATAID value.
    
    data_cigale.rename_column(id_col, 'CATAID')
    
    # Open the MAGPHYS data for normal galaxies.

    data_magphys = Table.read(magphys_file)

    '''
    Now, we work on joining the tables together based on the CATAIDs.

    Now, each normal galaxy entry (defined by its CATAID) has on the same row
    the SFR estimate from CIGALE and from MAGPHYS.
    '''
    
    # Join the tables for the relevant CATAIDs (Astropy **join** operation).
    
    data = join(data_cigale, data_magphys, keys='CATAID')
    
    return data


# In[ ]:


# I have to compute a better uncertainty measurement for the bins, because I am reporting medians
# I use bootstrap method

def median_e_bootstrap (data_array, N_boot):
    
    """
    Inputs
    data_array : an array of float values
    N_boot : the number of times to resample
    
    Returns
    median_error : the uncertainty associated with the median in an array
     
    This function takes in a data array, and computes the uncertainty associated
    to the median using the bootstrap method.
    You have to specify the number of times the data array has to be resampled.

    """
    
    rng = np.random.default_rng(42)
    # a random number generator for reproducibility
    
    # an array to store bootstrap medians
    boot_medians = np.empty(N_boot)
    
    # Perform boot strap resampling
    N = len(data_array)
    
    for i in range(N_boot):
        
        # Resample N points with replacement from the original data
        sample = rng.choice(data_array, size=N, replace=True)
        
        # Compute the median of this resampled sample
        boot_medians[i] = np.median(sample)
        
    # compute original median
    median_original = np.median(data_array)
    
    #compute bootstrap estimate of uncertainty
    median_error = np.std(boot_medians, ddof=1)
    
    return median_error

