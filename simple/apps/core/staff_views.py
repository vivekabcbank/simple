from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from .models import Couse, Staff, User, Session, \
    Subject, StaffNotification, Staff_Leave, \
    Staff_Feedback, Student, StudentNotification, \
    Student_Feedback, Student_Leave, Attendence, AttendenceReport, \
    StudentResult

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse


@login_required(login_url="core:account-login")
def courseList(request):
    context = {
        "courses": Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/course/courses.html', context)

@login_required(login_url="core:account-login")
def courseAddUpdate(request, id=None):
    if id != None and request.method == "POST":
        course_name = request.POST.get("course_name")

        if Couse.objects.filter(~Q(id=id), Q(name=course_name, isDelete=False)).exists():
            messages.warning(request, "course already taken")
            return redirect(reverse("core:edit-course", kwargs={'id': id}))

        Couse.objects.filter(id=id).update(
            name=course_name
        )
        messages.success(request, "course updates")
        return redirect(reverse("core:course-list"))

    if request.method == "POST":
        course_name = request.POST.get("course_name")
        if Couse.objects.filter(Q(name=course_name, isDelete=False), ~Q(id=id)).exists():
            messages.warning(request, "course already added")
            return redirect(reverse("core:add-course"))
        Couse.objects.create(
            name=course_name
        )
        messages.success(request, "course added")
        return redirect(reverse("core:course-list"))
    return render(request, 'core/course/add-course.html')

@login_required(login_url="core:account-login")
def courseEdit(request, id=None):
    context = {
        "course": Couse.objects.get(id=id)
    }
    return render(request, 'core/course/add-course.html', context)

@login_required(login_url="core:account-login")
def courseDelete(request, id):
    Couse.objects.filter(pk=id).update(
        isDelete=True
    )
    messages.success(request, "Course deleted")
    return redirect(reverse("core:course-list"))


@login_required(login_url='core:account-login')
def staffDashboard(request):
    return render(request, 'core/staff/staff-dashboard.html')


def teacherList(request):
        context = {
            "teachers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        }
        return render(request, 'core/teacher/teachers.html', context)

def teacherDetails(request):
    return render(request, 'core/teacher/teacher-details.html')

def teacherAdd(request):
        return render(request, 'core/teacher/add-teacher.html')

def teacherEdit(request):
    return render(request, 'core/teacher/edit-teacher.html')

@login_required(login_url="core:account-login")
def staffList(request):
    context = {
        "staffs": Staff.objects.filter(admin__isDelete=False)
    }
    return render(request, 'core/staff/staffs.html', context)


@login_required(login_url="core:account-login")
def staffAddUpdate(request, id=None):
    print(request.POST.get("first_name"))
    if id != None and request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")

            address = request.POST.get("address")
            gender = request.POST.get("gender")

            staff = Staff.objects.filter(id=id, isDelete=False).first()
            if User.objects.filter(~Q(id=staff.admin_id), Q(email=email, isDelete=False)).exists():
                messages.warning(request, "email already taken")
                return redirect(reverse("core:edit-staff", kwargs={'id': id}))
            
            if User.objects.filter(~Q(id=staff.admin_id), Q(username=username, isDelete=False)).exists():
                messages.warning(request, "username already taken")
                return redirect(resolve_url("core:edit-staff", id=id))

            User.objects.filter(id=staff.admin_id, isDelete=False).update(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user = User.objects.get(id=staff.admin_id)
            if request.FILES.get("profile_pic", "") != "" and request.FILES["profile_pic"] != None:                
                user.profile_pic = request.FILES["profile_pic"]                
            if request.POST.get("password") != "" and request.POST.get("password") != None:
                user.set_password(request.POST.get("password"))
            user.save()

            Staff.objects.filter(id=id, isDelete=False).update(
                address=address,
                gender=gender,
            )
            messages.success(request, "edited successfully")
            return redirect(resolve_url("core:staff-list"))
        except:
            messages.warning(request, "check all fields")
            return redirect(reverse("core:edit-staff", kwargs={'id': id}))        
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")

            address = request.POST.get("address")
            gender = request.POST.get("gender")

            if User.objects.filter(email=email, isDelete=False).exists():
                messages.warning(request, "email already taken")
                return redirect(reverse("core:add-staff"))

            if User.objects.filter(username=username, isDelete=False).exists():
                messages.warning(request, "username already taken")
                return redirect(reverse("core:add-staff"))

            user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            user_type="2",
                                            email=email,
                                            username=username,
                                            password=password
                                            )
            if request.FILES.get("profile_pic", "") != "" and request.FILES["profile_pic"] != None:
                user.profile_pic = request.FILES["profile_pic"]
                user.save()

            Staff.objects.create(admin=user,
                                 address=address,
                                 gender=gender
                                 )
            messages.success(request, "staff successfully saved")
            return redirect(reverse("core:staff-list"))
        except:
            messages.warning(request, "check all fields")
            return redirect(reverse("core:add-staff"))
    context = {
        "sessions": Session.objects.filter(isDelete=False),
        "courses": Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/staff/add-staff.html', context)

@login_required(login_url="core:account-login")
def staffEdit(request, id):
    context = {
        "staff": Staff.objects.get(pk=id),
        "sessions": Session.objects.filter(isDelete=False),
        "courses": Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/staff/add-staff.html', context)

@login_required(login_url="core:account-login")
def staffDelete(request, id):
    User.objects.filter(pk=id).update(
        isDelete=True
    )
    messages.success(request,"staff deleted")
    return redirect(reverse("core:staff-list"))

@login_required(login_url="core:account-login")
def subjectList(request):
    context = {        
        "subjects" : Subject.objects.filter(isDelete=False)
    }
    return render(request, 'core/subject/subjects.html',context)

@login_required(login_url="core:account-login")
def subjectAddUpdate(request,id=None):
    if id != None and request.method == "POST":
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")
        print(subject_name,course_id,staff_id)

        if Subject.objects.filter(~Q(id=id), Q(name=subject_name, isDelete=False)).exists():
            messages.warning(request, "subject already taken")
            return redirect(reverse("core:edit-subject", kwargs={'id': id}))

        Subject.objects.filter(id=id).update(
            name=subject_name,
            course_id=Couse.objects.get(id=course_id),
            staff_id=Staff.objects.get(id=staff_id),
        )
        messages.success(request, "subject updates")
        return redirect(reverse("core:subject-list"))

    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course_id")
        staff_id = request.POST.get("staff_id")        

        if Subject.objects.filter(Q(name=subject_name, isDelete=False), ~Q(id=id)).exists():
            messages.warning(request, "subject already added")
            return redirect(reverse("core:add-subject"))
        Subject.objects.create(
            name=subject_name,
            course_id=Couse.objects.get(id=course_id),
            staff_id=Staff.objects.get(id=staff_id),
        )
        messages.success(request, "subject added")
        return redirect(reverse("core:subject-list"))
    context = {
        "staffs" : Staff.objects.filter(isDelete=False),
        "courses" : Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/subject/add-subject.html',context)

@login_required(login_url="core:account-login")
def subjectEdit(request, id=None):
    context = {
        "subject": Subject.objects.get(pk=id),
        "staffs" : Staff.objects.filter(isDelete=False),
        "courses" : Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/subject/add-subject.html', context)

@login_required(login_url="core:account-login")
def subjectDelete(request, id):
    Subject.objects.filter(pk=id).update(
        isDelete=True
    )
    messages.success(request,"subject deleted")
    return redirect(reverse("core:subject-list"))


@login_required(login_url="core:account-login")
def sessionList(request):
    context = {        
        "sessions" : Session.objects.filter(isDelete=False)
    }
    return render(request, 'core/session/sessions.html',context)

@login_required(login_url="core:account-login")
def sessionAddUpdate(request,id=None):
    if id != None and request.method == "POST":        
        session_year_start = request.POST.get("session_year_start")
        session_year_end = request.POST.get("session_year_end")

        if Session.objects.filter(~Q(id=id), Q(session_start=session_year_start, session_end=session_year_end, isDelete=False)).exists():
            messages.warning(request, "session already taken")
            return redirect(reverse("core:edit-session", kwargs={'id': id}))

        Session.objects.filter(id=id).update(
            session_start=session_year_start,
            session_end=session_year_end
        )
        messages.success(request, "session updates")
        return redirect(reverse("core:session-list"))

    if request.method == "POST":
        session_year_start = request.POST.get("session_year_start")
        session_year_end = request.POST.get("session_year_end")

        if Session.objects.filter(Q(session_start=session_year_start, session_end=session_year_end, isDelete=False), ~Q(id=id)).exists():
            messages.warning(request, "session already added")
            return redirect(reverse("core:add-session"))
        Session.objects.create(
            session_start=session_year_start,
            session_end=session_year_end
        )
        messages.success(request, "session added")
        return redirect(reverse("core:session-list"))
    context = {
        "staffs" : Staff.objects.filter(isDelete=False),
        "courses" : Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/session/add-session.html',context)

@login_required(login_url="core:account-login")
def sessionEdit(request, id=None):
    context = {
        "session": Session.objects.get(pk=id),
    }
    return render(request, 'core/session/add-session.html', context)

@login_required(login_url="core:account-login")
def sessionDelete(request, id):
    Session.objects.filter(pk=id).update(
        isDelete=True
    )
    messages.success(request,"session deleted")
    return redirect(reverse("core:session-list"))


@login_required(login_url="core:account-login")
def staffSendNotification(request):
    context = {
        "staffs": Staff.objects.filter(admin__isDelete=False),
        "messages": StaffNotification.objects.filter(isDelete=False).order_by("-id")[:5]
    }
    return render(request, "core/staff/send-staff-notification.html", context)

@login_required(login_url="core:account-login")
def staffSaveNotification(request, id=None):
    if request.method == "POST":
        notification = StaffNotification(
            staff_id=Staff.objects.get(pk=id),
            message=request.POST.get("notification-message")                        
        )
        notification.save()
        return redirect(reverse("core:staff-send-notification"))
    return redirect(reverse("core:staff-send-notification"))

@login_required(login_url="core:account-login")
def studentSendNotification(request, id=None):
    if request.method == "POST":
        notification = StudentNotification(
            student_id=Student.objects.get(pk=id),
            message=request.POST.get("notification-message")                        
        )
        notification.save()
        return redirect(reverse("core:student-send-notification"))    
    context = {
        "students": Student.objects.filter(admin__isDelete=False),
        "messages": StudentNotification.objects.filter(isDelete=False).order_by("-id")[:10]
    }
    return render(request, "core/student/send-student-notification.html", context)

@login_required(login_url="core:account-login")
def studentGetNotification(request, id=None):     
    if id != None:
        StudentNotification.objects.filter(id=id).update(
            status = 1
        )
        return redirect(reverse('core:student-get-notification'))
    context = {
        "notifications":StudentNotification.objects.filter(student_id__admin_id=request.user.id, isDelete=False)            
    }
    return render(request, "core/student/notifications.html", context)

@login_required(login_url="core:account-login")
def staffGetNotification(request, id=None):    
    print(StaffNotification.objects.filter(staff_id=Staff.objects.get(admin_id=id), isDelete=False))
    print(StaffNotification.objects.filter(staff_id__admin_id=id, isDelete=False))
    context = {
        "notifications":StaffNotification.objects.filter(staff_id__admin_id=id, isDelete=False)            
    }
    return render(request, "core/staff/notifications.html", context)

@login_required(login_url="core:account-login")
def staffMakrReadNotification(request, id=None):
    notification = StaffNotification.objects.get(id=id)
    notification.status = 1
    notification.save()
    return redirect(reverse('core:staff-get-notification', kwargs={'id': request.user.id}))

@login_required(login_url="core:account-login")
def studentApplyLeave(request):    
    if request.method == "POST":
        leaveDate = request.POST.get("leave_date")
        reason = request.POST.get("reason")        
        Student_Leave.objects.create(
            student_id=Student.objects.get(admin_id=request.user.id),
            message=reason,
            date=leaveDate
        )
        return redirect("/student/dashboard/")
    context = {
        "leaves": Student_Leave.objects.filter(student_id__admin_id=request.user.id, isDelete=False)
    }
    
    return render(request,"core/student/apply-leave.html",context)

@login_required(login_url="core:account-login")
def studentLeaveView(request, id=None, status=None):
    if id != None:
        Student_Leave.objects.filter(pk=id).update(                
            status=1 if eval(status) else 2
            )
        return redirect(reverse('core:student-leave-view'))
    context = {
        "leaves": Student_Leave.objects.filter(isDelete=False)
    }
    return render(request,"core/student/student-leave.html",context)

@login_required(login_url="core:account-login")
def staffApplyLeave(request):
    if request.method == "POST":
        leaveDate = request.POST.get("leave_date")
        reason = request.POST.get("reason")        
        Staff_Leave.objects.create(
            staff_id=Staff.objects.get(admin_id=request.user.id),
            message=reason,
            date=leaveDate
        )
        return redirect(reverse("core:staff-dashboard"))
    context = {
        "leaves": Staff_Leave.objects.filter(staff_id__admin_id=request.user.id, isDelete=False)
    }
    return render(request,"core/staff/apply-leave.html",context)

@login_required(login_url="core:account-login")
def staffLeaveView(request):
    context = {
        "leaves": Staff_Leave.objects.filter(staff_id__admin_id=request.user.id,isDelete=False)
    }
    return render(request,"core/staff/staff-leave.html",context)

@login_required(login_url="core:account-login")
def staffApproveView(request, id=None, status=None):
    Staff_Leave.objects.filter(pk=id).update(
        status=1 if eval(status) else 2
    )
    return redirect(reverse('core:staff-leave-view'))


@login_required(login_url="core:account-login")
def staffDisapproveView(request,id=None):
    Staff_Leave.objects.filter(pk=id).update(
        status=2
    )
    return redirect(reverse('core:staff-leave-view'))


@login_required(login_url="core:account-login")
def studentFeedbackView(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        Student_Feedback.objects.create(
            student_id=Student.objects.get(admin_id=request.user.id),
            feedback=feedback,            
        )
        return redirect(reverse("core:student-feedbacck"))
    context = {
        "feedbacks": Student_Feedback.objects.filter(student_id__admin_id=request.user.id,isDelete=False)
    }
    return render(request,"core/student/feedback.html",context)

@login_required(login_url="core:account-login")
def studentReplayFeedback(request, id=None):
    if request.method == "POST":
        Student_Feedback.objects.filter(isDelete=False, id=id).update(
            feedback_reply=request.POST.get("feedback_reply")
        )
        return redirect(reverse("core:student-feedbacck-view"))
    context = {
        "feedbacks": Student_Feedback.objects.filter(isDelete=False),
    }
    return render(request, "core/student/feedback-replay.html", context)


@login_required(login_url="core:account-login")
def staffFeedbackView(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        Staff_Feedback.objects.create(
            staff_id=Staff.objects.get(admin_id=request.user.id),
            feedback=feedback,            
        )
        return redirect(reverse("core:staff-feedbacck"))
    context = {
        "feedbacks": Staff_Feedback.objects.filter(staff_id__admin_id=request.user.id,isDelete=False)
    }
    return render(request,"core/staff/feedback.html",context)

@login_required(login_url="core:account-login")
def staffReplayFeedback(request, id=None):
    if request.method == "POST":
        Staff_Feedback.objects.filter(isDelete=False, id=id).update(
            feedback_reply=request.POST.get("feedback_reply")
        )
        return redirect(reverse("core:staff-feedbacck-view"))
    context = {
        "feedbacks": Staff_Feedback.objects.filter(isDelete=False),
    }
    return render(request, "core/staff/feedback-replay.html", context)

@login_required(login_url="core:account-login")
def staffTakeAttendence(request):    
    action = request.GET.get("action")
    subject = None
    session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject = Subject.objects.get(pk=request.POST.get("subject_id"))
            session = Session.objects.get(id=request.POST.get("session_id"))

            students = Student.objects.filter(course_id_id=Subject.objects.get(id=subject.id,isDelete=False).course_id_id,
                                              session_id_id=session.id,isDelete=False)
             
    context = {
        "subjects": Subject.objects.filter(staff_id__admin_id=request.user.id,isDelete=False),
        "sessions": Session.objects.filter(isDelete=False),
        "session": session,
        "subject": subject,
        "action":action,
        "students":students,
    }
    return render(request, "core/staff/take-attendence.html", context)


@login_required(login_url="core:account-login")
def staffSaveAttendence(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        session_id = request.POST.get("session_id")
        attendence_date = request.POST.get("attendence_date")
        student_ids = request.POST.getlist("student_ids")
        
        attendence = Attendence.objects.create(
            subject_id=Subject.objects.get(id=subject_id),
            attendence_date=attendence_date,
            sesion_id=Session.objects.get(id=session_id)
        )

        for stud_id in student_ids:
            AttendenceReport.objects.create(
                student_id=Student.objects.get(pk=int(stud_id)),
                attendence_id=attendence
            )
        
    return redirect(reverse("core:staff-take-attendence"))

@login_required(login_url="core:account-login")
def staffViewAttendence(request):
    action = request.GET.get("action")
    subject = None
    session=None
    attendence_date=None
    students = None
    subjects = None
    if action is not None and request.method == "POST":
        subject = Subject.objects.get(pk=request.POST.get("subject_id"))
        session = Session.objects.get(id=request.POST.get("session_id"))
        attendence_date = request.POST.get("attendence_date")

        attendence = Attendence.objects.filter(
            subject_id=subject,
            attendence_date=attendence_date,
            sesion_id=session,
            isDelete=False
        ).first()        
        students = AttendenceReport.objects.filter(
            attendence_id=attendence
        )

    if int(request.user.user_type) == 1:
        subjects = Subject.objects.filter(isDelete=False)
    else:
        subjects = Subject.objects.filter(staff_id__admin_id=request.user.id,isDelete=False)
    context = {
        "subjects": subjects,
        "sessions": Session.objects.filter(isDelete=False),
        "action":action,
        "subject":subject,
        "session":session,
        "attendence_date":attendence_date,
        "students":students,
    }
    return render(request, "core/staff/view-attendence.html", context)


@login_required(login_url="core:account-login")
def studentViewAttendence(request):
    action = request.GET.get("action")
    subject = None
    attendence=None    
    subject_id = request.POST.get("subject_id")

    if action is not None and request.method == "POST":
        subject = Subject.objects.get(pk=subject_id)
        attendence = AttendenceReport.objects.filter(
            student_id=Student.objects.get(admin_id=request.user.id),
            attendence_id__subject_id_id=subject_id,
            isDelete=False,
        )
        print(attendence)

    context = {
        "subjects": Subject.objects.filter(isDelete=False),
        "action":action,
        "subject":subject,   
        "attendence":attendence,
    }
    return render(request, "core/student/view-attendence.html", context)


@login_required(login_url="core:account-login")
def staffAddResult(request):
    action = request.GET.get("action")
    subject = None
    session = None
    students = None
    if action is not None and request.method == "POST":
        subject = Subject.objects.get(pk=request.POST.get("subject_id"))
        session = Session.objects.get(id=request.POST.get("session_id"))
        
        students = Student.objects.filter(
            course_id=subject.course_id,
            isDelete=False
        )
             
    context = {
        "subjects": Subject.objects.filter(staff_id__admin_id=request.user.id,isDelete=False),
        "sessions": Session.objects.filter(isDelete=False),
        "session": session,
        "subject": subject,
        "action":action,
        "students":students,
    }
    return render(request, "core/staff/add-result.html", context)

@login_required(login_url="core:account-login")
def staffSaveResult(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        session_id = request.POST.get("session_id")
        assignment_marks = request.POST.get("assignment_marks")
        exam_marks = request.POST.get("exam_marks")
        student_id = request.POST.get("student_id")

        results = StudentResult.objects.filter(
            student_id=student_id,
            subject_id=subject_id
        )
        if results.exists():
            results.update(
                assignment_mark=int(assignment_marks),
                exam_mark=int(exam_marks),
            )
        else:
            StudentResult.objects.create(
                student_id=Student.objects.get(id=student_id),
                subject_id=Subject.objects.get(pk=subject_id),
                assignment_mark=int(assignment_marks),
                exam_mark=int(exam_marks),
            )

    return redirect(reverse("core:staff-dashboard"))

@login_required(login_url="core:account-login")
def studentViewResult(request):
    context = {
        "results": StudentResult.objects.filter(student_id__admin_id=request.user.id),
    }
    return render(request, "core/student/view-result.html", context)
