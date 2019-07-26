lb = int(input("Enter the lower bound:"))
ub = int(input("Enter the upper bound:"))
res = " ".join([str(i) for i in range(lb,ub+1) if i%9 == 0 and i%5!=0])
print(res)