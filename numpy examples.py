# -*- coding: utf-8 -*-

import numpy

# Generate random matrix
randmatrix =  numpy.random.randint(low = 1, high = 100, size = (5,5))

print(randmatrix)
print()


# mean of column vectors
print(numpy.mean(randmatrix, axis=0))

print()

# mean of row vectors
print(numpy.mean(randmatrix, axis=1))

print()

# calculate inverse matrix
invmatrix = numpy.round(numpy.linalg.inv(randmatrix), decimals=2)
print(invmatrix)



print("\n"+"Generate Singular Matrix: ")

# Generate a singular matrix
N = numpy.random.randint(low = 1, high = 100, size = (1,5))
S = numpy.transpose(N)*N

print(S)
det = numpy.linalg.det(S)

print("determinant: "+ str(det))
print()





   