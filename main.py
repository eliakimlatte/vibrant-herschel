Bank_Name = ("ELAmericanbank")
custumer_servise = ("helper")
credit_card_account =[
    "1. Cashback Credit Card",
    "2. Travel Rewards Card",
    "3. Low-Interest Card"
] 


print(f"Hello! Welcome to {Bank_Name}. I'm here to help you find the perfect credit card account for your needs.")
print("Can I ask a few quick questions to get started?")

print("\nHere are some credit card options we offer:")
for option in credit_card_account:
    print(option)


card_choice = ""
while card_choice not in ["1", "2", "3"]:
    card_choice = input("\nfirst, what type of credit card account are you looking for? Please type the number (1, 2, or 3): ")


if card_choice == "1":
    print("\nA Cashback Credit Card is a card that gives you cash back or rewards for your spending. "
          "For example, if you spend $500 on a card that offers 1.5% cashback, you earn $7.50 back.")
elif card_choice == "2":
    print("\nA Travel Rewards Card offers points or miles for travel-related expenses, "
          "which can be redeemed for flights, hotel stays, and other travel perks.")
elif card_choice == "3":
    print("\nA Low-Interest Card is a great option if you're looking to minimize interest payments. "
          "It offers lower rates on outstanding balances compared to other credit cards.")
else:
    print("\nSorry, I didn't understand that. Please choose a valid option (1, 2, or 3).")



ready_for_details = input("\nNow that we know which account you’d like to open."
                         "Do you have your personal details ready? ")
if ready_for_details.lower() == "yes":
    print("let’s get you started with the sign-up process.")
elif ready_for_details.lower() == "no":
    print("\ncan you Please get your personal details ready."
          "Thank you")


name = input("Please enter your full name: ")
dob = input("Please enter your date of birth (e.g., 01/01/1990): ")
address = input("Please enter your address (e.g., 1234 Elm St, City, State): ")

print(f"\nThanks, {name}! I have your details as follows:\n"
      f"Date of Birth: {dob}\n"
      f"Address: {address}")

ssn_or_id = input("\nNext, I’ll need your social security number (or government ID) for identity verification: ")

print("Here are the verification options:")
verification_option = [
    "Email", 
    "Phone Number"
    ]


for option in verification_option:
    print(option)

verification_choice =input("\nI just need to verify your identity to make sure everything is secure. "
                            "You’ll receive a one-time code on your email or phone number. "
                            "Which one would you prefer? (Email/Phone Number): ")

if verification_choice.lower() == "email":
    print(f"\nGreat! We will send a verification code to your email address, {name}. Please check your inbox.")
elif verification_choice.lower() == "phone number":
    print(f"\nGreat! We will send a verification code to your phone number, {name}. Please check your messages.")
else:
    print("\nSorry, I didn't understand that. Please choose either 'Email' or 'Phone Number'.")




print(f"Thank you, {name}, your verification was successful and your credit card application is now in process!")




print(f"Thank you, {name}, your verification was successful and your credit card application is now in process!")


