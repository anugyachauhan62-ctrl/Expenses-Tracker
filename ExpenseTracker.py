#Expense Tracker Project 

expensesList = []#List of expenses in from of dictionary
print("Welcome to Expense Tracker : kharcha kam kiya karo")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total khrcha")
    print("4. Exit")

    choice= input("Please enter your Choice :")

#ADD Expense
    if(choice =="1"):
        date= input("kis date par khrcha kiya tha?")
        category= input("kis type ka khrcha kiya?(Food, Travel, Makeup, Books)")
        description= input("Aur detail dedo")
        amount= float(input("Enter the amounnt:"))

        expenses= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expenses)
        print("\n DONE bro. Expense is added succesfully")

#2. VIEW ALL EXPENSES
    elif (choice == "2"):
        if( len(expensesList)==0):
            print("No Expenses Added.Jao pehle khrcha karo.")
        else:
            print("===== ye y apka sara expense ======")
            count= 1
            for eachkharcha in expensesList:
                print(f"kharcha Number {count} -> {eachkharcha["date"]},{eachkharcha["category"]},{eachkharcha["description"]},{eachkharcha["amount"]}")
                count= count+1

#3. View Total Spending
    elif(choice == "3"):
        total= 0
        for eachkrcha in expensesList:
            total = total + eachkrcha["amount"]
        print("\n TOTAL KHRCHA = ", total)

#4. EXIT
    elif(choice == "4"):
        print("Dhanyawad aapne humara system use kiya")
        break
    else:
        print("INVEID CHOICE. TRY AGAIN")
