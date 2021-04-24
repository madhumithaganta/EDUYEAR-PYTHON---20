n=int(input("enter the first number for the range:"))
m=int(input("enter the second number for the range:"))
for i in range(n,m,1):
      if i%5==0 and i%7==0:
          print(i,end=' ')



number_of_terms = 5
x = 1
num = 0
print("\n")
for i in range(number_of_terms):
    print('2'*x, end=' ')
    a = int('2'*x)
    x = x+1
    num = num + a
    print(num)


total = 0
while True:
    user_input=str(input('Enter the input(Take integer inputs) : '))
    if user_input!='q':
        total=total+int()
        print("Total : ",total)
        a = str(input('Enter to continue or q to quite: '))
        if a == 'q':
            break



number = int(input("Enter the number for the factorial : "))
factorial = 1
a = 1
while a <= number:
	factorial = factorial * a
	a = a + 1
print("Factorial :",factorial)        
    
