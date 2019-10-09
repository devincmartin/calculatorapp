print("Please insert your first number")

first_number_string = input(">> ")
first_number = int(first_number_string)

print("Please insert your second number")

second_number_string = input(">> ")
second_number = int(second_number_string)

print("Your numbers are", first_number, "and", second_number)

print("Select your operator: ADD, MULTIPLY or SUBTRACT")
operator_string = input(">> ")

if(operator_string == "ADD"):
    print("Your result is ", first_number + second_number)
elif(operator_string == "SUBTRACT"):
    print("Your result is ", first_number - second_number)
elif(operator_string == "MULTIPLY"):
    print("Your result is ", first_number * second_number)
    
else:
    print("Sorry, that option is not supported")
