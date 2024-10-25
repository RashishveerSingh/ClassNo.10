# activity 2 finding prime numbers
lower = int(input("enter lowar range namber"))
upper =int(input("enter apper range namber"))
for num in range(lower, upper +1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
            else:
                print(num)