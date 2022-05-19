number = int(input())
copy = number
digit_sum = 0
while number:
    digit_sum += number%10
    number //= 10
if copy%digit_sum == 0:
    print(True)
else:
    print(False)