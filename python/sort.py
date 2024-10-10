lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
lst.sort()
print(lst)  # [[-1, 3], [1, 2], [2, 3], [3, 4], [4, 2], [4, 5]]
lst.sort(reverse=True)
print(lst)  # [[4, 5], [4, 2], [3, 4], [2, 3], [1, 2], [-1, 3]]
# What if you want to sort by second element?
lst.sort(key=lambda x: x[1])
print(lst)  # where x is the parameter and x[1] is the second element
lst.sort(key=lambda x: x[1] + x[0])
print(lst)  # sorts by the sum of the elements inside the []
'''
# The lambda function is the same as saying
def sort_func(x):
    return x[0] + x[1]
lst.sort(key=sort_func)
print(lst) 
'''
# also works with sorted as in
'''
sorted(lst, key=)
'''