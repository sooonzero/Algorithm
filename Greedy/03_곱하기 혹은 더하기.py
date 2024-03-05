s = list(map(int, input()))
result = 0
for x in s:
    if x == 0:
        result += x
    else:
        if result == 0:
            result +=1
        result *= x

print(result)
