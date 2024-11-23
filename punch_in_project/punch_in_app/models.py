from django.db import models

# Create your models here.

class PinEntry(models.Model):
    from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    four_digit_code = models.CharField(max_length=4, unique=True)  # Assuming 4-digit PIN
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PunchRecord(models.Model):
    punch_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    week_id = models.IntegerField()  # Assuming you'll add a reference to a WeekLog
    date = models.DateField()
    punch_in_time = models.TimeField(null=True, blank=True)
    punch_out_time = models.TimeField(null=True, blank=True)
    break_start_time = models.TimeField(null=True, blank=True)
    break_end_time = models.TimeField(null=True, blank=True)
    receipt_uploaded = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
