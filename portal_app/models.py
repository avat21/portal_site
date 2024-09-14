from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICE = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=False)
    hire_date = models.DateField(blank=False)
    department_id = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    joined_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeaveManagement(models.Model):
    LEAVE_CHOICE = [
        ('Sick Leave', 'Sick Leave'),
        ('Casual Leave', 'Casual Leave'),
        ('Paid Leave', 'Paid Leave'),
        ('Unpaid Leave', 'Unpaid Leave'),
    ]

    LEAVESTATUS_CHOICE = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=False)
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    status = models.CharField(max_length=10, choices=LEAVESTATUS_CHOICE, blank=False)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} requested leave"