#                   NUMPY   ( Numerical Python )

# This repo includes code related to Numpy library

import numpy as np

# np.array() this function will create an array(space separated) of list( comma separated

arr = np.array([3,5,4,7,8])
print(arr)
# Output->       [3 5 4 7 8]

print(type(arr))
# Output ->      <class 'numpy.ndarray'>

# for multiple dimendion array like matrices

arr2 = np.array( [ [ 22,33,44,55 ] , [ 66, 77, 88, 99 ] , [ 32, 43, 54,65 ] ] )
print(arr2)
# Output-> [[22 33 44 55]
#           [66 77 88 99]
#           [32 43 54 65]]

# for multiple dimension array all the lists have same No of values( because in matrices every row have same No of columns )
# in the main list otherwise will throw an error .We can extend the dimensions of array by adding comma and then by adding list 
# having same No of values as others

# Slicing in Numpy
   
# Slicing in One dimensional array

arr3 = np.array( [ 2,4,6,8,7,5,3,1 ] )
print ( arr3[ 0: 4 ] ) 
# Output->        [2 4 6 8]

print( arr3 [ : 4 ] )
# Output->       [2 4 6 8]
print ( arr3 [ 0 : ] )
# Output->       [2 4 6 8 7 5 3 1]

print ( arr3 [ -1 : ] )
# Output->       [1]

print ( arr3 [ -4 : -1 ])
# Output->       [7 5 3]

print ( arr3 [-4 : ] )
# Output->       [7 5 3 1]
print ( arr3 [ : -1 ] )
# Output->       [2 4 6 8 7 5 3]

# Slicing in Multi Dimensional array

arr4 = np.array( [ [ 1,3,5,7,9] , [ 0,2,4,6,8 ] ] )
print( arr4 [ 0:2 , 0:3 ] ) 
# Output-> [[1 3 5]
#          [0 2 4]]

# Wanna access a single element form multidimensional array

print ( arr4 [ 0, 1:3 ] )
# Output->    [3 5]

print ( arr4 [ 0 ] )
# Output->   [1 3 5 7 9]

print ( arr4 [ 1, 1:3 ] )
# Output->    [2 4]

print (arr4 [ 1,1 ] )
# Output->    2

# for checking No of elements in an array
arr5 = np.array( [2,3,4] )
print(arr5.size)
# Output-> 3

arr6 = np.array ( [ [ 2,3,4] , [5,6,7] ] )
print(arr6.size)
# Output-> 6

# To check No of nested elements 
arr5 = np.array( [2,3,4] )
print(len(arr5))
# Output-> 3

arr6 = np.array ( [ [ 2,3,4] , [5,6,7] ] )
print(len(arr6))
# Output->      2

# To check type of array
print( type(arr5))
# Output->    <class 'numpy.ndarray'>

# To check type of datatype used in array
print ( arr5.dtype)
# Output->    int64

# To change datatype in array
# But string datatype can not be converted into int or float 
print( arr5.astype(float))
# Output->    [2.0 3.0 4.0]
print( arr5.astype(str))
# Output->    ['2' '3' '4']

# To check No of columns and rows .shape() function will be used
print( arr6.shape)
# Output->    (2, 3)

# Mathematical Operations and Functions on array

# Addition for one dimensional array
arr7 = np.array( [ 1,2,3,4,5] )
arr8 = np.array ( [ 6,7,8,9,5] )
print( arr7 + arr8 )
# Output-> 
#               [ 7  9 11 13 10]
print( np.add(arr7, arr8 ) )
# Output-> 
#               [ 7  9 11 13 10]

# Addition for multi dimensional array

#Subtraction
arr7 = np.array( [ 1,2,3,4,5] )
arr8 = np.array ( [ 6,7,8,9,5] )
print( arr8 - arr7 )
# Output->       
#                [5 5 5 5 0]
print ( np.subtract(arr8, arr7))
# Output->       [5 5 5 5 0]

# Multiply
arr7 = np.array( [ 1,2,3,4,5] )
arr8 = np.array ( [ 2,2,2,2,2] )
print( arr8 * arr7 )
# Output->       
#         [ 2  4  6  8 10]
print ( np.multiply(arr8, arr7))
# Output->       
#         [ 2  4  6  8 10]

# Divide
arr7 = np.array( [ 1,2,3,4,5] )
arr8 = np.array ( [ 2,2,2,2,2] )
print( arr8 / arr7 )
# Output->     
#         [2.         1.         0.66666667 0.5        0.4       ]
print ( np.divide(arr8, arr7))
# Output->     
#         [2.         1.         0.66666667 0.5        0.4       ]

# Power
arr9 = np.array([2])
arr7 = np.array( [ 1,2,3,4,5] ) 
print( np.power( arr7, arr9 ) )
# Output->     
#         [ 1  4  9 16 25]

# SQRT
arr7 = np.array( [ 1,2,3,4,5] ) 
print( np.sqrt( arr7 ) )
# Output->    
#         [1.         1.41421356 1.73205081 2.         2.23606798]

# Combining and Spliting Arrays

# Concatenation without using numpy library
first = [ 2 , 3, 4, 5]
second = [ 6, 7, 8, 9]
print( first +  second)
# Output->     
#           [2, 3, 4, 5, 6, 7, 8, 9]

# Concatenation  using numpy library

# Concatenation in one dimension using numpy library
arr7 = np.array( [ 1,2,3,4,5] )
arr8 = np.array ( [ 2,2,2,2,2] )
print( np.concatenate( [arr7, arr8] ))
# Output->     
#            [1 2 3 4 5 2 2 2 2 2]

# Concatenation in two dimension using numpy library

# Horizontal Concatenation when axis = 1
arr7 = np.array([ [ 1,2,9], [3,4,5] ] )
arr8 = np.array ( [ [ 2,3,4], [1,0,2] ] )
print( np.concatenate( [arr7, arr8], axis = 1 ))
# Output->     
#              [[1 2 9 2 3 4]
#              [3 4 5 1 0 2]]

# Horizontal Concatenation using hstack
print(np.hstack ( [arr7, arr8 ]))
# Output->     
#              [[1 2 9 2 3 4]
#              [3 4 5 1 0 2]]

# Vertical Concatenation when axis = 0
print( np.concatenate( [arr7, arr8], axis = 0 ))
# Output->      
#               [[1 2 9]
#               [3 4 5]
#               [2 3 4]
#               [1 0 2]]

# Vertical Concatenation using vstack
print(np.vstack ( [arr7, arr8 ]))
# Output->       [[1 2 9]
#                 [3 4 5]
                 [2 3 4]
                 [1 0 2]]


# Spliting array

# np.array_split ( array_name, No of parts in which array will be splited )
arr_2 = np.array( [ 1,2,3,4,5,6,7,8,9 ] )
print ( np.array_split ( arr_2, 3) )
# Output->       [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
arr_3 = np.array_split(arr_2 , 1 )
print ( arr_3)
# Output->       [array([1, 2, 3, 4, 5, 6, 7, 8, 9])]


# Adding and removing Elements in Arrays

# np.append(a,b) This function will add item at the end of the array
arr_2 = np.array( [ 1,2,3,4,5,6,7,8,9 ])
print(np.append(arr_2,10))
# Output->       [ 1  2  3  4  5  6  7  8  9 10]

# np.insert(a,1,5) This function will add an  item at a specific index like in brackets first we will give name of the array then index and then the value to be add
arr_4 = np.array( [ 1,2,3,4])
print(np.insert(arr_4,1,10))
# Output->       [ 1 10  2  3  4]

# np.delete(a,[1])
arr_4 = np.array( [ 1,2,3,4])
print(np.delete(arr_4, 1 ) )
# Output->       [1 3 4]

# Search , Sort and Filter in Arrays

# Sort
arr_5 = np.array( [ 9,3,8,2,1 ] )
print( np.sort( arr_5 ))
# Output->       [1 2 3 8 9] 
arr_6 = np.array ( [ [ 2,1,8,4,0], [ 7,2,5,3,9 ] ] )
print( np.sort( arr_6 ) )
# Output->       [[0 1 2 4 8]
                 [2 3 5 7 9]]

# Search
arr_5 = np.array( [ 9,3,8,2,1 ] )
a = np.where ( arr_5 == 8 )
print(a)
# Output->       (array([2]),)     # will return index number
# Program which will return indices of only those numbers which are divisible by 2
arr_5 = np.array( [ 9,3,8,2,1 ] )
b = np.where ( arr_5 % 2 == 0 )
print(b)
# Output->       (array([2, 3]),)

# np.searchsorted() function, for this array must be sorted first
arr_6 = np.array ( [ 1,2,3,4,5 ] )
print(np.searchsorted (arr_6, 2) )
# Output ->        1

# Filter

b = np.array( [ 20,30, 40, 50 ] )
c = [ True, False, True, False ]
d = b[c]
print( d )
# Output->        [20 40]

b = np.array( [ 20,30, 40, 50 ] )
e = b > 35
f = b [ e ]
print(f)
# Output->        [40 50]

b = np.array( [ 20,30, 40, 50 ] )
g = b % 2 == 0
h = b[g]
print(h)
# Output->        [20 30 40 50]

# Statistical Functions in array

b = np.array( [ 20,30, 40, 50 ] )
print( np.sum ( b) )
# Output->        140

print( np.cumsum (b) )
# Output->        [ 20  50  90 140]

print( np.cumprod (b) )
# Output->        [     20     600   24000 1200000]

print( np.max (b) )
# Output->        50

print( np.min (b) )
# Output->        20

print( np.size (b) )
# Output->        4

print( np.mean (b) )
# Output->        35.0

b = np.array( [ 20,30, 40, 50 ] )
c_ = np.array( [ 2,3,4,5] )
print( b , "\n", c_ ) # adding new line
# Output->        [20 30 40 50] 
                  [2 3 4 5]

print( b , "\n", c_ )
print () # for adding single line
d_ =  np.cumprod ( [ b, c_ ] , axis =0 ) # axis is provided bcz we have two columns/values
print( d_ )
# Output->        [20 30 40 50] 
                  [2 3 4 5]

                  [[ 20  30  40  50]
                  [ 40  90 160 250]]
print ( d_[ 1 ].sum() )
# Output->        540

# Median is central value after sorting

_b = np.array( [ 25,37, 44, 59 ] )
print( np.mean ( _b ) ) # Sum of all the values / divided by total No of values
print( np.median ( _b ) )  # first sort the given data and then average of middle values
# for median if total No of values are odd then after sorting center value will be median
# for median if total No of values are even then after sorting take average of center two values
# Output->        41.25
# Output->        40.5

# There is no function in Numpy library for finding mode

# Statistics Library
# For finding mode there is function in statistics library

import statistics as stats
_c = np.array( [ 25,37, 59, 44, 59 ] )
print ( stats.mode ( _c ) )
# Output->        59

# Standard Diviation
_c = np.array( [ 25,37, 59, 44, 59 ] )
print ( np.std (_c ) )
# Output->       13.090454537562858

# Variance
print( np.var ( _c ) )171.36z
# Output->       171.36

# To verify var and std function 
print ( 13.09**2 )
# Output->       171.3481

# Cofficient of Corelation
# -1 represents inversely proportional relationship
# +1 represents directly proportional relationship
# zero represents no relation i-e both quantities are independent of each other
x = [ 100, 200, 300, 400, 500, 600 ]
y = [ 9, 7, 5, 3, 2, 1]
z = [ 2 , 4, 6, 7, 8, 9 ]
print ( np.corrcoef( [ x,y ] ) )
# Output->       [[ 1.         -0.98850537]
                 [-0.98850537  1.        ]]
print()
# Output->    

print ( np.corrcoef ( [ x , z ] ) )
# Output->       [[1.         0.98390407]
                 [0.98390407 1.        ]]
