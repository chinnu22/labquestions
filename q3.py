tnum=num = int(input("Enter a number:"))
sum = 0
while num>9:
    sum = (num%10+num//10)
    num = sum
    
print(f"Sum of digits of:{tnum} is:{num}")