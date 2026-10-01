# NUMPY - PYTHON PROGRAMS


import numpy as np



# Problem 1


arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)


# Problem 2

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# Problem 3

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# Problem 4

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)


# Problem 5

arr = np.arange(1, 13)

print("2 x 6 matrix:")
print(arr.reshape(2, 6))

print("3 x 4 matrix:")
print(arr.reshape(3, 4))

print("4 x 3 matrix:")
print(arr.reshape(4, 3))


# Problem 6

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix Addition:")
print(a + b)


# Problem 7

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

result = np.matmul(a, b)

print("Matrix Multiplication:")
print(result)


# Problem 8

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("Original matrix:")
print(matrix)

print("Transpose:")
print(matrix.T)


# Problem 9


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("First row:", matrix[0])
print("Last column:", matrix[:, -1])
print("Diagonal:", np.diag(matrix))
print("Second and third rows:")
print(matrix[1:3])


# Problem 10

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("Sum of each row:", np.sum(matrix, axis=1))
print("Sum of each column:", np.sum(matrix, axis=0))


# Problem 11

arr = np.arange(1, 21)

print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])


# Problem 12

arr = np.array([20, 65, 45, 80, 30, 55, 90, 25, 70, 40])

arr[arr > 50] = 0

print("Updated array:", arr)


# Problem 13

arr = np.array([50, 20, 80, 10, 40, 90, 30])

print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])


# Problem 14

arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40])

print("Unique elements:", np.unique(arr))


# Problem 15


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))


# Problem 16

marks = np.array([78, 85, 67, 92, 74, 88, 95, 81, 69, 90])

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))


# Problem 17

marks = np.array([
    78, 65, 89, 45, 92,
    71, 84, 55, 96, 68,
    73, 88, 61, 79, 90,
    52, 85, 76, 94, 70
])

average = np.mean(marks)

print("Class average:", average)
print("Marks above average:", marks[marks > average])


# Problem 18

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)
print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# Problem 19

arr = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])



# Problem 20

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows:", np.sum(arr, axis=2))
print("Sum along columns:", np.sum(arr, axis=1))


# Problem 21

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original array:")
print(arr)

arr[arr > 50] = 0

print("After replacing values greater than 50:")
print(arr)


# Problem 22

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# Problem 23

arr = np.arange(1, 25).reshape(2, 3, 4)
flat = arr.flatten()

print("Original 3D array:")
print(arr)

print("Flattened array:")
print(flat)


# Problem 24


arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()

print("Flattened array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# Problem 25

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)

print("Original 3D array:")
print(arr)

print("Elements greater than 50:", flat[flat > 50])
print("Even numbers:", flat[flat % 2 == 0])
print("Elements less than average:", flat[flat < average])
