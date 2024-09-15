n = int(input())
a = []
ni = []

for i in range(n):
  c = int(input())
  a.append(c)

for i in range(n):
  l = True
  for j in range(i+1,n):
    if a[i] < a[j]:
      l = False
      break
  if l:
    ni.append(a[i])

print(ni)
