from django.urls import path
from . import views, hod_views, staff_views, student_views
app_name = "core"
urlpatterns = [
    path('dashboard/', views.home, name="admin-dashboard"),
    path('account/login/', views.doLogin, name="account-login"),
    path('account/register/', views.register, name="account-register"),
    path('account/logout/', views.doLogout, name="account-logout"),
    path('account/forgot-password/', views.forgotPassword, name="account-forgot-password"),    
    path('error/error-404/', views.error404, name="error-404"),        
    path('blank-page/', views.blankPage, name="blank-page"),            
    
    path('student/details/', student_views.studentDetails, name="student-details"),        

    path('student/dashboard/', student_views.studentDashboard, name="student-dashboard"),
    path('student/list/', student_views.studentList, name="student-list"),    
    path('student/add/', student_views.studentAddUpdate, name="add-student"),
    path('student/update/<int:id>', student_views.studentAddUpdate, name="update-student"),     
    path('student/edit/<int:id>', student_views.studentEdit, name="edit-student"),
    path('student/delete/<int:id>', student_views.studentDelete, name="delete-student"),

    path('course/list/', staff_views.courseList, name="course-list"),    
    path('course/add/', staff_views.courseAddUpdate, name="add-course"),
    path('course/update/<int:id>', staff_views.courseAddUpdate, name="update-course"),     
    path('course/edit/<int:id>', staff_views.courseEdit, name="edit-course"),
    path('course/delete/<int:id>', staff_views.courseDelete, name="delete-course"),

    path('staff/dashboard/', staff_views.staffDashboard, name="staff-dashboard"),
    path('staff/list/', staff_views.staffList, name="staff-list"),    
    path('staff/add/', staff_views.staffAddUpdate, name="add-staff"),
    path('staff/update/<int:id>', staff_views.staffAddUpdate, name="update-staff"),     
    path('staff/edit/<int:id>', staff_views.staffEdit, name="edit-staff"),
    path('staff/delete/<int:id>', staff_views.staffDelete, name="delete-staff"),

    path('teacher/list/', staff_views.teacherList, name="teacher-list"),    
    path('teacher/details/', staff_views.teacherDetails, name="teacher-details"),        
    path('teacher/add/', staff_views.teacherAdd, name="add-teacher"),     
    path('teacher/edit/', staff_views.teacherEdit, name="edit-teacher"),    

    path('subject/list/', staff_views.subjectList, name="subject-list"),    
    path('subject/add/', staff_views.subjectAddUpdate, name="add-subject"),
    path('subject/update/<int:id>', staff_views.subjectAddUpdate, name="update-subject"),     
    path('subject/edit/<int:id>', staff_views.subjectEdit, name="edit-subject"),
    path('subject/delete/<int:id>', staff_views.subjectDelete, name="delete-subject"),

    path('session/list/', staff_views.sessionList, name="session-list"),    
    path('session/add/', staff_views.sessionAddUpdate, name="add-session"),
    path('session/update/<int:id>', staff_views.sessionAddUpdate, name="update-session"),     
    path('session/edit/<int:id>', staff_views.sessionEdit, name="edit-session"),
    path('session/delete/<int:id>', staff_views.sessionDelete, name="delete-session"),

    path('profile/', views.profile, name="profile"),   
    path('profile/update/', views.profileUpdate, name="profile-update"),                    

    path('staff/send_notification/', staff_views.staffSendNotification, name="staff-send-notification"),    
    path('staff/save_notification/<int:id>', staff_views.staffSaveNotification, name="staff-save-notification"),    
    path('staff/get_notification/<int:id>', staff_views.staffGetNotification, name="staff-get-notification"),    
    path('staff/notification_mark_as_done/<int:id>', staff_views.staffMakrReadNotification, name="staff-notification-mark-as-done"),

    path('staff/apply-leave/', staff_views.staffApplyLeave, name="staff-apply-leave"),
    path('staff/leave-view/', staff_views.staffLeaveView, name="staff-leave-view"),
    path('staff/approve-leave/<int:id>/<str:status>/', staff_views.staffApproveView, name="staff-approve-leave"),
    path('staff/feedbacck/', staff_views.staffFeedbackView, name="staff-feedbacck"),
    path('staff/feedbacck-view/', staff_views.staffReplayFeedback, name="staff-feedbacck-view"),
    path('staff/feedbacck-replay/<int:id>', staff_views.staffReplayFeedback, name="staff-feedbacck-replay"),

    path('student/send_notification/', staff_views.studentSendNotification, name="student-send-notification"),    
    path('student/save_notification/<int:id>', staff_views.studentSendNotification, name="student-save-notification"),    
    path('student/get_notification/', staff_views.studentGetNotification, name="student-get-notification"),    
    path('student/notification_mark_as_done/<int:id>', staff_views.studentGetNotification, name="student-notification-mark-as-done"),

    path('student/feedbacck/', staff_views.studentFeedbackView, name="student-feedbacck"),
    path('student/feedbacck-view/', staff_views.studentReplayFeedback, name="student-feedbacck-view"),
    path('student/feedbacck-replay/<int:id>', staff_views.studentReplayFeedback, name="student-feedbacck-replay"),

    path('student/apply-leave/', staff_views.studentApplyLeave, name="student-apply-leave"),
    path('student/leave-view/', staff_views.studentLeaveView, name="student-leave-view"),
    path('student/approve-leave/<int:id>/<str:status>/', staff_views.studentLeaveView, name="student-approve-leave"),

    path('staff/take-attendence/', staff_views.staffTakeAttendence, name="staff-take-attendence"),
    path('staff/save-attendence/', staff_views.staffSaveAttendence, name="staff-save-attendence"),
    path('staff/view-attendence/', staff_views.staffViewAttendence, name="staff-view-attendence"),
    
    path('student/view-attendence/', staff_views.studentViewAttendence, name="student-view-attendence"),
    
    path('staff/add-result/', staff_views.staffAddResult, name="staff-add-result"),
    path('staff/save-result/', staff_views.staffSaveResult, name="staff-save-result"),
    path('student/view-result/', staff_views.studentViewResult, name="student-view-result"),
]
