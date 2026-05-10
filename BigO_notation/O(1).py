def add_five(nums):
    nums.append(5)
    return nums

minha_lista=[1,2,3,4]
resultado= add_five(minha_lista)
print(resultado)


 # O(n²)


# def print_nums(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             print((nums[i], nums[j]))


# print_nums([1,2,3,4])            