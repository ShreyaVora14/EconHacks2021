name=input ("Enter your name: ")
adults=int(input('Enter the number of adults (18+) in your family: '))
children=int(input('Enter the number of children (under 18) in your family: '))
people_working=int(input('Enter the number of people working in your household: '))
total_income=0
for i in range(0,people_working):
    income=int(input("Enter the annual income for Person"+str(i+1)+": "))
    total_income+=income
attend_school = int(input("Enter the number of people attending school in your household: "))






