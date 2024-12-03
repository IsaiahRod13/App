#calculator app
#first actual project
#gotta star somewhere

#def main
def main():
    
    #Welecome user
    #provide the operator options 
    print("Hello World")
    print("1: Multiplication: ""*")
    print("2: Division: ""/")
    print("3: Addition: ""+")
    print("4: Subtraction: ""-")
    
    #take in user input for what operator to use and save it as the user variable
    user  = input(("Please enter what type of operator you will be using for your values: \n"))
    
    #prompt and save user input for their variables as an integer
    value1 = int(input("Enter your first value: \n"))
    value2 = int(input("Enter your second value: \n"))
    
    #initialize result
    result = 0
    
    #if statement for each operator
    #performing the calculations for each operator based on user input using elif statements
    #prints result to user
    if user == "*" :
        result = value1 * value2
        print(result)
        
    elif user == "/" :
        result = value1 / value2
        print(result)
        
    elif user == "+" :
        result = value1 + value2
        print(result)
        
    elif user == "-" :
        result = value1 - value2
        print(result)

    
    
    
main()


