"""Expense Tracker"""
print(__doc__)
Expenses={

}
while True:
    option=["Add Expense","View Expense","Exit"]
    for a,b in enumerate(option, start=1):
        print(f"{a}.{b}")
    choice=int(input("Enter Your Choice (1-3):"))
    if choice==1:
        expense_name=input("Enter Expense name:")
        expense_amount=int(input("Enter expense amount:"))
        if expense_name in Expenses:
            Expenses[expense_name].append(expense_amount)
        else:
            Expenses[expense_name]=[expense_amount]
        print("Expense Added Successfuly")
    elif choice==2:
        for i,j in Expenses.items():
            for amount in j:
                print(f" Expense Name : {i} | Expense amount : {amount}")
    elif choice==3:
        total=0
        for i,j in Expenses.items():
            for amount in j:
                total+=amount
        print(total)
        print("program exit, Bye!")
        break

    else:
        print("Invalid Choice, Choose number b/w(1-3)")