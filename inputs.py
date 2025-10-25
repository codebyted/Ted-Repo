First_name = input("Enter your First Name: ")
Middle_name = input("Enter your Middle Name:")
Last_name = input("Enter your Last Name:")
Year_of_Birth = int(input("Enter your Year of Birth:"))
Location = input('Enter your Current Location:')
Weather =input ("Give your opinion on Today's Weather:")

age = int(Year_of_Birth)
age = 2025 - Year_of_Birth
print(f"Hello {First_name}!")
print(f"You are {age} years old ")
print(f" {Last_name} says the weather is {Weather}")
print(f"{First_name} {Last_name} is currently at {Location}")