def employee_payroll(salary):
    return salary
try:
    employee_name=input("enter your name:")
    hours_worked=int(input("enter hours worked:"))
    hourly_rate=15/100
    salary=(hourly_rate*100000*hours_worked)
    print(employee_payroll(salary))
except ValueError:
    print("please enter the right value")


