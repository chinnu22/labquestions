def biggest(num1,num2,num3):
    if num1>num2 and num1>num3:
        max = num1
    elif num2>num3:
        max = num2
    else:
        max = num3
    return max


num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = int(input("Enter number3:"))
print(f"Biggest number is:{biggest(num1,num2,num3)}"")