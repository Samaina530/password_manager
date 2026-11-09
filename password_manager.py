import random
import string

running= True

chars = list(string.ascii_letters + string.digits + string.punctuation)
key = chars.copy()
random.shuffle(key)

while running:

    master_pwd=input("Enter your password(q to quit): ")

    def add():

        account=input("Enter your account: ")
        user_name=input("Enter your username: ")
        password=input("Enter your password: ")

        data= account +' | '+ user_name

        cipher = ""

        for line in password:
            index=chars.index(line)
            cipher+=key[index]

        with open("password.txt","a") as file:
            file.write(data)
            file.write(f' | (password= {cipher}) \n')
            print("Password saved!")


    def view():

          search = input("Enter account name: ")

          with open("password.txt", "r") as f:
            for line in f:

                if search in line:
                    print(line)
                    break

            else:
                print("Account not found!")


    if master_pwd == "Selenophile":
        pwd=input("Do you wanna add or view password?(add or view): ").lower()

        if pwd=="add":
            add()
        if pwd=="view":
            view()

    elif master_pwd == "q":
        running=False
        print("Goodbye!")

    else:
         print("Invalid Input")
         running=True




