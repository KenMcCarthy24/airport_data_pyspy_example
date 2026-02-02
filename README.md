This Repo contains the code used for a demonstration of using the py-spy library to optimize python code that performs and analysis on
flight data from the Bureau of Transportation Statistics (BTS). 

# Folders/Files
* **data folder**: For the raw data pulled from BTS. Too large to upload to GitHub.
  * Available at: https://www.kaggle.com/datasets/kennethmccarthy/early-2025-flight-data/data
* **environment.yml**: Contains the necessary libraries for running the notebook
* **raw_data_formatting.py**: Processes raw data into the format used for the analysis
* **slow_analysis.py**: Performs the data analysis in a slow and inefficient way
* **profile.svg**: Py-spy icicle plot output profiling slow_analysis.py
* **fast_analysis.py**: Performs the data analysis in a faster optimized way