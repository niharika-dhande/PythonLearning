import re
def MakeDataBase():
    """Gathers customer data and returns it as a dictionary."""
    while True:
        name = input('Please enter your name: ').strip()
        if name and re.match(r"^[A-Za-z\s]+$", name):
            break
        print("Invalid name. Please enter a valid name (letters and spaces only).")

    while True:
        contact_number = input('Enter your contact number: ').strip()
        if contact_number and re.match(r"^\+?\d{10,15}$", contact_number):
            break
        print("Invalid contact number. Please enter a valid contact number (10-15 digits, optional leading '+').")

    while True:
        email = input('Enter your email address: ').strip()
        if email and re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            break
        print("Invalid email address. Please enter a valid email address.")
    return {"Name": name, "Contact_Number": contact_number, "Email": email}

def get_faqs():
    """Gathers FAQs and returns them as a list of dictionaries."""
    faqs = []
    while True:
        question = input("Enter a FAQ question (or 's' to finish): ").strip()
        if question.lower() == "s":
            break
        if not question:
            print("Question cannot be blank. Please enter a question.")
            continue

        while True:
            answer = input("Enter the answer to the question: ").strip()
            if answer:
                break
            print("Answer cannot be blank. Please enter an answer.")
        faqs.append({"Question": question, "Answer": answer})
    return faqs

def save_data_to_file(customer_data, faqs, filename="CustomerDataAndFAQs.txt"):
    """Writes customer data and FAQs to a file."""
    try:
        with open(filename, 'a') as file:
            file.write(f"\n\nName: {customer_data['Name']}\nContact Number: {customer_data['Contact_Number']}\nEmail: {customer_data['Email']}\n")
            file.write("FAQs:\n")
            for faq in faqs:
                file.write(f"Q: {faq['Question']}\nA: {faq['Answer']}\n")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def read_data_from_file(filename="CustomerDataAndFAQs.txt"):
    """Reads and prints data from a file."""
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# Continuously prompt for customer data and FAQs until the user types "s"
while True:
    user_input = input("Enter a customer name (or 's' to quit): ").strip()
    if user_input.lower() == "s":
        break  # Exit the loop if the user enters "s"

    # Get customer data
    customer_data = MakeDataBase()

    # Get FAQs
    faqs = get_faqs()

    # Save the data and FAQs
    save_data_to_file(customer_data, faqs)

    # Read and display the data
    read_data_from_file()

