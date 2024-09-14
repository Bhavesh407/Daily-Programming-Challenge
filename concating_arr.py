a = [1,3,5,7]
b = [2,4,6,8]
s=[]
n = len(a)+len(b)
for i in range(n):
  if i < len(a):
    s.append(a[i])
  else:
    s.append(b[i-len(a)])
print(s)
s = sorted(s)

m = s[:4]
n = s[4:]
print(m)
print(n)
