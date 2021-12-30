#8min
s="LVIII"
def romanToNumber(s):
  sums=0
  for i in s:
    if i=="I":
      sums+=1
    elif i=="V":
      sums+=5
    elif i=="X":
      sums+=10
    elif i=="L":
      sums+=50
    elif i=="C":
      sums+=100
    elif i=="D":
      sums+=500
    elif i=="M":
      sums+=1000 
  print(sums)
  
romanToNumber(s)
