a = int(input())

if not 1 <= a <= 1000:
    print("input value is invalid")

if a%2 == 0:
    print("%d is even" % a)
else:
    print("%d is odd" % a)
