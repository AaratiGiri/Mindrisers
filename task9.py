#Import the NumPy library and print its version.
import numpy as np
print(np.__version__)

#Create a NumPy array containing numbers from 1 to 10.
array1 = np.array([1, 2, 3, 4,5, 6, 7, 8, 9, 10])
print(array1)

#Create an array of all zeros with size 10 
zero = np.zeros(10)
print(zero)

#Create an array of all ones with shape (3,3).
ones = np.ones((3, 3))
print(ones)

#Create an identity matrix of size 5×5.

mi = np.identity(5)
print(mi)

#6	Create an array of even numbers from 2 to 50.
even = np.arange(2, 51, 2)
print("The even number from 2 to 50 is:", even)

#7	Create an array of odd numbers from 1 to 99.
odd = np.arange(1, 100, 2)
print("The odd number from 1 to 99 is:", odd)

#Generate numbers from 10 to 100 with step size 5.
step = np.arange(10, 101, 5)
print("The numbers from 10 to 100 with step size is:", step)

#9	Create a NumPy array from a Python list.
python_list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = np.array(python_list)
print("The numpy array from a python list is", array2)

#10	Create a NumPy array from a tuple.
python_tuple = (2, 1, 3, 4, 5, 6, 7, 8, 9, 10)
array3 = np.array(python_tuple)
print("The numpy array from a python tuple is", array3) 

#11	Find the shape of an array.....
array4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("The shape of the array is:", array4.shape)

#12	Find the dimensions of an array.
print("The dimensions of the array is:", array4.ndim)

#14	Create a random array of size 10.
random_array = np.random.rand(10)
print("The random array of size 10 is:", random_array)

#15	Generate 10 random integers between 1 and 100.
random_integers = np.random.randint(1, 101, size=10)
print("The 10 random integers between 1 and 100 are:", random_integers)

#16	Reshape an array of size 12 into (3,4).
array5 = np.arange(12)
reshaped_array = array5.reshape(3, 4)

print("The reshaped array of size 12 into (3,4) is:\n", reshaped_array)

# 17	Flatten a 3×3 matrix into a 1D array.

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_array = matrix.flatten()
print("The flattened array of the 3×3 matrix is:", flattened_array)

# 18	Create a 4×4 matrix filled with value 7.
matrix_4x4 = np.full((4, 4), 7)
print("The 4×4 matrix filled with value 7 is:\n", matrix_4x4)


# 19	Find the size (number of elements) of an array.
array6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("The size (number of elements) of the array is:", array6.size)

# 20	Create a diagonal matrix with diagonal values [1,2,3,4].
diagonal_matrix = np.diag([1, 2, 3, 4])
print("The diagonal matrix with diagonal values [1,2,3,4] is:\n", diagonal_matrix)
# 21	Convert a float array into an integer array.
float_array = np.array([1.5, 2.3, 3.7, 4.1])
integer_array = float_array.astype(int)
print("The integer array converted from float array is:", integer_array)
# 22	Create an array with values between 0 and 1 using linspace().
linspace_array = np.linspace(0, 1, num=10)
print("The array with values between 0 and 1 using linspace() is:", linspace_array)
# 23	Reverse an array.
array7 = np.array([1, 2, 3, 4, 5])
reversed_array = array7[::-1]
print("The reversed array is:", reversed_array)
# 24	Sort an array in ascending order.
unsorted_array = np.array([5, 2, 9, 1, 5, 6])
sorted_array = np.sort(unsorted_array)
print("The sorted array in ascending order is:", sorted_array)
# 25	Find the maximum and minimum values in an array.
array8 = np.array([1, 2, 3, 4, 5])
max_value = np.max(array8)
min_value = np.min(array8)
print("The maximum value in the array is:", max_value)
print("The minimum value in the array is:", min_value)

# 26	Find the index of maximum value.
array9 = np.array([1, 2, 3, 4, 5])
index_of_max = np.argmax(array9)
print("The index of maximum value in the array is:", index_of_max)
# 27	Find the index of minimum value.
index_of_min = np.argmin(array9)
print("The index of minimum value in the array is:", index_of_min)
# 28	Create a 2×3 matrix and print its transpose.
matrix_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
transpose_matrix = matrix_2x3.T
print("The 2×3 matrix is:\n", matrix_2x3)
print("The transpose of the 2×3 matrix is:\n", transpose_matrix)
# 29	Concatenate two arrays.
array10 = np.array([1, 2, 3])
array11 = np.array([4, 5, 6])   
concatenated_array = np.concatenate((array10, array11))
print("The concatenated array is:", concatenated_array)

# 30	Split an array into 3 equal parts.
array12 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
split_arrays = np.array_split(array12, 3)
print("The array split into 3 equal parts is:")
for i, split_array in enumerate(split_arrays):
    print(f"Part {i+1}:", split_array)
#     Add two arrays element-wise
array13 = np.array([1, 2, 3])
array14 = np.array([4, 5, 6])
added_array = array13 + array14
print("The element-wise addition of two arrays is:", added_array)

# Subtract two arrays element-wise.
subtracted_array = array13 - array14    
print("The element-wise subtraction of two arrays is:", subtracted_array)

# Multiply two arrays element-wise.
multiplied_array = array13 * array14
print("The element-wise multiplication of two arrays is:", multiplied_array)

# Divide two arrays element-wise.
divided_array = array13 / array14
print("The element-wise division of two arrays is:", divided_array)

# Find square of every element in an array.
squared_array = array13 ** 2
print("The square of every element in the array is:", squared_array)

# Find cube of every element.
cubed_array = array13 ** 3
print("The cube of every element in the array is:", cubed_array)

# Calculate square root of array values.
sqrt_array = np.sqrt(array13)
print("The square root of array values is:", sqrt_array)
# Find exponential values of array elements.
exp_array = np.exp(array13)
print("The exponential values of array elements is:", exp_array)

# Find logarithm of array elements.
log_array = np.log(array13)
print("The logarithm of array elements is:", log_array)
# Compute sum of all elements in an array.
sum_array = np.sum(array13)

print("The sum of all elements in the array is:", sum_array)

# Compute mean of array values.
mean_array = np.mean(array13)
print("The mean of array values is:", mean_array)

# Compute median of array values.
median_array = np.median(array13)
print("The median of array values is:", median_array)

# Compute standard deviation.
std_array = np.std(array13)
print("The standard deviation of array values is:", std_array)
# Compute variance.
var_array = np.var(array13)
print("The variance of array values is:", var_array)

# Find cumulative sum of elements.
cumsum_array = np.cumsum(array13)
print("The cumulative sum of elements in the array is:", cumsum_array)

# Find cumulative product of elements.
cumprod_array = np.cumprod(array13)
print("The cumulative product of elements in the array is:", cumprod_array)
# Find product of all elements in array.
product_array = np.prod(array13)
print("The product of all elements in the array is:", product_array)

# Round decimal values to 2 decimal places.
decimal_array = np.array([1.234567, 2.345678, 3.456789])
rounded_array = np.round(decimal_array, 2)
print("The decimal values rounded to 2 decimal places is:", rounded_array)


# Find absolute values of negative numbers.
negative_array = np.array([-1, -2, -3, -4, -5])
absolute_array = np.abs(negative_array)
print("The absolute values of negative numbers is:", absolute_array)

# Replace all negative values with zero.
replaced_array = np.where(negative_array < 0, 0, negative_array)
print("The array with negative values replaced by zero is:", replaced_array)
# 51	Access the first element of an array.
first_element = array13[0]
print("The first element of the array is:", first_element)

# 52	Access the last element of an array.
last_element = array13[-1]
print("The last element of the array is:", last_element)

# 53	Extract first 5 elements from an array.
array15 = np.arange(10)
first_five_elements = array15[:5]
print("The first 5 elements of the array are:", first_five_elements)

# 54	Extract last 5 elements from an array.
last_five_elements = array15[-5:]
print("The last 5 elements of the array are:", last_five_elements)

# 55	Slice every alternate element.
alternate_elements = array15[::2]
print("Every alternate element of the array is:", alternate_elements)







