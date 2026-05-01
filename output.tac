nums = [3, 1, 4, 1, 5]
total = 0
i = 0
L1:
t1 = i < 5
if t1 goto L2
goto L3
L2:
t2 = nums[i]
t3 = t2 % 2
r = t3
t4 = r == 0
if t4 goto L4
goto L5
L4:
t5 = nums[i]
t6 = total + t5
total = t6
L5:
t7 = i + 1
i = t7
t8 = total > 10
if t8 goto L6
goto L7
L6:
goto L3
L7:
goto L1
L3:
begin_func fibonacci
param n
t9 = n <= 1
if t9 goto L8
goto L9
L8:
return n
L9:
t10 = n - 1
param t10
t11 = call fibonacci, 1
t12 = n - 2
param t12
t13 = call fibonacci, 1
t14 = t11 + t13
return t14
end_func fibonacci
msg = "Fibonacci(15) = "
print msg
param 15
t15 = call fibonacci, 1
print t15
print "Total pares: "
print total