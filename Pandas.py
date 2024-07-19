
# this repo includes all the code related to Pandas library in Python

import numpy as np
import pandas as pd
dict1 = {
    "Name" : ["Talha" , "Sheikh" , "Ali" , "Fahad" , " Saleem"] , 
    "Age" : [20, 21 , 22, 19 , 7] ,
    "City" : ["Mansehra", "Karachi" , "Lahore" , "Qalandarabad" , "Abbottabad" ] , 
    "Marks" : [99, 88, 45, 76 , 67 ]
}

# DataFrame() function will convert simple data to datasheet
# DataFrame must be in camel format
a = pd.DataFrame(dict1)
print ( a )
# Output->   
#        	Name	 Age	  City	       Marks
#        0	Talha	 20	 Mansehra	99
#        1	Sheikh	 21	 Karachi        88
#        2	Ali      22	 Lahore	        45
#        3	Fahad  	 19	 Qalandarabad   76
#        4	Saleem	  7	 Abbottabad	67

# csv  stands for comma separated values
# csv files is sheet of comma sepated values 

# import data to MS Excel datasheet
# to_csv('filename.extension') function will be used 
a.to_csv('friends.csv')

# if we don't want first column then
a.to_csv('friends_index_false.csv' , index = False) 


# F in False must be capital in python
# first column (serial No ) will be accessed by index = True

# we can access values of any column by column name and can access row by index number

# wanna see starting two rows then  .head()  function is used
# Often used when data is too large like more than 100 rows and then we wanna see starting some rows
df.head(2)
# Output-> 
#         	Name	 Age	    City	     Marks
#         0	Talha	 20	    Mansehra	     99
#         1	Sheikh	 21	    Karachi	     88

a.head(3)
# Output-> 
#                 Name	 Age 	    City	 Marks
#         0	Talha	 20	    Mansehra	 99
#         1	Sheikh	 21	    Karachi  	 88
#         2	Ali	 22	    Lahore  	 45

# Wanna see ending rows of given dataset then .tail()  function is used
df.tail(2)
# Output-> 
#         	Name	Age	City	        Marks
#         3	Fahad	19	Qalandarabad	76
#         4	Saleem	7	Abbottabad	67

# By default pd.tail() and pd.head() function takes 5 as an argument

# to read data from csv sheet then
# pd.read_csv('filename.csv') when file is in the same folder 
# pd.read_csv('file_path.csv') when file is not in the same folder then we have to give complete file path and change backward salshes into forward slashes
# Example
b = pd.read_csv('sheikh_.csv')


# to read data / import excel file then we have to import openpyxl library
c = pd.read_excel ("second.xlsx")
print(c)

# for statistical analysis of columns having numerical values then .describe()  function is used
b.describe()
# Output-> 
#           	Age	        Marks
#           count	5.000000	5.000000
#           mean	17.800000	75.000000
#           std	6.140033	20.676073
#           min	7.000000	45.000000
#           25%	19.000000	67.000000
#           50%	20.000000	76.000000
#           75%	21.000000	88.000000
#           max	22.000000	99.000000


# # to access specific column e.g marks
b['marks']
# Output-> 
#        0    99.0
#        1    88.0
#        2    89.0
#        3    98.0
#        4    78.0
#        5     8.0
#        6    87.0
#        7     NaN
#        8     NaN
#    Name: marks, dtype: float64

# To access specific value from specific column
b['marks'][0]
# Output-> 
np.float64(99.0)

# To change specific value or overwrite
b['marks'][0] = 3
print(b)
# Output->
#      	age	marks	Unnamed: 2
#      0	23.0	3.0	NaN
#      1	32.0	88.0	NaN
#      2	34.0	89.0	NaN
#      3	33.0	98.0	NaN
#      4	43.0	78.0	NaN
#      5	45.0	8.0	NaN
#      6	65.0	87.0	NaN
#      7	NaN	NaN	NaN
#      8	NaN	NaN	NaN

# To change index No 
b.index = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eight", "ningth"]
print(b)
# Output->
#     	age	marks	Unnamed: 2
#      first	23.0	3.0	NaN
#      second	32.0	88.0	NaN
#      third	34.0	89.0	NaN
#      forth	33.0	98.0	NaN
#      fifth	43.0	78.0	NaN
#      sixth	45.0	8.0	NaN
#      seventh	65.0	87.0	NaN
#      eight	NaN	NaN	NaN#      
#      ningth	NaN	N#      aN	NaN

# To get info about data
print(d.info() )
# Output-> 
#     <class 'pandas.core.frame.DataFrame'>
#     RangeIndex: 9 entries, 0 to 8
#    Data columns (total 3 columns):
#   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
#     0   age         7 non-null      float64
#     1   marks       7 non-null      float64
#     2   Unnamed: 2  0 non-null      float64
#     dtypes: float64(3)
#     memory usage: 348.0 bytes
#     None

# For statistical analysis of data a.describe() function will be used
# For getting general info about data a.info() function will be used

# To check null values in every column
print( d.isnull().sum() )
# Output-> 
#      age           2
#      marks         2
#      Unnamed: 2    9
#      dtype: int64

# To check duplicate values
print( d["age"].duplicated().sum() )
# Output->      1

# Duplicate function will use when we are dealing with duplicate values and wanna find it then we will find it from a unique column/serial No/ RollNo
print( d.duplicated().sum() )
# Output->    
#     1

# For drop duplicate values drop_duplicates("column_name") function will be used
print(d.drop_duplicates( "age" ) )
# Output->
#          age  marks
#        0   23     99
#        1   32     88
#        2   34     89
#        3   33     98
#        4   43     78
#        5   45      8
#        6   65     87

# When working with large data then .dropna() function will be used But we have to know that 
# in every scenario we are not supposed to use this function e.g in a company while dealing with 
# duplicate data, if we use this function then this will remove some data at the end we are required
# count the total employee then there will be ambiguity in results.
print( d.dropna())
# Output-> 
#         age  marks
#      0   23     99
#      1   32     88
#      2   34     89
#      3   33     98
#      4   43     78
#      5   45      8
#      6   65     87
#      7   43      2

# Replacing nan(not a number) values 
import numpy as np
print( d.replace(np.nan, "hello" ) ) # but this will replace all the nan values( int/string/float/char) with hello(string)

# For Replacing specific value d["column_name"].replace(np.nan, new_value) )
print( d["age"].replace(np.nan, 18 ) )
 # OR 
_c = d["age"].replace(np.nan, 18 )
print(_c)

# Best approch to replace data of int/float type is first find mean of data(int/float)
# column having nan values and then replace nan values with mean this not affect data
print(d["age"].mean() )
# Output->    39.75
print( d["age"].replace( np.nan, 39.75 ) )

# Best approch to replace data of string type is using backward fill or forward fill method
print( a.fillna( method = "bfill" ) )    # bfill is backward fill
# OR print( a.fillna( method = "ffill" ) )   # ffill is forward fill  

# Column Transformation in Pandas
d.loc[ ( d  ["age %" ] == 0), "new_age"  ]= 18 
d.loc[ ( d  ["age %" ] > 0), "new_age"  ]= 19 


f = pd.read_excel ('sheikh.xlsx' )
print ( f )
# Output->    
#         First Name Last Name  age  marks
#       0      Talha    Sheikh   23     99
#       1      Azeem      Azam   32     88
#       2     Saleem    Shokat   34     89
#       3     Kaleem    Faheem   33     98
#       4    Shakeel      Niaz   43     78
#       5       Faiz      Umar   45      8
#       6       Riaz     Usman   65     87

# Combining two columns
f["Full Name"] = f["First Name"] +" " + f[ "Last Name" ]
print ( f )
# Output->  
#            First Name   Last Name  age   marks      Full Name
#       0      Talha       Sheikh     23     99     Talha Sheikh
#       1      Azeem       Azam       32     88     Azeem Azam
#       2      Saleem      Shokat     34     89     Saleem Shokat
#       3      Kaleem      Faheem     33     98     Kaleem Faheem
#       4      Shakeel     Niaz       43     78     Shakeel Niaz
#       5      Faiz        Umar       45      8     Fai#       z Umar
#       6      Riaz        Usman      65     87     Riaz Usman

f["Full Name"] = f["First Name"].str.capitalize() +" " + f[ "Last Name" ].str.capitalize()
print ( f )
# Output->
#           First Name    Last Name  age  marks      Full Name
#       0      Talha      Sheikh     23     99     Talha Sheikh
#       1      Azeem      Azam       32     88     Azeem Azam
#       2      Saleem     Shokat     34     89     Saleem Shokat
#       3      Kaleem     Faheem     33     98     Kaleem Faheem
#       4      Shakeel    Niaz       43     78     Sh#       akeel Niaz
#       5      Faiz       Umar       45      8     Faiz Umar
      
f["Percentage"] = f["marks"]/100
print(f)
# Output->
#         First Name Last Name  age  marks      Full Name  Percentage
#       0      Talha    Sheikh   23     99   Talha Sheikh        0.99
#       1      Azeem      Azam   32     88     Azeem Azam        0.88
#       2     Saleem    Shokat   34     89  Saleem Shokat        0.89
#       3     Kaleem    Faheem   33     98  Kaleem Faheem        0.98
#       4    Shakeel      Niaz   43     78   Shakeel Niaz        0.78
#       5       Faiz      Umar   45      8      Faiz Umar        0.08
#       6       Riaz     Usman   65     87     Riaz Usman        0.87


# Make a new column from existing one and also make a function to implement function on all the values once
h = { "Months" : 
    [ "January", "Febuary", "March", "April",
     "May", "June", "July", "August", "September", 
     "October", "November ", "December" ]  }
_h = pd.DataFrame(h)
print (_h,"\n")

def extract(value):
    return value[0:3]
_h["Short_Months" ] = _h["Months"].map(extract)
print(_h)
# Output->
#             Months     Short_Months
#       0     January       Jan
#       1     Febuary       Feb
#       2     March         Mar
#       3     April         Apr
#       4     May           May
#       5     June          Jun
#       6     July          Jul
#       7     August        Aug
#       8     Septembe      Sep
#       9     October       Oct
#       10    November      Nov
#       11    December      Dec

# To check summary of data .groupby("column_name").agg( {"coumn_name": "count"})  function will be used
print ( f.groupby("Gender").agg( {"Full Name": "count"}) )
# Output->
#                Full Name
#       Gender           
#       female          6
#       male            7

# To check summary of data .groupby("column_name").agg( {"coumn_name": "count"})  function will be used
# Single Parameter
print ( f.groupby([ "Gender", "Country"]).agg( {"Full Name": "count"}) )
# Output->
#                      Full Name
#        Gender  Country               
#        female  Afghanistan          3
#                Bangladesh           3
#        male    India                2
#                Netherland           1
#                Pakistan             3
#                Srilanka             1

# Single Parameter
print ( f.groupby([ "Gender", "Country"]).agg( {"age": "mean"}) )
# Output->
#                    age
#        Gender  Country               
#        female  Afghanistan  20.333333
#                Bangladesh   36.000000
#        male    India        33.500000
#                Netherland   65.000000
#                Pakistan     33.333333
#                Srilanka     43.000000

# Single Parameter
print ( f.groupby([ "Gender", "Country"]).agg( {"age": "max"}) )
# Output->
#                  age
#        Gender  Country         
#        female  Afghanistan   31
#                Bangladesh    59
#        male    India         34
#                Netherland    65
#                Pakistan      45
#                Srilanka      43

# Double Parameter
print ( f.groupby([ "Gender", "Country"]).agg( {"age": "max", "marks" : "max"}) )
# Output->
#                  age  marks
#        Gender  Country                
#        female  Afghanistan   31     82
#                Bangladesh    59     92
#        male    India         34     98
#                Netherland    65     87
#                Pakistan      45     99
#                Srilanka      43     78


data1 = { 
    "EID" : [ "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8" , "e9"],
    "Salary" : [9000, 8000, 7000, 9900, 3900, 5600, 2549, 7600, 3980],
    "Name" : [ " Sheikh" , "Saleem" , "Kaleem", "Hafeez", " Ibrar", "Qasim" , "Jabar", "Qadir", "Saad" ] }
data2 = {
    "EID" : [ "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8" , "e9"],
    "Age" : [ 18, 20, 29, 50, 43, 39, 68, 23, 76] }
d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)
print( d1, "\n\n", d2 )
# Output->
#         EID  Salary     Name
#       0  e1    9000   Sheikh
#       1  e2    8000   Saleem
#       2  e3    7000   Kaleem
#       3  e4    9900   Hafeez
#       4  e5    3900    Ibrar
#       5  e6    5600    Qasim
#       6  e7    2549    Jabar
#       7  e8    7600    Qadir
#       8  e9    3980     Saad 

#          EID  Age
#       0  e1   18
#       1  e2   20
#       2  e3   29
#       3  e4   50
#       4  e5   43
#       5  e6   39
#       6  e7   68
#       7  e8   23
#       8  e9   76

# Merge data ( merge data from different data sets )
print(pd.merge(d1,d2) )
# Output->
#         EID  Salary     Name  Age
#       0  e1    9000   Sheikh   18
#       1  e2    8000   Saleem   20
#       2  e3    7000   Kaleem   29
#       3  e4    9900   Hafeez   50
#       4  e5    3900    Ibrar   43
#       5  e6    5600    Qasim   39
#       6  e7    2549    Jabar   68
#       7  e8    7600    Qadir   23
#       8  e9    3980     Saad   76

# Merge data ( merge data from different data sets )
print(pd.merge(d1,d2) )
# OR
print()
print(pd.merge(d1,d2, on = "EID") )
# We merge data in this mannaer only when there is no nan value or there are equal Number of values in both datasets
# Output->
#        EID  Salary     Name  Age
#      0  e1    9000   Sheikh   18
#      1  e2    8000   Saleem   20
#      2  e3    7000   Kaleem   29
#      3  e4    9900   Hafeez   50
#      4  e5    3900    Ibrar   43
#      5  e6    5600    Qasim   39
#      6  e7    2549    Jabar   68
#      7  e8    7600    Qadir   23
#      8  e9    3980     Saad   76

#        EID  Salary     Name  Age
#      0  e1    9000   Sheikh   18
#      1  e2    8000   Saleem   20
#      2  e3    7000   Kaleem   29
#      3  e4    9900   Hafeez   50
#      4  e5    3900    Ibrar   43
#      5  e6    5600    Qasim   39
#      6  e7    2549    Jabar   68
#      7  e8    7600    Qadir   23
#      8  e9    3980     Saad   76

data1 = { 
    "EID" : [ "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8" , "e9"],
    "Salary" : [9000, 8000, 7000, 9900, 3900, 5600, 2549, 7600, 3980],
    "Name" : [ " Sheikh" , "Saleem" , "Kaleem", "Hafeez", " Ibrar", "Qasim" , "Jabar", "Qadir", "Saad" ] }
data3 = {
    "EID" : [ "e11", "e22", "e3", "e4", "e5", "e6", "e77", "e8" , "e9"],
    "Age" : [ 18, 20, 29, 50, 43, 39, 68, 23, 76] }
d1 = pd.DataFrame(data1)
d3 = pd.DataFrame(data3)

# there are different values in employee id column(EID) of both sets, So if we try to merge data in simple way ( on ) then 
# then We will get only  6 indices out of 9 bcz in 3 record are different from each datasets ( having no common a
print( pd.merge( d1,d3) )
# Or
print( pd.merge ( d1,d3 , on = "EID" , how = "inner" ) )
# Both have same meaning/ same output
# Output->
#        EID  Salary    Name  Age
#      0  e3    7000  Kaleem   29
#      1  e4    9900  Hafeez   50
#      2  e5    3900   Ibrar   43
#      3  e6    5600   Qasim   39
#      4  e8    7600   Qadir   23
#      5  e9    3980    Saad   76

# To get all the values of first dataset and get nan value on that index on which there is no value in second dataset
print( pd.merge ( d1,d3 , on = "EID" , how = "left" ) )
# Output->
#        EID  Salary     Name   Age
#      0  e1    9000   Sheikh   NaN
#      1  e2    8000   Saleem   NaN
#      2  e3    7000   Kaleem  29.0
#      3  e4    9900   Hafeez  50.0
#      4  e5    3900    Ibrar  43.0
#      5  e6    5600    Qasim  39.0
#      6  e7    2549    Jabar   NaN
#      7  e8    7600    Qadir  23.0
#      8  e9    3980     Saad  76.0

print( pd.merge ( d1,d3 , on = "EID" , how = "right" ) )
# Or
print( pd.merge ( left = d1, right = d3 , on = "EID" , how = "right" ) )
# To get all the values of second dataset and get nan value on that index on which there is no value in first dataset
# Output->
#         EID  Salary    Name  Age
#      0  e11     NaN     NaN   18
#      1  e22     NaN     NaN   20
#      2   e3  7000.0  Kaleem   29
#      3   e4  9900.0  Hafeez   50
#      4   e5  3900.0   Ibrar   43
#      5   e6  5600.0   Qasim   39
#      6  e77     NaN     NaN   68
#      7   e8  7600.0   Qadir   23
#      8   e9  3980.0    Saad   76
#         EID  Salary    Name  Age
#      0  e11     NaN     NaN   18
#      1  e22     NaN     NaN   20
#      2   e3  7000.0  Kaleem   29
#      3   e4  9900.0  Hafeez   50
#      4   e5  3900.0   Ibrar   43
#      5   e6  5600.0   Qasim   39
#      6  e77     NaN     NaN   68
#      7   e8  7600.0   Qadir   23
#      8   e9  3980.0    Saad   76

# Concatenate two datasets
data5 = { 
    "EID" : [ "e1", "e2", "e3", "e4", "e5"],
    "Age" : [23,52,26,70,10]}
data4 = {
    "EID" : [ "e6", "e7", "e8", "e9"],
    "Age" : [ 18, 20, 29, 50] }
d5 = pd.DataFrame(data5)
d4 = pd.DataFrame(data4)
print( pd.concat ( [d5,d4] ) )
# Output-> 
#       EID  Age
#     0  e1   23
#     1  e2   52
#     2  e3   26
#     3  e4   70
#     4  e5   10
#     0  e6   18
#     1  e7   20
#     2  e8   29
#     3  e9   50

print( d4 )
# Output-> 
#      EID  Age
#    0  e6   18
#    1  e7   20
#    2  e8   29
#    3  e9   50

# Copy data in new dataset from existing dataset
d6 = d4.copy()
d6.loc[0, "EID"] =  "e9"
d6.loc[0,"Age" ] = 29
print ( d6 )
# Output-> 
#      EID  Age
#    0  e9   29
#    1  e7   20
#    2  e8   29
#    3  e9   50

 Compare data of two datasets
data5 = { 
    "EID" : [ "e1", "e2", "e3", "e4", "e5"],
    "Age" : [23,52,26,70,10]}
data8 = {
    "EID" : [ "e1", "e2", "e3", "e4", "e5"],
    "Age" : [ 18, 20, 29, 50, 49] }
d5 = pd.DataFrame(data5)
d8 = pd.DataFrame(data8)
print( d5, "\n", d8 )

# Output-> 
#      EID  Age
#    0  e1   23
#    1  e2   52
#    2  e3   26
#    3  e4   70
#    4  e5   10 
#       EID  Age
#    0  e1   18
#    1  e2   20
#    2  e3   29
#    3  e4   50
#    4  e5   49

print ( d5.compare(d8 ) )  # By defalut axis = 1
# Output-> 
#    Age      
#   self other
# 0   23    18
# 1   52    20
# 2   26    29
# 3   70    50
# 4   10    49

print ( d5.compare(d8 ,align_axis = 0 )) 
# When axis = 0, it will return initial value and final value both
# Output-> 
#          Age
# 0 self    23
#   other   18
# 1 self    52
#   other   20
# 2 self    26
#   other   29
# 3 self    70
#   other   50
# 4 self    10
#   other   49

print ( d5.compare(d8) ) # the row having same value in both dataset will not be shown
# Output->
#     Age      
#    self other
# 0  23.0  18.0
# 1  52.0  20.0
# 3  70.0  50.0
# 4  10.0  49.0


print ( d5.compare(d8, keep_shape = True) ) 
# keep_shape = True will give nan value at a position where values are same in both datasets
# Output->
   EID         Age      
  self other  self other
0  NaN   NaN  23.0  18.0
1  NaN   NaN  52.0  20.0
2  NaN   NaN   NaN   NaN
3  NaN   NaN  70.0  50.0
4  NaN   NaN  10.0  49.0

