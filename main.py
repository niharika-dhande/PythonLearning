def MakeDataBase():
    """Gathers customer data and returns it as a dictionary."""
    name = input('Please enter your name: ')
    contact_number = input('Enter your contact number: ')
    email = input('Enter your email address: ')
    return {"Name": name, "Contact_Number": contact_number, "Email": email}

def save_customer_data(customer_data, filename="HelloFile.txt"):
    """Appends customer data to a file."""
    with open(filename, 'a') as file:
        file.write(f"\n\nName:{customer_data['Name']}\nContact_Number:{customer_data['Contact_Number']}\nEmail:{customer_data['Email']}")

def read_customer_data(filename="HelloFile.txt"):
    """Reads and prints customer data from a file."""
    with open(filename, 'r') as file:
        print(file.read())



# Continuously prompt for names until the user types "stop"
while True:
    user_input = input("Enter a customer name (or 'stop' to quit): ")
    if user_input.lower() == "stop":
        break  # Exit the loop if the user enters "stop"
# Get customer data
customer_data = MakeDataBase()

# Save the data
save_customer_data(customer_data)

# Read and display the data
read_customer_data()
