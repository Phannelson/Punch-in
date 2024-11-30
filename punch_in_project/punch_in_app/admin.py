from django.contrib import admin
from .models import Employee, PunchRecord, AbsenceRecord, MilesLog, WeekLog, ChangeLog

admin.site.register(Employee)
admin.site.register(PunchRecord)
admin.site.register(AbsenceRecord)
admin.site.register(MilesLog)
admin.site.register(WeekLog)
admin.site.register(ChangeLog)
