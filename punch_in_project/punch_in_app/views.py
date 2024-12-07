from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, PunchRecord
from datetime import datetime, timedelta
from django.utils import timezone
import json

# Create your views here.

def index(request):
    return render(request, 'punch_in_app/index.html')

# Punch-in view
def punch_in(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pin = data.get('pin')
        punch_time = data.get('time')

        try:
            employee = Employee.objects.get(four_digit_code=pin)
            
            # Convert to your local timezone (adjust hours as needed)
            punch_datetime = datetime.fromisoformat(punch_time.replace('Z', '+00:00'))
            local_time = punch_datetime - timedelta(hours=8)  # Adjust for PST/PDT
            
            # Get the last punch record and increment its base number
            last_punch = PunchRecord.objects.all().order_by('-punch_id').first()
            next_number = int(last_punch.punch_id.split('-')[0]) + 1
            
            # Create the new punch_id
            punch_id = f"{next_number}-{employee.employee_id}"
            
            # Format time as HH:MM:SS without microseconds
            formatted_time = local_time.strftime('%H:%M:%S')
            print(f"Formatted time: {formatted_time}")  # Debug print
            
            try:
                new_record = PunchRecord.objects.create(
                    punch_id=punch_id,
                    employee=employee,
                    record_date=local_time.date(),
                    punch_in_time=formatted_time,
                    week_id=local_time.strftime('%Y-W%W')
                )
                print(f"Created new record with time: {new_record.punch_in_time}")
                
                return JsonResponse({
                    'success': True,
                    'punch_id': punch_id,
                    'time': formatted_time
                })
            except Exception as e:
                print(f"Error saving record: {str(e)}")
                return JsonResponse({
                    'success': False,
                    'error': f'Error saving record: {str(e)}'
                })
                
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid PIN'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})