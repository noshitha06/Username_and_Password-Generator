'''

  * Class: 44-141 Computer Programming I

  * Author:Noshithareddy Gudhibandi,Brooklen Black

  * Description: creating a username and password generator program. 

  * Due:06-03-2024

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.

'''


#declaring the variables
outer_count=1
import random
count=0
x=random.randint(0,3)
#outer whileloop
while(outer_count!=0):
    #menu for user
    print("\n**menu**")
    print("‘u’ to create usernames from file\n‘p’ to generate a password\n‘q’ to quit the program")
    #commands from user
    num=str(input("Enter a command:"))
    #to read from and write to files and if u is the command
    if(num=="u"):
        file=input("Enter the file name:")
        readFile = open(file,"r")
        #open a file to write to
        printfile= open ("username.txt","w")

        #for loop to process each line in the read file
        for line in readFile:
            #to create username we have to split 
            nameList=line.split(",")
            Last=nameList[1]
            First=nameList[0]
            number=nameList[2]
            userlastname=Last[:4]
            userfirstname=First[:3]
            usernumber=number[7:]
            userName=First+Last+"'s "
            final_user = userlastname+userfirstname+usernumber
            final_user = final_user.lower()
            printfile.write("\n")
            printfile.write(userName)
            printfile.write("username is:")         
            printfile.write(final_user)
       # print("Usernames sucessfully created and written to file")
        readFile.close()
        printfile.close()
    print("Usernames sucessfully created and written to file")
    #if p is the command                  
    if(num=="p"):
        #inner while loop to create password
        while(count<=3):
            #to create the password converting ACSII values
            sum=random.randint(65,90)
            y=random.randint(97,122)
            print(random.randint(0,9),end="")
            print(chr(y)+chr(sum),end="")
            count+=1
            #for special character toprint randomly
            if(count==x):
                x=random.randint(35,38)
                print(chr(x),end="")
    #if q is the command 
    if(num =="q"):
        print("Thank you for using the username/password generator")
        break
    #if the command wasn't include in menu 
    if(num!="u" and num!="p" and num!="q"):
        print("Invalid input") 
