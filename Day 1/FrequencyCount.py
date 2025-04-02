
li=[1,2,3,2,4,2,5,6,3]
count = {}
for v in li:
    if(not(v in count)):
        count[v] = 0
    count[v] += 1
print(count)