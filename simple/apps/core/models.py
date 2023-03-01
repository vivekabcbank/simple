from django.db import models
from django.contrib.auth .models import AbstractUser
from django.utils.timezone import datetime

class User(AbstractUser):
    USER = [
        ("1", 'HOD'),
        ("2", 'STAFF'),
        ("3", 'STUDENT'),
    ]
    user_type = models.CharField(max_length=50, choices=USER, default="1")
    profile_pic = models.ImageField(upload_to='media/profile_pic', default='')
    isDelete = models.BooleanField(default=False)

class Couse(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Session(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.session_start }-{self.session_end }"

class Student(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Couse, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.admin.first_name } {self.admin.last_name }"

class Staff(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.admin.first_name } {self.admin.last_name }"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.ForeignKey(Couse, on_delete=models.DO_NOTHING)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class StaffNotification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.staff_id.admin.username
    

class StudentNotification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id.admin.username

class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.CharField(max_length=100)
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff_id.admin.first_name} {self.staff_id.admin.last_name}"
    

class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff_id.admin.first_name} {self.staff_id.admin.last_name}"
    

class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.admin.first_name} {self.student_id.admin.last_name}"
        
    
class Student_Leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.CharField(max_length=100)
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.admin.first_name} {self.student_id.admin.last_name}"

class Attendence(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendence_date = models.DateField()
    sesion_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject_id.name}"

class AttendenceReport(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING, blank=True, default=None)
    attendence_id = models.ForeignKey(Attendence, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.admin.username}"
    

class StudentResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.admin.username}"
    
    def getResult(self):
        return "Pass" if (self.assignment_mark+self.exam_mark) >=40 else "Fail"
    
    
        