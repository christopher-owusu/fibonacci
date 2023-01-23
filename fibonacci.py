# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# x = input("enter a number: ")
# y = input("enter a second number: ")

def fib(n):
    x = 0
    y = 1

    for i in range (2, n):
        print(x+y)
        x, y = y, x + y

fib(7)

print("Done")
