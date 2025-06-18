employee_list = []

# CREATE FEATURE
def create_menu():
    """Sub-menu for adding employees"""
    while True:
        print("\n=== Add Employee Menu ===")
        print("1. Add New Employee")
        print("2. Return to Main Menu")
        choice = input("Select an option [1-2]: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please select a valid option.")

def add_employee():
    """Add an employee with validated input"""
    
    # Validate Employee ID (alphanumeric only)
    employee_id = input("Input Employee ID: ")
    while not employee_id.isalnum():
        print("Invalid input, ID must be alphanumeric.")
        employee_id = input("Input Employee ID: ")

    # Validate Name (letters and spaces only)
    name = input("Input Employee Name: ")
    while not name.replace(" ", "").isalpha():
        print("Invalid input, name must contain letters only.")
        name = input("Input Employee Name: ")

    # Validate Monthly Salary (numeric only)
    while True:
        try:
            salary = float(input("Input Monthly Salary: "))
            break
        except ValueError:
            print("Invalid input, salary must be numeric.")

    # Validate Absence Days (numeric only)
    while True:
        try:
            absence = int(input("Input Absence Days: "))
            break
        except ValueError:
            print("Invalid input, absence days must be numeric.")

    # Confirmation step before adding employee
    while True:
        confirm = input(f"Confirm adding {name} (ID: {employee_id})? (Y/N): ").strip().lower()
        if confirm == "y":
            employee = {"employee_id": employee_id, "name": name, "monthly_salary": salary, "absence_days": absence}
            employee_list.append(employee)
            print("\nEmployee has been successfully added!\n")
            return
        elif confirm == "n":
            print("\nAddition canceled.\n")
            return
        else:
            print("Invalid input, please enter 'Y' or 'N'.")

# READ FEATURE
def read_menu():
    """Sub-menu for viewing employees"""
    while True:
        print("\n=== Employee Records Menu ===")
        print("1. View All Employees")
        print("2. Search Employee by ID")
        print("3. Return to Main Menu")
        choice = input("Select an option [1-3]: ")

        if choice == "1":
            show_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please select a valid option.")

def show_employee():
    """Show all employees"""
    deduction_per_absence = 250000
    if not employee_list:
        print("No employee data available.")
        return

    print("\nEmployee Data:")
    for employee in employee_list:
        absence = employee['absence_days']
        salary = employee["monthly_salary"]
        deduction = absence * deduction_per_absence
        adjusted_salary = salary - deduction

        print(f"ID: {employee['employee_id']}")
        print(f"Name: {employee['name']}")
        print(f"Base Salary: {salary}")
        print(f"Absence Days: {absence}")
        print(f"Deduction: {deduction}")
        print(f"Total Salary: {adjusted_salary}\n")

def search_employee():
    """Search employee by ID with adjusted salary calculation"""
    emp_id = input("Enter Employee ID to search: ")
    deduction_per_absence = 250000 

    for employee in employee_list:
        if employee["employee_id"] == emp_id:
            absence = employee["absence_days"]
            salary = employee["monthly_salary"]
            deduction = absence * deduction_per_absence
            adjusted_salary = salary - deduction

            print("\nEmployee Found:")
            print(f"ID: {employee['employee_id']}")
            print(f"Name: {employee['name']}")
            print(f"Base Salary: {salary}")
            print(f"Absence Days: {absence}")
            print(f"Deduction: {deduction}")
            print(f"Total Salary: {adjusted_salary}\n")
            return

    print("Employee ID not found.\n")

# UPDATE FEATURE
def update_menu():
    """Sub-menu for updating employees"""
    while True:
        print("\n=== Update Employee Menu ===")
        print("1. Update Employee Data")
        print("2. Return to Main Menu")
        choice = input("Select an option [1-2]: ")

        if choice == "1":
            update_employee()
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please select a valid option.")

def update_employee():
    """Update employee data based on ID with validation"""
    emp_id = input("Input the Employee ID to update: ")
    while not emp_id.isalnum():
        print("Invalid input, ID must be alphanumeric.")
        emp_id = input("Input Employee ID to update: ")

    for employee in employee_list:
        if employee["employee_id"] == emp_id:

            # Validate new name (letters and spaces only)
            new_name = input("New Name: ")
            while not new_name.replace(" ", "").isalpha():
                print("Invalid input, name must contain letters only.")
                new_name = input("New Name: ")

            # Validate new monthly salary (numeric only)
            while True:
                try:
                    new_salary = float(input("New Monthly Salary: "))
                    break
                except ValueError:
                    print("Invalid input, salary must be numeric.")

            # Validate updated absence days (numeric only)
            while True:
                try:
                    new_absences = int(input("Updated Absence Days: "))
                    break
                except ValueError:
                    print("Invalid input, absence days must be numeric.")

            # Confirmation step
            while True:
                confirm = input(f"Confirm update for {emp_id}? (Y/N): ").strip().lower()
                if confirm == "y":
                    employee["name"] = new_name
                    employee["monthly_salary"] = new_salary
                    employee["absence_days"] = new_absences
                    print("\nEmployee data updated successfully!\n")
                    return
                elif confirm == "n":
                    print("\nUpdate canceled.\n")
                    return
                else:
                    print("Invalid input, please enter 'Y' or 'N'.")

    print("Employee ID not found.\n")

# DELETE FEATURE
def delete_menu():
    """Sub-menu for deleting employees"""
    while True:
        print("\n=== Delete Employee Menu ===")
        print("1. Delete Employee")
        print("2. Return to Main Menu")
        choice = input("Select an option [1-2]: ")

        if choice == "1":
            delete_employee()
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please select a valid option.")

def delete_employee():
    """Delete employee data based on ID with confirmation"""
    employee_id = input("Input Employee ID to delete: ")
    for employee in employee_list:
        if employee["employee_id"] == employee_id:
            
            # Confirmation step
            while True:
                confirm = input(f"Confirm deletion for {employee_id}? (Y/N): ").strip().lower()
                if confirm == "y":
                    employee_list.remove(employee)
                    print("\nThe employee record has been deleted.\n")
                    return
                elif confirm == "n":
                    print("\nDeletion canceled.\n")
                    return
                else:
                    print("Invalid input, please enter 'Y' or 'N'.")
    print("Employee ID not found.\n")

# MAIN PAGE
def main():
    """Main menu with structured sub-menus"""
    while True:
        print("\n=== EMPACT (Employee Impact) Management System ===")
        print("1. Add Employee")
        print("2. View Employee Records")
        print("3. Update Employee Data")
        print("4. Delete Employee Data")
        print("5. Exit")

        choice = input("Select an option [1-5]: ")
        if choice == "1":
            create_menu()
        elif choice == "2":
            read_menu()
        elif choice == "3":
            update_menu()
        elif choice == "4":
            delete_menu()
        elif choice == "5":
            print("You have successfully logged out.")
            break
        else:
            print("Invalid input, please try again.")
main()



        




    