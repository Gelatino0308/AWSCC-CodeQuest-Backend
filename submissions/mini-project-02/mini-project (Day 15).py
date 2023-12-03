import manager_ops

menu_choice = 0

while menu_choice != 6:
    print("\n----- WELCOME TO THE COMMAND LINE PASSWORD MANAGER APP -----\n")
    print("(1) Add a Password, Email, and Name of Website")
    print("(2) View All Inputs")
    print("(3) Search for a Specific Input")
    print("(4) Delete an Existing Input")
    print("(5) Update a Specific Input")
    print("(6) Exit")

    try:
        menu_choice = int(input("\nEnter the number of your command from the menu: "))

        if menu_choice == 1:

            manager_ops.add()

        elif menu_choice == 2:

            manager_ops.view()

        elif menu_choice == 3:

            web_name = input("\nEnter website name to search: ")
            manager_ops.search(web_name)

        elif menu_choice == 4:
            
            exists = False
            choice = 1

            while not exists:

                web_name = input("\nEnter website name to delete: ")
                exists, choice = manager_ops.is_existing(web_name)

                if choice == 0:
                    break
            
            if choice == 0:
                continue

            manager_ops.delete(web_name)

        elif menu_choice == 5:

            exists = False
            choice = 1

            while not exists:
                
                web_name = input("\nEnter website name to update: ")
                exists, choice = manager_ops.is_existing(web_name)

                if choice == 0:
                    break
            
            if choice == 0:
                continue
            else:
                manager_ops.update(web_name)
        
        elif menu_choice == 6:
            print("\n>> Exiting...")

        else:
            print("\n>> Choose a number from the options only!\n")

    except Exception as e:
        print(f"Invalid input: {e}\n")
        continue
        