from django.urls import path
from . import views, hod_views, staff_views, student_views
app_name = "core"
urlpatterns = [
    path('', views.home),
    path('account/login/', views.login, name="account-login"),
    path('account/register/', views.register, name="account-register"),
    path('account/forgot-password/', views.forgotPassword, name="account-forgot-password"),    
    path('error/error-404/', views.error404, name="error-404"),        
    path('blank-page/', views.blankPage, name="blank-page"),        

    path('teacher/dashboard/', staff_views.teacherDashboard, name="teacher-dashboard"),
    path('student/dashboard/', student_views.studentDashboard, name="student-dashboard"),
    path('student/list/', student_views.studentList, name="student-list"),    
    path('student/details/', student_views.studentDetails, name="student-details"),        
    path('student/add/', student_views.studentAdd, name="add-student"),     
    path('student/edit/', student_views.studentEdit, name="edit-student"),            


    path('teacher/list/', staff_views.teacherList, name="teacher-list"),    
    path('teacher/details/', staff_views.teacherDetails, name="teacher-details"),        
    path('teacher/add/', staff_views.teacherAdd, name="add-teacher"),     
    path('teacher/edit/', staff_views.teacherEdit, name="edit-teacher"),    

    path('department/list/', staff_views.departmentList, name="department-list"),    
    path('department/add/', staff_views.departmentAdd, name="add-department"),     
    path('department/edit/', staff_views.departmentEdit, name="edit-department"),                    

    path('subject/list/', staff_views.subjectList, name="subject-list"),    
    path('subject/add/', staff_views.subjectAdd, name="add-subject"),     
    path('subject/edit/', staff_views.subjectEdit, name="edit-subject"),                    
]
