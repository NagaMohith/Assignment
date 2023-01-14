def fun(a):
  r=[]
  for i in a:
    if i%2!=0:
      #print(i)
      r.append(i)
  r.sort()
  r.reverse()
  print(r)

fun([5,3,11,9,10,12,14,7])