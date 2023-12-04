import json
import os

def is_existing (web_key):

    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)

        if web_key in data_dict:
            return True, 1
        
        while (True):
            try:
                print("\n>> Website doesn't exists!")
                print("\t[Enter '1' - Try again]")
                print("\t[Enter '0' - Go back to menu]")
                choice = int(input(">> "))
                
                if choice == 1 or choice == 0:
                    return False, choice
            
            except Exception as e:
                print(f"\n>> Invalid input: {e}\n")
        
def add():

    web_key = input("\nEnter name of website to be added: ")
    user_email = input("Enter your email address: ")
    user_pass = input("Enter your password: ")

    new_data_dict = {
        web_key: [{
            "email": user_email,
            "password": user_pass
        }]
    }

    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)

        if web_key in data_dict:
            data_dict[web_key].append({"email": user_email, "password": user_pass})
        else:
            data_dict.update(new_data_dict)

    with open("web_data.json", 'w') as file:
        json.dump(data_dict, file, indent=4)
    
    os.system("cls")
    print("\n>> Successfully added.\n")

def view():
    os.system("cls")
    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)

        for key_name, val_list in data_dict.items():
            print(f"\nWebsite: {key_name}")
            
            for user_data_dict in val_list:
                print(f"\tEmail: {user_data_dict['email']}")
                print(f"\tPassword: {user_data_dict['password']}\n")

def search(web_key):
    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)

        for key_name, val_list in data_dict.items():
            if web_key == key_name:
                print(f"\nWebsite: {key_name}")

                for user_data_dict in val_list:
                    print(f"\tEmail: {user_data_dict['email']}")
                    print(f"\tPassword: {user_data_dict['password']}\n")
                return 
        
        print("\n>> No website of that name found.\n")
        return 

def delete(web_key):

    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)
        delete_scope = -1

        while (delete_scope != 1 and delete_scope != 0):
            try:
                search(web_key)

                print("\nDelete the entire website's data content or a specific data only? ")
                print("\t[Enter '1' - Delete entire data of the website]")
                print("\t[Enter '0' - Delete specific data of a website only]")
                delete_scope = int(input(">> "))

                if delete_scope == 1:
                    del data_dict[web_key]

                elif delete_scope == 0:
                    valid_idx = False

                    while not valid_idx:

                        data_num = int(input(("\nEnter the number of the specific email-password data to delete: ")))
                        valid_idx = data_num > 0 and data_num <= len(data_dict[web_key])
                        if not valid_idx:
                            print("\n>> No email-password data exists with such number!\n")
                    
                    data_dict[web_key].pop(data_num-1)

                    if (len(data_dict[web_key]) == 0):
                        data_dict.pop(web_key)
                else:
                    print("\n>> Choose between '1' or '0' only!\n")
            
            except Exception as e:
                print(f"\n>> Invalid input: {e}\n")

    with open("web_data.json", 'w') as file:
        json.dump(data_dict, file, indent=4)

    os.system("cls")
    print("\n>> Successfully removed.\n")

def update(web_key):

    with open("web_data.json", 'r') as file:
        data_dict = json.load(file)

        search(web_key)
        valid_idx = False

        while not valid_idx:
            try:
                data_num = int(input(("\nEnter the number of the specific email-password data to update: ")))
                valid_idx = data_num > 0 and data_num <= len(data_dict[web_key])
                if not valid_idx:
                    print("\n>> No email-password data exists with such number!\n")

            except Exception as e:
                print("\n>> Invalid input: {e}\n")
        
        valid_key = False
        while not valid_key:

            data_choice = input("Enter which data to update ['email' or 'password']: ").lower()
            if data_choice == "email" or data_choice == "password":
                valid_key = True
            else:
                print("\n>> Only 'email' or 'password' can be recognized!\n")

        new_data_key = input(f"Enter your new {data_choice}: ")

        data_dict[web_key][data_num-1][data_choice] = new_data_key

    with open("web_data.json", 'w') as file:
        json.dump(data_dict, file, indent=4)

    os.system("cls")
    print("\n>> Successfully updated.\n")
