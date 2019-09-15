# 
#  Fib Casestudy Example
#
import matplotlib.pyplot as plt

from_n, to_n = 1, 30

X = range(from_n, to_n)
#print(X)
# our old fib function
def fibslow(n):
    if n == 0 or n == 1 :
        return n

    else:
        return fibslow(n-1) + fibslow(n-2)

def fibfast(n):
    if n <= 1: return n

    a, b = 0, 1

    for i in range(1, n+1):
        a, b = b, a + b

    return a
# 
#  Time Calculate function
#
def time_function(fn, start, end):
    from datetime import datetime

    times = []
    for i in range(start, end):
        start_time = datetime.now()

        _ = fn(i)  # actual call to the function, don't care about value

        end_time = datetime.now()
        time_taken = end_time - start_time   # returns a timedelta
        time_taken = time_taken.microseconds

        times.append(time_taken)

    return times

#
#  Fib slow time
#
fibslow_times = time_function(fibslow, from_n, to_n)
fibfast_times = time_function(fibfast, from_n, to_n)

print(fibslow_times)
print(fibfast_times)

#
#  Ploting fibSlow and fibFast time graph
#
plt.figure()
plt.plot(X, fibslow_times, label='fibslow')
plt.plot(X, fibfast_times, label='fibfast')
plt.xlabel('n')
plt.ylabel('time (microseconds)')
plt.legend()
