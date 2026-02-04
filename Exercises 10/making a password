#define the correct password
correct_password = "12345"
#define maximum number of attempts
max_attempts = 5
#initialize attempt counter 
attempts = 0
#loop untit password is correct or attepmts are exhausted 
while attempts < max_attempts:
    #ask the user to enter the password
    entered_password = input("enter the password: ")
    #check if the entered password is correct
    if entered_password == correct_password:
        print("access granted. correct password")
        break
#increase the number of attempts
    else:
        attempts +=1
        #calculate remaining attempts
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"incorrect password. attempts remaining: {remaining_attempts} ")
        else:
            print("maximum attempts reached. ")
            print("authorities have been alerted")
