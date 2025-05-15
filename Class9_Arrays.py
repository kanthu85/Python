'''Arrays in Python are ordered collections of items that can store elements of the same data type. 
Unlike lists (which are more flexible), true arrays in Python are more memory-efficient and faster for numerical operations.'''
'''Python offers different ways to work with arrays:
    1.Python’s built-in array module
    2.NumPy arrays (the most commonly used)
    3.Lists (Python’s default sequence type)'''
#Method 1: Using Python’s Built-in Array Module(The array module provides an array object that is more compact than lists for storing basic numeric types.)
'''Common Array Type Codes
1.‘b’: signed char (integer between -128 to 127)
2.‘i’: signed int
3.‘f’: float
4.‘d’: double (float with higher precision)'''
import array as arr

# Creating an integer array
# 'i' represents signed integer
numbers = arr.array('i', [1, 2, 3, 4, 5])

print(numbers)  # Output: array('i', [1, 2, 3, 4, 5])
print(type(numbers))  # Output: <class 'array.array'>

# Create an array of integers
sales_figures = arr.array('i', [10500, 15200, 8700, 19300, 12600])

# Accessing elements
print(f"January sales: ${sales_figures[0]}")  # Output: January sales: $10500

# Updating values
sales_figures[1] = 16000
print(f"Updated February sales: ${sales_figures[1]}")  # Output: Updated February sales: $16000

# Adding elements
sales_figures.append(14800)
print(f"Added June sales: ${sales_figures[-1]}")  # Output: Added June sales: $14800

# Removing elements
removed_value = sales_figures.pop(2)
print(f"Removed March sales (${removed_value}) due to data error")

#Method 2: Using NumPy Arrays (Recommended)
#NumPy arrays are the most widely used arrays in Python, especially for data science and numerical computing.

#Setting Up NumPy
# Install NumPy if you haven't already

# pip install numpy
#Step-by-Step Instructions:
#Step1: Exit the Python Interpreter: If you are inside the Python interpreter, exit it by typing: > exit()
#Step2: Run the Command in Terminal: Open your terminal or command prompt and run: pip install numpy
#Alternative Method: Using Python -m
#If you encounter issues with pip, you can use the python -m prefix to ensure that pip is executed correctly.
#'C:\Users\10652749> python -m pip install numpy'

#Creating NumPy Arrays
import numpy as np
# 1D array
temperatures = np.array([68, 71, 73, 69, 75, 83, 79])
print(temperatures)  # Output: [68 71 73 69 75 83 79]

# 2D array (matrix)
monthly_sales = np.array([
    [5000, 6000, 7000],  # Q1 (Jan, Feb, Mar)
    [7500, 8200, 9000],  # Q2 (Apr, May, Jun)
    [9500, 9800, 10000], # Q3 (Jul, Aug, Sep)
    [12000, 15000, 13000] # Q4 (Oct, Nov, Dec)
])

print(monthly_sales)

#Creating Special NumPy Arrays
# Array of zeros
zero_array = np.zeros(5)
print(f"Zeros array: {zero_array}")

# Array of ones
ones_array = np.ones(5)
print(f"Ones array: {ones_array}")

# Range array
range_array = np.arange(0, 10, 2)  # Start, stop, step
print(f"Range array: {range_array}")  # Output: [0 2 4 6 8]

# Evenly spaced array
linspace_array = np.linspace(0, 1, 5)  # Start, stop, number of elements
print(f"Linspace array: {linspace_array}")  # Output: [0.   0.25 0.5  0.75 1. 

#NumPy Array Operations
import numpy as np

# Create arrays of US city temperatures (°F)
new_york = np.array([45, 48, 52, 58, 65])
los_angeles = np.array([68, 70, 72, 74, 76])

# Addition
temperature_sum = new_york + los_angeles
print(f"Sum of temperatures: {temperature_sum}")

# Multiplication (element-wise)
temperature_product = new_york * 2  # Double all temperatures
print(f"New York temperatures doubled: {temperature_product}")

# Statistical operations
print(f"Average NY temperature: {np.mean(new_york)}°F")
print(f"Maximum LA temperature: {np.max(los_angeles)}°F")
print(f"Minimum NY temperature: {np.min(new_york)}°F")
print(f"Standard deviation of NY temperatures: {np.std(new_york):.2f}°F")
#Array Reshaping and Slicing
# Creating a 1D array
quarterly_sales = np.array([55000, 68000, 72000, 98000, 62000, 75000, 83000, 91000])

# Reshaping to 2D (2 rows, 4 columns) - 2 years of quarterly data
sales_by_year = quarterly_sales.reshape(2, 4)
print("Sales by year (quarterly):")
print(sales_by_year)

# Slicing arrays
print("\nFirst year quarterly sales:")
print(sales_by_year[0])  # First row

print("\nQ2 sales for both years:")
print(sales_by_year[:, 1])  # Second column

#Method 3: Using Python Lists as Arrays
#While not true arrays, Python lists can serve as array-like structures for many purposes.

# Creating a list as an array
us_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Adding elements
us_cities.append("Philadelphia")

# Accessing elements
print(f"Third largest city: {us_cities[2]}")  # Output: Chicago

# Slicing
east_coast_cities = us_cities[0:2]
print(f"East coast cities: {east_coast_cities}")  # Output: ['New York', 'Los Angeles']
'''When to Use Each Type of Array
Use Python’s array module when:
1.You need a simple collection of numerical data of the same type
2.Memory efficiency is important
3.You don’t need complex mathematical operations
Use NumPy arrays when:
1.You need to perform mathematical operations on arrays
2.You’re working with large datasets
3.You need broadcasting and vectorized operations
4.You need multi-dimensional arrays
Use Python lists when:
1.You need a collection of mixed data types
2.You’re frequently adding/removing elements
3.You don’t need high-performance numerical operations'''
