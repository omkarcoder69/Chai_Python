# basic calculator using python

# added modules , addition , subtraction , multiple , division , flor (//) division , 



operations = input("Enter Your choice (+,-,*,/):")
n1 = float(input("Enter number 1:"))
n2 = float(input("Enter number 2:"))
match operations:
        case "+":
            print("Addition",n1+n2)
        case "-":
            print("subtraction",n1-n2)
        case "*":
            print("Mutliplication",n1*n2)
        case "/":
            if n2!=0:
                print("Divide",n1/n2)
            else:
                print("divided by zero")
        case "%":
            print("module",n1%n2)
        case "//":
            print("module",n1//n2)
        case _:
            print("Enter proper choice")
   

    
