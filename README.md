README

Code used in Stone et al. (in review, ApJ) for GAMA quasar host star formation history paper analysis.

-------

# Author
This code is developed by Maria B. Stone.

# Last Updated
October 19th, 2025


# Motivation
⚠️ Note
This repository contains the code and work-in-progress analysis for my study on quasar host star formation. 
The code is under active development.
Only a small representative data is included (not the full catalog).


# Background


-------

The code demonstrates:
- How to 


## Usage

A small example on how to start using this code.




## Notes

* Scratch Notebooks are included to show full workflow and reasoning, see 4_scratchcode_notes/ directory.

* Core functions in code/ are reusable for other projects.

* This repository is a work in progress and will be updated as analyses continue.



## References

* GAMA Survey: https://www.gama-survey.org

* CIGALE SED fitting: https://cigale.lam.fr

* MAGPHYS SED fitting: https://www.iap.fr/magphys



## Acknowledgments

Guidance on coding workflow and documentation provided by OpenAI’s ChatGPT (GPT-5).



## Citation

If you use this example or its concepts, please cite:

**Stone, M. (in review, ApJ)**


--------


## Files

- `1_tables/`    # This is a director with all of the data tables. As of now, since the paper is not published, only subsamples.

results_galaxies.fits     #Subsample of results for control galaxies from CIGALE fits

12_data_seed_gals_set199_magphys.fits    #Subsample of data from MAGPHYS database for control galaxies



- `4_code/`      # This directory contains all of the clean code. I aim for this code to be reusable, especially the functions.

functions_GAMA_github.ipynb	    # Jupyter notebook of functions used in this analysis
functions_GAMA_github.py        # Same as above, but as a python file / python module



- `4_scratchcode_notes/`    # This directory contains Jupyter notebooks showing step-by-step calculations, visualizations, and intermediate checks. These notebooks demonstrate the workflow, reasoning, and plots used in the analysis. These notebooks are for transparency and exploration.

# END
