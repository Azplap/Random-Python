def factorial(n):
    if(n<=1):
        return n
    else:
        return n*factorial(n-1)




if __name__ == '__main__':
    input = input()

    print(factorial(int(input)))