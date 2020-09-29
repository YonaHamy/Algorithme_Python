n=21
while n>0:
  j=-1
  while j<1 or j>3 or j>n:
    j=int(input("Combien?"))
  n=n-j
  if n==0:
    print("Perdu !")
  else:
    print("Il en reste ",n)
    if n%4==3:
      p=2
    elif n%4==2:
      p=1
    elif n%4==0:
      p=3
    else:
      p=1
    print("Le bot en prends  ",p)
    n=n-p
    print("Il en reste ",n)
    if n==0:
      print("Gagné")
            