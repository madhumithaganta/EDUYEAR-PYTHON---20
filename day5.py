x=[1,2,5,6,7,8,11,33,45,66,78,94]
count_even, count_odd = 0, 0
for num in x:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("count of even numbers available : ", count_even)
print("Count of odd number available : ", count_odd)



x.sort()
print("The minimum number is :", x[0])
print("The maximum number is :", x[-1])



x=[1,1,2,2,1,1,]
y=x[::-1]
if y==x:
    print("yes")
else:
    print("no")




num=[121,545,232]
rev_num=num[::-1]
if num==rev_num:
     print("it is a palindrome")
else:
     print("it is not a palindrome")
