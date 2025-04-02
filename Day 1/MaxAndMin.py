r = 3
c = 3
li = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
max_element = li[0][0]
min_element = li[0][0]

for i in range(r):
    for j in range(c):
        if li[i][j] > max_element:
            max_element = li[i][j]
        if li[i][j] < min_element:
            min_element = li[i][j]

print("Maximum element in matrix:" ,max_element)
print("Minimum element in matrix:" ,min_element)
