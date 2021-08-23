import cProfile
from itertools import permutations

# uses in built python library to calculate permutations
my_list = [1, 2, 3, 4]

list_of_permutations = permutations(my_list)
cnt = 0
for permutation in list_of_permutations:
    cnt += 1
print(len(my_list), cnt)


# script for calculating permutations manually
def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n-1)*n


for i in range(10):
    print(faculty(i))


# used for cProfile to calculate runtime
def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


# calculates the runtime of functions
cProfile.run("counter(faculty(11))")


