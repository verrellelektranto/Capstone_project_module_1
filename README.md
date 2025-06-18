# CAPSTONE PROJECT MODULE 1
JCDS 2702 - VERRELL ELEKTRANTO
# EMPLOYEE DATA MANAGEMENT APPS (EMPACT) EMPLOYEE IMPACT
    employee_list = []

# CREATE FEATURE

    def add_employee():
    """"Add an employee"""

    # Employee ID (alphanumeric only)
    employee_id = input ("Input employee ID: ")
    while not employee_id.isalnum():
        print("Invalid input, employee ID must contain alphanumeric (letters and numbers only).")
        employee_id = input("Input employee ID: ")

    # Name (letters only)
    name = input("Input employee name: ")
    while not name.isalpha():
        print("Invalid input, name must be letter only. ")
        name = input("Input employee name: ")
    
    # Salary (numeric only)
    while True:
        try:
            salary = float(input("Input monthly salary: "))
            break
        except ValueError:
            print("Invalid input, salary must be numeric.")
    
    # Absence (numeric only)
    while True:
        try:
            absence =int(input("Input absence day: "))
            break
        except ValueError:
            print("Invalid input, absence day must be numeric.")
    
    employee = {"employee_id": employee_id,
                "name": name,
                "monthly salary": salary,
                "absence day": absence, }
    
    employee_list.append(employee)
    print("\nEmployee has been successfully added!\n")

# READ FEATURE

    def show_employee():
    """employee list"""
    
    # DEDUCTION SYSTEM
    deduction_per_absence = 250000
    if not employee_list:
        print("Employee not found")
        return
    
    print("\nEmployee data: ")
    for employee in employee_list:
        absence = employee['absence day']
        salary = employee["monthly salary"]
        deduction = absence * deduction_per_absence
        adjusted_salary = salary - deduction

        print(f"ID: {employee['employee_id']} ")
        print(f"name: {employee['name']}")
        print(f"basic salary: {salary}")
        print(f"absence: {absence}")
        print(f"deduction: {deduction}")
        print(f"total salary: {adjusted_salary}")
        print()

# UPDATE FEATURE

    def update_employee():
    """Update employee data based on ID"""

    employee_id = input("Input the employee ID that requires an update: ")
    for employee in employee_list:
        if employee["employee_id"] == employee_id:
           employee["name"] = input("name: ")
           employee["monthly salary"] = float(input("monthly salary: "))
           employee["absence"] = int(input("absence day: "))
           print("\nEmployee data was successfully updated\n")
           return
    print("Employee ID not found.\n")

# DELETE FEATURE

    def delete_employee():
    """Delete employee data based on ID"""

    employee_id = input("Please input the employee ID to be deleted: ")
    for employee in employee_list:
        if employee["employee_id"] == employee_id:
           employee_list.remove(employee)
           print("\nThe employee ID has been deleted.\n")
           return
    print("Employee ID not found.\n")

# MAIN PAGE

    def main():
    """Main page of the application"""
    while True:
        print("=== EMPACT(Employee impact) employee data management Apps ===")
        print("1. Add employee")
        print("2. Employee list")
        print("3. Update employee")
        print("4. Delete employee")
        print("5. Exit")
        
        select = input("Select menu (1-5): ")
        if select == "1":
            add_employee()
        elif select == "2":
            show_employee()
        elif select == "3":
            update_employee()
        elif select == "4":
            delete_employee()
        elif select == "5":
            print("You have successfully logged out.")
            break
        else:
            print("Invalid input, please try again.")
    main()
