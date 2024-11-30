from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from datetime import datetime
import json

# Create your views here.

def index(request):
    return render(request, 'punch_in_app/index.html')

# Punch-in view
def punch_in(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pin = data.get('pin')

        try:
            employee = Employee.objects.get(four_digit_code=pin)
            # Here, we're just validating the PIN, not yet recording any punch-in time
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid PIN'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})