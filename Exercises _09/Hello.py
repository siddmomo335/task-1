#define a function that prints "hello"
def hello():
    print("hello") # this prints "hello" to the console
#define the main function that calls hello()
def main():
    hello()  # this calls the hello() function
#run the main function only if this file is executed directly
if __name__ == "_main__":
    main()  #this starts the program by calling main()
