# break operatori eng ichkaridagi for yoki while tsiklini darhol to‘xtatadi (ya’ni, undan chiqib ketadi).

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break



for num in range(2, 10):
    if num % 2 == 0:
        print(f"found an even number {num}")
        continue
    print(f"Found an odd number{num}")




for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')