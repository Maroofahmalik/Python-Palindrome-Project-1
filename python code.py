n = int(input("Enter the number: "))
if n > 1:
    flag = 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            break
    if flag == 1:
        print(n,"is not a prime number")
        x = n
        sum = 0
        while x > 0:
            r = x % 10
            sum = sum * 10 + r
            x = x // 10
            if sum==n:
                print(n,"is not a prime number but is a Palindrome")
                print(n,"is not a prime Palindrome")
    else:
        x = n
        sum = 0
        while x > 0:
            r = x % 10
            sum = sum * 10 + r
            x = x // 10
        if sum == n:
            print(n, "is a prime Palindrome")
        else:
            print(n, "is not a prime Palindrome")
