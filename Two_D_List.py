arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [6, 7, 8, 9],
    ["Chetan"]
]
print(arr[2][0])    # accessing individual elements of array
print(*arr)
#   printing a list/array in matrix format
for i in arr:
    for j in i:
        print(j, end=" ")
    print("\n")
