METADATA

Metadata: METADATA:Helps to understand the properties of a dataset,such as its isze, column names, data types, or source, making it easier to work with and analyze the data

Import Library

#Import the pandas library makes the pandas library available for use in coding
#It allows us to use pd instead of typing pandas every time we want to use pandas functions

import pandas as pd
 
#Import the numpy library makes the numpy library available for use in coding
#It allows us to use np instead of typing numpy every time we want to use numpy functions

import numpy as np
 
Install dependencies

#Install dependencies: pandas and numpy relies on other libraries to function properly.

%pip install openpyxl

#Dependencies provide essential functionality for pandas to work correctly

#data path is the location of a file (Excel,CSV,JSON) or dataset that you want to load into a DataFrame
data_path = "/Workspace/Users/besteve4luv@gmail.com/Viewership Analysis .xlsx"
 
Data Reading

#Data reading is a function used to read data from a file or dataset into a DataFrame

df=pd.read_excel('/Workspace/Users/besteve4luv@gmail.com/Viewership Analysis .xlsx')
df:pandas.core.frame.DataFrame = [DateID: int64, CustomerID: object ... 4 more fields]

Display Function

#Display() is a visually presents a DataFrame in a formatted way, showing columns, index, and data in a table format which is more readable

display(df)
 

Table
10,000+ rows
|
Truncated data
|
6.25s runtime
Refreshed 39 minutes ago

Shape Function

 #df.shape: it provides the number of rows and columns in a DataFrame 
 
df.shape
(118534, 6)

Dtypes Functions

#df.dtypes is an attribute that returns the data types of each column in the DataFrame
df.dtypes
 
DateID               int64
CustomerID          object
TotalTimeWatched     int64
Platform            object
PlayEventType       object
VideoTitle          object
dtype: object


Columns Function
#df.columns is used to inspect or manipulate the column labels of the DataFrame

df.columns
 
Index(['DateID', 'CustomerID', 'TotalTimeWatched', 'Platform', 'PlayEventType',
       'VideoTitle'],
      dtype='object')

Info() Function
#df.info() provides a concise summary of the DataFrame, including the number of rows, column names, data types, and memory usage

df.info()
 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 118534 entries, 0 to 118533
Data columns (total 6 columns):
 #   Column            Non-Null Count   Dtype 
---  ------            --------------   ----- 
 0   DateID            118534 non-null  int64 
 1   CustomerID        118534 non-null  object
 2   TotalTimeWatched  118534 non-null  int64 
 3   Platform          118534 non-null  object
 4   PlayEventType     118534 non-null  object
 5   VideoTitle        118534 non-null  object
dtypes: int64(2), object(4)
memory usage: 5.4+ MB

Platform Unique Function
#Platform unique values returns an index object containing the names of all columns in the DataFrame

df['Platform'].unique()
 
array(['Leanback', 'iOS', 'Web', 'Android'], dtype=object)

VideoTitle Unique Function
#VideoTitle unique value extracts all distinct values from the videotitle column, which is useful for identiftying unique video title in a dataset 

df['VideoTitle'].unique()
 
array(["F1 '20: Emilia Romagna GP", 'Chasing The Sun',
       'Sonic The Hedgehog', ..., 'Baby', 'Iron Man 3',
       'The Campaign Against The Climate'], dtype=object)

TotalTimeWatched Sum() Function
#TotalTimeWatched.sum() is for aggregating numerical data, such as totalling the time watched for videos

df['TotalTimeWatched'].sum()
242623672

TotalTimeWatched.min() Function
#TotalTimeWatched.min() is the finding the minimum value in a numerical column, such as the shortest time watched for a video

df['TotalTimeWatched'].min()
 
1
 
 TotalTimeWatched.max() Function
#TotalTimeWatched.max() is the finding the maximum value in a numerical column, such as the longest time watched for a video

df['TotalTimeWatched'].max()
 
88500

Duplicated.sum() Function
#duplicated.sum() is used to count the number of duplicate rows in a DataFrame

df.duplicated().sum()
 
9873

Drop_duplicates(inplace=True) and df.duplicated().sum() Function
#df.drop_duplicates(inplace=True): Removes duplicate rows from the DataFrame and modifies it in place
#df.duplicated().sum(): Counts the number of duplicate rows in the DataFrame after the operation

df.drop_duplicates(inplace=True)
df.duplicated().sum()

0
Shape Function
df.shape
 
(108661, 6)

#df.index(): Returns the index row labels of the DataFrame

df.index
Index() Function

 
Int64Index([     0,      2,      4,      5,      6,      8,      9,     10,
                11,     12,
            ...
            118524, 118525, 118526, 118527, 118528, 118529, 118530, 118531,
            118532, 118533],
           dtype='int64', length=108661)

df.size() Function
#df.size(): Returns the total number of elements in the DataFrame (rows*columns) and gives the result as an integer

df.size
 
651966

df.ndim() Function
#df.ndim(): Returns the number of dimensions of the DataFrame(always 2 for a DataFrame)
#Output it as integer (2 for DataFrame, 1 for series)

df.ndim
 
2

df.empty Function
#df.empty: Returns True if the DataFrame is empty (no rows or columns), False otherwise.
#Output it a Boolean

df.empty

False

df.memory_usage() Function
#df.memory_usage(): Returns the memory usage of each column in the DataFrame
#Output: Series with column names as the index and memory usage as values

df.memory_usage()

 
Index               869288
DateID              869288
CustomerID          869288
TotalTimeWatched    869288
Platform            869288
PlayEventType       869288
VideoTitle          869288
dtype: int64
df.head() Function

 

df.tail() Function
#df.tail() as a method that displays the last five rows of the Dataframe

df.tail()

df.head() Function
 #df.head() is a method that displays the first five rows of the Dataframe
df.head()

df.sample() Function
#df.sample() is a method used to randomly select a specified number of rows or columns from a DataFrame
#It's useful for creating a random sample of your data for tasks like exploratory, testing,splitting datasets.

df.sample()

df.describe() Function
#Summary statistics for numerical columns
df.describe()
	DateID	TotalTimeWatched
count	1.086610e+05	108661.000000
mean	2.020947e+07	2140.043180
std	2.550794e+03	3803.223852
min	2.020110e+07	1.000000
25%	2.021012e+07	300.000000
50%	2.021022e+07	1121.000000
75%	2.021032e+07	2520.000000
max	2.021042e+07	88500.000000
