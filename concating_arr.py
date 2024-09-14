n = int(input())
a = []
b = []
s=[]

for i in range(n):
  c = int(input())
  a.append(c)

for i in  range(n):
  d = int(input())
  b.append(d)

print(a)
print(b)

n = len(a)+len(b)
for i in range(n):
  if i < len(a):
    s.append(a[i])
  else:
    s.append(b[i-len(a)])

s = sorted(s)

m = s[:4]
n = s[4:]
print(m)
print(n)
