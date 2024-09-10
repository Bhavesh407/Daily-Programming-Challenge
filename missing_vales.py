n = int(input())
a = []
for i in range(1,n):
  b = int(input())
  a.append(b)
print(a)

r = []
for j in range(1,n):
  if j not in a:
    r.append(j)
print(r)
