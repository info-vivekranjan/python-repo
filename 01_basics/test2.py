import test
import random
import copy

print(test.add(99,55))

print("Random ==", random.random())

h1 = [1,2,3]
h2 = h1

h2[0] = 55

print(h1)

###############

k1 = [4,5,6]

k2 = copy.deepcopy(k1)
k2[0] = 66

k3 = copy.copy(k1)
k3[0] = 88

k4 = k1[:]
k4[0]=99

print(k1, k2, k3, k4)

############################
n1 = [5, 8 , 9]

print(n1[0:2])

#################