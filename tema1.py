a= [7 ,8 ,9 , 2, 3, 1, 4, 10, 5, 6]
print (a)
a.sort()
print('sorted list:', a)
a.sort(reverse=True)
print('sorted list (descending:', a)
sliced_a = a[: : 2]
print(sliced_a)
sliced_a = a[ 1 : : 2]
print(sliced_a)
sliced_a = a[ 1: 10: 3  ]
print(sliced_a)