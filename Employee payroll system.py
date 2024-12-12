# Employee Payroll System

def display_menu():
    print("\nEmployee Payroll Management System")
    print("1. Add Employee")
    print("2. Update Employee Information")
    print("3. Delete Employee")
    print("4. Display All Employees")
    print("5. Exit")

def add_employee(payroll):
    emp_id = input("Enter Employee ID: ").strip()
    if emp_id in payroll:
        print("Employee ID already exists.")
        return
    name = input("Enter Employee Name: ").strip()
    position = input("Enter Position: ").strip()
    salary = float(input("Enter Salary: ").strip())
    payroll[emp_id] = {"Name": name, "Position": position, "Salary": salary}
    print(f"Employee {name} added successfully.")

def update_employee(payroll):
    emp_id = input("Enter Employee ID to update: ").strip()
    if emp_id not in payroll:
        print("Employee ID not found.")
        return
    print("Enter new details (leave blank to keep current value):")
    name = input(f"Current Name ({payroll[emp_id]['Name']}): ").strip()
    position = input(f"Current Position ({payroll[emp_id]['Position']}): ").strip()
    salary = input(f"Current Salary ({payroll[emp_id]['Salary']}): ").strip()

    if name:
        payroll[emp_id]["Name"] = name
    if position:
        payroll[emp_id]["Position"] = position
    if salary:
        try:
            payroll[emp_id]["Salary"] = float(salary)
        except ValueError:
            print("Invalid salary entered. Keeping the current value.")
    print("Employee information updated successfully.")

def delete_employee(payroll):
    emp_id = input("Enter Employee ID to delete: ").strip()
    if emp_id in payroll:
        del payroll[emp_id]
        print(f"Employee ID {emp_id} deleted successfully.")
    else:
        print("Employee ID not found.")

def display_all_employees(payroll):
    if not payroll:
        print("No employees in the payroll system.")
        return
    print("\nAll Employees:")
    print("ID	Name	Position	Salary")
    print("-" * 40)
    for emp_id, details in payroll.items():
        print(f"{emp_id}	{details['Name']}	{details['Position']}	PKR{details['Salary']:.2f}")

def main():
    payroll = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_employee(payroll)
        elif choice == "2":
            update_employee(payroll)
        elif choice == "3":
            delete_employee(payroll)
        elif choice == "4":
            display_all_employees(payroll)
        elif choice == "5":
            print("Exiting the Employee Payroll System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
