import numpy as np

arr = np.genfromtxt('array.txt', dtype=np.int32, delimiter=',')
cube = np.reshape(arr, [50, 50, 50], order='C') # Example: array[0, 1, 0] = sheet 0, row 1, column 0

# 1
max_sum = 0
max_index = None
for x in range(cube.shape[0] - 2):
    for y in range(cube.shape[1] - 2):
        for z in range(cube.shape[2] - 2):  # x, y, z loops create 3x3x3 array
            # print(cube[x:x+3, y:y+3, z:z+3])
            # np.sum(cube[x:x+3, y:y+3, z:z+3])  # These were lines to test my 3d array
            s = np.sum(cube[x:x + 3, y:y + 3, z:z + 3])  # This sums the 3d array each time it moves one cube in any direction
            if s > max_sum:
                max_index = (x, y, z)
                max_sum = s
print('Max sum:', max_sum, ', Index of max sum cube:', max_index)

# 2
sub_cube = {}
for x in range(cube.shape[0] - 9):
    for y in range(cube.shape[1] - 9):
        for z in range(cube.shape[2] - 9):
            s = np.sum(cube[x:x + 10, y:y + 10, z:z + 10])  # Above code essentially recycled
            if s in sub_cube:  # Increases the value in the key value pair for any duplicate sums
                sub_cube[s] += 1
            else:
                sub_cube[s] = 1
print(sub_cube)

# 3
s = np.sum(cube, axis=2)  # NumPy method which makes this much simpler than traditional code would have
print(s)
