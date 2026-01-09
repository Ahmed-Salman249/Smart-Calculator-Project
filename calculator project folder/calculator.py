# Calculator Project
# This program performs basic arithmetic operations with input validation
while True:
  # input first number
  while True:
    try:
     first_number = float(input("enter first number: "))
     break
    except ValueError:
     print("invalid input. please enter a numeric value")


  # input operation type
  while True:
   try:
     operation = input("enter operation type: ")
     if operation in ("+","-","/","*"):
        break
     else:
      raise ValueError
   except ValueError:
      print("invalid operation, please enter +,-,/,*")


  # input second number
  while True:
    try:
     second_number = float(input("enter second number: "))
     if second_number == 0 and operation == "/":
      raise ZeroDivisionError
     break
    except ZeroDivisionError:
       print("you can't divide on zero")
    except ValueError:
       print("invalid input. please enter a numeric value")


  # print the result
  if operation == "+":
     print("Result is" , first_number + second_number)
  elif operation == "-":
     print("Result is" , first_number - second_number)
  elif operation == "/":
     print("Result is" , first_number / second_number)
  elif operation == "*":
    print("Result is" , first_number * second_number)

  repeat = input("do you want to perform another operation (yes/no): ").lower()
  if repeat == "no":
   break
  elif repeat == "yes":
   continue
  else:
    while repeat not in ("yes","no"):
     repeat = input("please enter yes or no: ").lower()
    if repeat == "no":
     break
    elif repeat == "yes":
      continue
  break

print("program exited")
