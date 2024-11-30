from django.db import models

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    four_digit_code = models.CharField(max_length=4, unique=True)
    employee_role = models.CharField(max_length=50)

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# PunchRecord Model
class PunchRecord(models.Model):
    punch_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    week_id = models.CharField(max_length=50)  # Assuming week_id is stored as a VARCHAR in the database
    date = models.DateField()
    punch_in_time = models.TimeField(null=True, blank=True)
    punch_out_time = models.TimeField(null=True, blank=True)
    break_start_time = models.TimeField(null=True, blank=True)
    break_end_time = models.TimeField(null=True, blank=True)
    receipt_uploaded = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"PunchRecord {self.punch_id} for Employee {self.employee.first_name} {self.employee.last_name}"

# AbsenceRecord Model
class AbsenceRecord(models.Model):
    absence_id = models.CharField(max_length=50, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    absence_type = models.CharField(max_length=50)
    absence_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"AbsenceRecord {self.absence_id} for Employee {self.employee.first_name} {self.employee.last_name}"

# MilesLog Model
class MilesLog(models.Model):
    miles_id = models.CharField(max_length=50, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    week_id = models.CharField(max_length=50)
    miles_date = models.DateField()
    miles_driven = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"MilesLog {self.miles_id} for Employee {self.employee.first_name} {self.employee.last_name}"

# WeekLog Model
class WeekLog(models.Model):
    week_id = models.CharField(max_length=50, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    week_ending_day = models.DateField()
    total_hours = models.FloatField()
    overtime = models.FloatField()
    weighted_hours = models.FloatField()

    def __str__(self):
        return f"WeekLog {self.week_id} for Employee {self.employee.first_name} {self.employee.last_name}"

# ChangeLog Model
class ChangeLog(models.Model):
    change_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=50)
    old_value = models.TextField()
    new_value = models.TextField()
    change_date = models.DateField()
    change_time = models.TimeField()
    changed_by = models.CharField(max_length=50)

    def __str__(self):
        return f"ChangeLog {self.change_id} for Employee {self.employee.first_name} {self.employee.last_name}"
