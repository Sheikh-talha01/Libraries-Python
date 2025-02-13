import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.quiver( 0,0, 4,5 )

plt.quiver( 0,0, 4,5, scale_units='xy', angles='xy', scale=1 )
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()

# Showing 2 vectors in same graph
plt.quiver( 0,0, 5,6, scale_units='xy', angles= 'xy', scale = 1, color = 'b')
plt.quiver( 0,0,-2,-4, scale_units='xy', angles= 'xy', scale = 1, color = 'r')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()

# Addition of vectors
vec1 = np.asarray([0,0, 2,3])
vec2 = np.asarray([0,0, 5,6])
vec_sum = vec1 + vec2
print(vec_sum)

plt.quiver( 0,0, 2,3, scale_units='xy', scale=1, color= 'r')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()

plt.quiver( 0,0, 2,3, scale_units='xy', angles = 'xy', scale=1, color= 'r')
plt.quiver( 0,0, 5,-2, scale_units='xy', angles = 'xy', scale=1, color= 'b')
plt.quiver( 0,0, 7,1, scale_units='xy', angles = 'xy', scale=1, color= 'g')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()
plt.quiver( 0,0, 2,3, scale_units='xy', angles = 'xy', scale=1, color= 'r')
plt.quiver( 0,0, 5,-2, scale_units='xy', angles = 'xy', scale=1, color= 'b')
plt.quiver( 0,0, 3,-5, scale_units='xy', angles = 'xy', scale=1, color= 'g')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()

# Subtraction of vectors
vec3 = np.asarray([0,0, 2,3])
vec4 = np.asarray([0,0, 5,-2])
vec_sub = vec2 - vec1
print(vec_sub)
lt.quiver(0,0, 2,3, scale_units = 'xy', angles = 'xy', scale = 1, color = 'r')
plt.quiver(0,0, 5,-2, scale_units = 'xy', angles = 'xy', scale = 1, color = 'g')
plt.quiver(0,0, 3,-5, scale_units = 'xy', angles = 'xy', scale = 1, color = 'b')
plt.xlim(-9,9)
plt.ylim(-9,9)
plt.show()


# Multiplication of Vectors

# Cross Product of 3 values
vec3 = np.asarray([2,3])
vec4 = np.asarray([5,-2])
result = np.cross(vec3, vec4)
print( result)

# Cross Product of 3 values
vec7 = np.asarray([2,4,3])
vec8 = np.asarray([6,0,-2])
_result = np.cross(vec7, vec8)
print( _result)

# Dot Product
vec5 = np.asarray([4,3])
vec6 = np.asarray([6,-2])
result_ = np.dot(vec3, vec4)
print( result_)

# Projection of 'a' vector on 'v' vector
a = np.array([2,5])
v = np.array([8,-6])

# Magnitude of v
magnitude_of_v = np.sqrt(sum(v**2) )
# Projection of 'a' on 'v'
ans = ( ( np.dot(a,v) ) / ( magnitude_of_v**2 ) ) * v
print("Projection of 'a' on 'v' is ",ans )

# Scaler Vs Vector Vs Matrics
# Scaler-> a single number
# Vector-> Lists of numbers( only one row or only one column )
# Metrix-> Multiple rows and columns ( More than one row and column )

# Creating Matrix in Python
metrix = np.array( [ [1,2,3] ,[4,5,6] ] )
print( metrix )
metrix1 = np.array( [ [1,2], [3,4]])
print('\n', metrix1)

# Creating Matrix with Random Values( floating Point Numbers)
metrix2 = np.random.rand(2,3)
print( metrix2 )

# Creating Matrix with Random Values( Integers)
metrix3 = np.random.randint(50, size = (2,3)) # first argument( 50) is for limit i-e we want numbers less than 50
print( '\n',metrix3 )

# Metrix with all the values equal to 1 ( having datatype float)
metrix4 = np.ones((2,3) )
print( metrix4 )

# Metrix with all the values equal to 1 ( having datatype int)
metrix4 = np.ones((2,3), dtype = int )
print( metrix4 )

# Null metrix or zero metrix
metrix5 = np.zeros( (3,4) )
print( metrix5)

# Identity Metrix
metrix6 = np.eye(3,3)
print( metrix6 )

# Metrix Addition and subtraction
# Two metrices can be added/subtracted only if they have same shape i-e they have same number of rows and columns

# Addition of Metrics
metrix = np.array( [ [1,2,3] ,[4,5,6] ] )
print( metrix )
metrix_ = np.array( [ [1,2,4], [3,5,4]])
print('\n', metrix_)

# Addition of Metrics ( random numbers)
metrix3 = np.random.randint(50, size = (2,3)) 
metrix_3 = np.random.randint( 50, size = (2,3))
metrix_sum_ = np.add( metrix3, metrix_3)
print( metrix3, '\n\n', metrix_3, '\n\n', metrix_sum_ )

metrix_sum = metrix + metrix_
print('\n', metrix_sum)

# Subtarction of Metrics ( random numbers)
metrix_4 = np.random.randint(50, size = (2,3)) 
metrix4_ = np.random.randint( 50, size = (2,3))
metrix_sub_ = np.subtract( metrix_4, metrix4_)
print( metrix_4, '\n\n', metrix4_, '\n\n', metrix_sub_ )


# Multiplication of two metrics

# General Multiplication of metrics
# Condition-> No of columns in first metrix should be equal to No of rows in the second metrix
metrix_5 = np.random.randint( 4, size = (2,3))
metrix5_ = np.random.randint(4, size = (3,2)) 
metrics_multiply = np.dot(metrix_5,metrix5_)
print(metrix_5, '\n\n',metrix5_, '\n\n', metrics_multiply)

# Elementwise Multiplication 
# Multiplication of elements of one matrix to corresponding elements of another matrix
metrix6_ = np.random.randint( 4, size = (3,3))
metrix_6 = np.random.randint(4, size = (3,3)) 
elementwise_multiply = np.multiply(metrix6_,metrix_6)
print(metrix6_, '\n\n',metrix_6, '\n\n', elementwise_multiply)

