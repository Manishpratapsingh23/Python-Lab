# question 1 CountDown Timer
import time
n = int(input('Enter the number '))
print('Counter start ')
while n:
    print(n)
    n -= 1
    time.sleep(1)
else:
    print('Counter Stop')
