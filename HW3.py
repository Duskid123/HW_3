import numpy
import numpy as np

def assignment_1():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    unique_a = np.unique(a)
    unique_b = np.unique(b)

    common_element = np.intersect1d(unique_a, unique_b)

    print(common_element)

def assignment_2():
    array = np.fromfunction(lambda i, j: i + 1 + j * 5, (5, 3), dtype=int)

    # print(array)
    return array

def assignment_3(array):
    flattened_array = array.flatten(order='F')
    # # print(flattened_array)
    # array = flattened_array
    return flattened_array

def assignment_4(array):
    array_3d = array.reshape((5, 3, 1))
    return array_3d

def assignment_5(array_3d):
    array_2d = array_3d.reshape((5,3))
    return array_2d

def assignment_6():
    a = np.array([12, 5, 7, 15, 3, 1, 8])
    b = np.array([14, 6, 3, 11, 19, 12, 5])

    print(a)
    a = np.delete(a, np.where(np.isin(a, b)))
    print(a)

def main():
    assignment_1()

    array = assignment_2()
    print(array)

    print(assignment_3(array))
    array = assignment_4(array)
    print(array)
    array = assignment_5(array)
    print(array)

    assignment_6()

if __name__ == '__main__':
    main()