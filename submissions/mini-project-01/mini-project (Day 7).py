shopping_list = []
choice = 0

while choice != 4:
    print("\nOptions:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

    choice = int(input("\nEnter the number of your choice: "))

    if choice == 1:
        add_item = input("\nEnter the item you want to add: ")
        shopping_list.append(add_item)
        print(f"{add_item} has been added to your shopping list.")
    
    elif choice == 2:
        print("\nYour shopping list:")
        for item in shopping_list:
            print(item)

    elif choice == 3:
        remove_item = input("\nEnter the item you want to remove: ")
        if remove_item not in shopping_list:
            print("Item is not in the shopping list.")
        else:
            shopping_list.remove(remove_item)
            print(f"{remove_item} has been removed from you shopping list.")
    
    else:
        print("\nChoose a number from the options only!")

print("Goodbye!")    

