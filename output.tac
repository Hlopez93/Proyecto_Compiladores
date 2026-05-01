nums = [1, 3, 5, 7, 9]
total = 0
i = 0
L1:
t1 = i < 5
if not t1 goto L2
t2 = nums[i]
t3 = t2 % 2
r = t3
t4 = r == 0
if t4 goto L3
goto L4
L3:
t5 = nums[i]
t6 = total + t5
total = t6
L4:
t7 = i + 1
i = t7
goto L1
L2:
begin_func fibonacci
param n
t8 = n <= 1
if t8 goto L5
goto L6
L5:
return n
L6:
t9 = n - 1
arg t9
t10 = call fibonacci, 1
t11 = n - 2
arg t11
t12 = call fibonacci, 1
t13 = t10 + t12
return t13
end_func fibonacci
print "Fibonacci(20) = "
arg 20
t14 = call fibonacci, 1
print t14
print "Total pares: "
print total