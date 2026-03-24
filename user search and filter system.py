import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    while True:
        menu = input("1. Show all users\n2. Search by name\n3. Filter by city\n4. Exit\n")

        if menu == "1":
            for user in data:
                print(user["name"])

        elif menu == "2":
            search_name = input("Enter name to search: ")
            found_users = False
            for user in data:
                if search_name.lower() in user["name"].lower():
                    print(user["name"], user["address"]["city"])
                    found_users = True
            if not found_users:
                print(f"No user found with name '{search_name}'.")

        elif menu == "3":
            search_city = input("Enter city to filter by: ")
            found_users = False
            for user in data:
                if search_city.lower() in user["address"]["city"].lower():
                    print(user["name"], user["address"]["city"])
                    found_users = True
            if not found_users:
                print(f"No user found in city '{search_city}'.")

        elif menu == "4":
            break

        else:
            print("Invalid option")

else:
    print("Error fetching data")