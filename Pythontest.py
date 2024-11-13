#Princedaniel Ehimen-Abuya
#Pythontest.py
#Determine if the user is on the dean's list or honor roll.
counter=0
while True:
    #Lname["Smith","Joestar","Bludhound","Jackson","Heartwith"]
    Lname = input("What is your lastname ")
    if Lname == "ZZZ":
        print("alright we are done.")
        exit()
    else:
        Fname= input("What is your Firstname ")

        x = float(input(f"Hello {Fname} {Lname}, what is your GPA? ")) 
        if x >=3.5:
            print("You have made the Dean's List")
        elif x>=3.25:
            print("You have made the Honor Roll.")
        else:
            print("You haven't made any list good luck next time.")
        counter+=1

        if counter == 5:
            break   