def is_magic_square(mat):
    return is_x(mat) and is_y(mat) and is_magic_row(mat) and is_magic_col(mat)

def is_magic_row(mat):
    is_true = []
    sum = 0
    for row in mat:
        for num in row:
            sum +=num
        is_true.append(sum)
    return not is_true[0] in is_true

def is_magic_col(mat):
    is_true = [[0] for row in range(len(mat))]
    sum = 0
    for row in range(len(mat)):
        for num in range(len(mat)):
            is_true[num] += mat[row][num]
    return not is_true[0] in is_true

def is_x(mat):
    is_true = [[0] for row in range(len(mat))]
    for row in range(len(mat)):
        is_true[row] += mat[row][row]
    return not is_true[0] in is_true

def is_y(mat):
    is_true = [[0] for row in range(len(mat))]
    for row in range(len(mat)):
        for num in range(len(mat)-1,-1,-1):
            is_true[num] += mat[row][num]
    return not is_true[0] in is_true


def ranksort(lst):
    if len(lst) == 2:
        if lst[0] <= lst[1]:
            return lst[0]
        else:
            return lst[1]

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x <= pivot]
    greater = [x for x in nums[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x <= pivot]
    more = [ x for x in nums[1:] if x > pivot]
    return quicksort(less) + pivot +quicksort(more)


def c1(func):
    def outer(arg1):
        def inner(*args):
            args = args + (arg1,)
            return func(*args)
        return inner
    return outer
final = c1(lambda x,y,z: x+y*z)
print(final(2)(3,4))

def win(lst1,lst2):
    lst1_win = 0
    lst2_win =0
    for i in lst1:
        for j  in lst2
            if i > j:
                lst1_win +=1
            else:
                lst2_win += 1
