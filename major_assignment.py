def basic_salary(hourly_rate, hours_worked_per_week):
    basic_hrs = min(hours_worked_per_week, 40);
    return basic_hrs*hourly_rate*4

def overtime_salary(hourly_rate, hours_worked_per_week):
    overtime_hrs = max(0, hours_worked_per_week - 40)
    return overtime_hrs*hourly_rate*1.5*4

def total_salary(hourly_rate, hours_worked_per_week):
    return overtime_salary(hourly_rate, hours_worked_per_week) + basic_salary(hourly_rate, hours_worked_per_week)

# tax amount based on basic salary
def tax_amount(basic_salary):
    if basic_salary < 60000:
       return basic_salary * 0.1
    elif 60000 <= basic_salary <= 85000:
        return basic_salary * 0.15
    else: 
        return basic_salary * 0.2

# gross salary
def gross_salary(basic_salary):
    allowance = basic_salary * 0.2
    taxes = tax_amount(basic_salary)
    return basic_salary + allowance - taxes

# salary bracket
def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low Income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle Income"
    else: 
        return "High Income"

def employee_report(employees):
    print("Employee Salary Report".center(90, "="))
    print(f"{'Name':<20}{'Hours Worked':<15}{'Basic Salary':<15}{'Gross Salary':<15}{'Tax Amount':<15}{'Bracket':<15}")
    print("*" * 90)
    
    for name, hourly_rate, hours_per_week in employees:
        basic = basic_salary(hourly_rate, hours_per_week)
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        
        print(f"{name:<20}{hours_per_week:<15}{basic:<15.2f}{gross:<15.2f}{tax:<15.2f}{bracket:<15}")
    print("*" * 90)

# employee details are taken as user input
employees = []
emplyee_number = 3

for i in range(emplyee_number):
    name = input("Enter employee name: ")
    hourly_rate = float(input("Enter hourly rate: "))
    hours_per_week = int(input("Enter hours worked per week: "))
    employees.append((name, hourly_rate, hours_per_week))

# Generating employee salary report
employee_report(employees)