print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
try:
    print("Enter first value:")
    num1 = float(input())
    val = float(num1)
except ValueError:
   print("Please enter a number")
   exit();
try:
    print("Enter second value:")
    num2= float(input())
    val = float(num2)
    print("Processing..!!")   
except ValueError:
    print("Please enter a number") 
    exit();
choice = float(input("Enter your choice: "));
if(choice==1 or choice==2 or choice==3 or choice==4):
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    elif choice == 4:
        if(num2==0):
            print("Error: Division by zero!!!!!!");
        else:
            res = num1 / num2;
            print("Result = ", res);
else:
    print("Wrong input..!!");
