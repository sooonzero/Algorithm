n = int(input())
s = list(map(int, input().split()))

result = 0
s.sort()

print(s)


for i in range(len(s)):
    if s[i] <= n:
        result +=1
        i += s[i]
        n -= i
    else:
        break

print(result)
