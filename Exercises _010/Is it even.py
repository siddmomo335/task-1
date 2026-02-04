#function that checks if a number is even or odd
def check_even_odd(number):
    #if the remainder when dividing by 2 is 0, its even 
    if number % 2==0:
        return "the number is even."
    else:
        return"the number is odd."
#main function that runs the program
def main():
    #asks the user for a number
    num = int(input("enter a number: "))
    #pass the number to the function and get the result
    result = check_even_odd(num)
    #print the returned message
    print(result)
#run the main function
if __name__  ==  "__main__" :
    main()
