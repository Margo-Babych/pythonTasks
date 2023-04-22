"""Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program"""

import json

file_path = "phonebook_filename.py"


def read_dataset(file_path):
    with open(file_path, 'r', encoding='uft-8') as file:
        dataset = json.load()
    return dataset


def write_dataset(dataset, file_path):
    with open(file_path, 'w', encoding='uft-8') as file:
        json.dump(dataset, file)


new_data = {
    "first_name": "",
    "last_name": "",
    "phone": "",
    "city": "",
    "country": ""
}

command_key = {
    "sf": "first_name",
    "sl": "last_name",
    "sp": "phone",
    "sct": "city",
    "sc": "country"
}

field_names = ["first_name", "last_name", "phone", "city", "country"]



def input_contact():
    our_data = new_data.copy()
    for key, name in zip(our_data.keys(), field_names):
        our_data[key] = input(f'Enter {name}: ' )
    return our_data

def read_commands():
    print("You can choice: ",
          "n - new data",
          "sf - find first_name",
          "sl - find last_name",
          "sfl - find full_name",
          "sp - find phone",
          "sct - find city",
          "sc - find country",
          "up - update data",
          "del - delete data",
          "exit - exit", sep='\n')

    command = input("Enter command: ")
    if command == 'n':
        save_data(input_contact())
        print("Data saved")
        return True
    elif command in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
        find_type = command
        find_value = input("Enter value: ")
        if find_type in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
            contact = search_by(find_type, find_value)
            if contact != None and len(contact) == 5:
                print("Found: ")
                print_result(contact)
                return True
            elif len(contact) > 5:
                print("Found some numbers: ")
                print(contact)
                return True
            else:
                print("Not found")
                return True
        elif command == 'up':
            update_contact()



def search_by(command, value):
    with open('data.json', 'r', encoding='utf-8') as data_file:
        database = json.load(data_file)
    if command != 'sfl':
        for i in range(len(database)):
            if dict(database[i])[command_key[command]] == value:
                return dict(database[i])

    else:
        for i in range(len(database)):
            full_name = dict(database[i])['first_name'] + ' ' + dict(database[i]['last_name'])
            if full_name == value:
                return dict(database[i])

def update_contact():
    print("Found contact for update:  ")
# Helper function to search phonebook by key and value
def search_phonebook(key, value, phonebook=None):
    results = []
    for record in phonebook:
        if record.get(key) == value:
            results.append(record)
    return results


# Helper function to save phonebook data to file
def save_phonebook(phonebook="phonebook_filename.py"):
    with open("phonebook_filename.py", "w") as f:
        json.dump(phonebook, f)


# Main loop
while True:
    print("Phonebook application\n")
    print("1. Add new entry")
    print("2. Search by first name")
    print("3. Search by last name")
    print("4. Search by full name")
    print("5. Search by telephone number")
    print("6. Search by city or state")
    print("7. Delete a record for a given telephone number")
    print("8. Update a record for a given telephone number")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add new entry
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter telephone number: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        record = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "city": city,
            "state": state,
        }
        phonebook.append(record)
        print("Record added successfully.\n")

    elif choice == "2":
        # Search by first name
        first_name = input("Enter first name: ")
        results = search_phonebook("first_name", first_name)
        if len(results) == 0:
            print("No records found.\n")
        else:
            print("Search results:\n")
            for record in results:
                print(f"{record['first_name']} {record['last_name']}")
            print()

    elif choice == "3":
        # Search by last name
        last_name = input("Enter last name: ")
        results = search_phonebook("last_name", last_name)
        if len(results) == 0:
            print("No records found.\n")
        else:
            print("Search results:\n")
            for record in results:
                print(f"{record['first_name']} {record['last_name']}")
            print()

    elif choice == "4":
        # Search by full name
        full_name = input("Enter full name: ")
        results = []
        for record in "phonebook_filename.py":
            if f"{record['first_name']} {record['last_name']}" == full_name:
                results.append(record)
        if len(results) == 0:
            print("No records found.\n")
        else:
            print("Search results:\n")
            for record in results:
                print(f"{record['first_name']} {record['last_name']}")
            print()

    elif choice == "5":
        # Search by telephone number
        phone_number = input("Enter telephone number: ")
        results = search_phonebook("phone_number", phone_number)
        if len(results) == 0:
            print("No records found.\n")
        else:
            print("Search results:\n")
            for record in results:
                print(f"{record['first_name']} {record['last_name']}")
            print()

    elif choice == "6":
        # Search by city or state
        city_or_state = input("Enter city or state: ")
        results = []
        for record in phonebook:
            if record["city"] == city_or_state or record["state"] == city_or_state:
                results.append(record)
        if len(results) == 0:
            print("No records found.\n")
        else:
            print("Search results:\n")
            for record in results:
                print(f"{record['first_name']} {record['last_name']} ({record['phone_number']})")
                print(f"{record['city']}, {record['state']}\n")

    elif choice == "7":
        # Delete a record for a given telephone number
        phone_number = input("Enter telephone number: ")
        results = search_phonebook("phone_number", phone_number)
        if len(results) == 0:
            print("No records found.\n")
        else:
            for record in results:
                print(
                    f"Are you sure you want to delete the record for {record['first_name']} {record['last_name']} ({record['phone_number']})? (y/n)")
                confirm = input()
                if confirm.lower() == "y":
                    phonebook.remove(record)
                    print("Record deleted successfully.\n")
                else:
                    print("Deletion cancelled.\n")

    elif choice == "8":
        # Update a record for a given telephone number
        phone_number = input("Enter telephone number: ")
        results = search_phonebook("phone_number", phone_number)
        if len(results) == 0:
            print("No records found.\n")
        else:
            record = results[0]
            print("Current record:")
            print(f"{record['first_name']} {record['last_name']} ({record['phone_number']})")
            print(f"{record['city']}, {record['state']}\n")
            print("Enter new values (leave blank to keep current value):")
            first_name = input(f"First name ({record['first_name']}): ") or record["first_name"]
            last_name = input(f"Last name ({record['last_name']}): ") or record["last_name"]
            phone_number = input(f"Phone number ({record['phone_number']}): ") or record["phone_number"]
            city = input(f"City ({record['city']}): ") or record["city"]
            state = input(f"State ({record['state']}): ") or record["state"]
            new_record = {
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
                "city": city,
                "state": state,
            }
            phonebook.remove(record)
            phonebook.append(new_record)
            print("Record updated successfully.\n")

    elif choice == "9":
        # Exit program
        save_phonebook()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")
