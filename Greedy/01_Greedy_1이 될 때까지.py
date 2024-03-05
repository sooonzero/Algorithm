n, k = map(int, input().split())
count = 0
a = 0

a += (n // k)
count = a

if a >= k:
    a -= k

count += a
print(count)

