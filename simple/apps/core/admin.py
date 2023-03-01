from django.contrib import admin

from .models import User, Couse, Session, Student, Staff, Subject, \
    Student_Leave, StaffNotification, Staff_Leave, Staff_Feedback, \
    Attendence, AttendenceReport, StudentResult, StudentNotification, Student_Feedback

class UserAdmin(admin.ModelAdmin):
    list_display = ("username","user_type",)

admin.site.register(User,UserAdmin)

class CouseAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Couse,CouseAdmin)

admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)

class StaffNotificationAdmin(admin.ModelAdmin):
    list_display = ("get_staff","status",)
    
    def get_staff(self, obj):
        return obj.staff_id.admin    
    get_staff.username = 'Staff'

admin.site.register(StaffNotification,StaffNotificationAdmin)
admin.site.register(Staff_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(StudentNotification)
admin.site.register(Student_Feedback)
admin.site.register(Student_Leave)
admin.site.register(Attendence)
admin.site.register(AttendenceReport)
admin.site.register(StudentResult)



