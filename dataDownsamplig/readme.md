Script for downsampling large data for plotting purposes. 
the data is downsampled to the max HD resolution width - 1980 px

2 algorithms are used:
 - the LTTB - adapted after https://github.com/javiljoen/lttb.py
 - sampling the min and max value in subarays of the data set
 
 the Script takes as input a python dictionary, a pandas dataframe or a numpy array.
 It returns the same data type as the input. 
