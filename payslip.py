import openpyxl
import random

class Employee:
    def __init__(self, first_name, last_name, job_title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary

    def generate_payslip(self):
        payslip = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nJob Title: {self.job_title}\nSalary: {self.salary}"
        return payslip


class Company:
    def __init__(self, first_name, last_name, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self, filename):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Payroll"
        sheet.append(["نام", "نام خانوادگی", "شغل", "حقوق($)"])

        for employee in self.employees:
            sheet.append([
                employee.first_name,
                employee.last_name,
                employee.job_title,
                employee.salary,
            ])

        wb.save(filename)
        print("لیست کارمندان با دیتای مورد نظر ساخته شد.")


company = Company("University", "Limited", "UniversityLimited")

num_employees = int(input("تعداد کارمندان را وارد کنید: "))

for i in range(num_employees):
    first_name = input("نام کارمند را وارد کنید: ")
    last_name = input("نام خانوادگی کارمند را وارد کنید: ")
    job_title = input("شغل کارمند را وارد کنید: ")

    salary = random.randint(3000, 8000)
    company.add_employee(Employee(first_name, last_name, job_title, salary))

company.generate_payroll("data.xlsx")
