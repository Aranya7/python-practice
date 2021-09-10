n=int(input("Enter a number:"))
tot=0
if n<0 or n>1000:
    n=int(input("Invalid Entry, Enter Again:"))
    
while(n>0 and n<1000):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)
