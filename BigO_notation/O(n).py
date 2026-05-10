def add_five(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 5
    return nums

minha_lista = [1,2,3]
resultado = add_five(minha_lista)
print(resultado)