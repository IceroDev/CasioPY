import math
A=float(input("a="))
B=float(input("b="))
C=float(input("c="))
DELTA=B**2-4*A*C
rac=math.sqrt(B**2-4*A*C)
X1=(-B+rac)/2*A
X2=(-B-rac)/2*A
X3=-B/(2*A) 
print("DELTA :",DELTA)
if(DELTA==0):
  print("Pas de solution")
elif(DELTA>0):
  print("X1=",X1)
  print("X2=",X2)
elif(DELTA<0):
  print("X1=",X3) 