type_of_transportation=str(input("What is your family's usual transportation (Please enter one of the following (Please enter PERSONAL VEHICLE or PUBLIC TRANSPORTATION): "))
type_of_transportation=type_of_transportation.lower()
type_of_transportation=type_of_transportation.replace(" ", "")

loans = str(input("Do you have any loans? Please enter YES or NO: "))
loans = loans.lower()
loans = loans.replace(" ", "")
if loans == 'yes':
    total_loans = int(input("Enter the total payment for loans in a year: "))
insurance = str(input("Do you have an insurance? Please enter YES or NO: "))
insurance = insurance.lower()
insurance = insurance.replace(" ", "")

housing = str(input("Do you live on a rental property or a personal property (Please enter RENTAL or PERSONAL): "))
housing = housing.lower()
housing = housing.replace(" ", "")

food = str(input("Do you typically eat at home or outside (Please enter HOME or OUTSIDE): "))
food = housing.lower()
food = housing.replace(" ", "")

