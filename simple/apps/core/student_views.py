from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from .models import Session, Couse, Student, User
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q


@login_required(login_url='core:account-login')
def studentDashboard(request):
    return render(request, 'core/student/student-dashboard.html')

@login_required(login_url="core:account-login")
def studentList(request):
    context = {
        "students": Student.objects.filter(admin__isDelete=False)
    }
    return render(request, 'core/student/students.html', context)


def studentDetails(request):
    return render(request, 'core/student/student-details.html')


@login_required(login_url="core:account-login")
def studentAddUpdate(request, id=None):
    print("tim add student",id, request.method)
    print(request.POST.get("first_name"))
    print(request.GET.get("first_name"))
    if id != None and request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")

            address = request.POST.get("address")
            gender = request.POST.get("gender")
            course_id = request.POST.get("course_id")
            session_year_id = request.POST.get("session_year_id")

            student = Student.objects.filter(id=id, isDelete=False).first()
            if User.objects.filter(~Q(id=student.admin_id), Q(email=email, isDelete=False)).exists():
                messages.warning(request, "email already taken")
                return redirect(reverse("core:edit-student", kwargs={'id': id}))
            
            if User.objects.filter(~Q(id=student.admin_id), Q(username=username, isDelete=False)).exists():
                messages.warning(request, "username already taken")
                return redirect(resolve_url("core:edit-student", id=id))

            User.objects.filter(id=student.admin_id, isDelete=False).update(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user = User.objects.get(id=student.admin_id)
            if request.FILES.get("profile_pic", "") != "" and request.FILES["profile_pic"] != None:                
                user.profile_pic = request.FILES["profile_pic"]                
            if request.POST.get("password") != "" and request.POST.get("password") != None:
                user.set_password(request.POST.get("password"))
            user.save()

            Student.objects.filter(id=id, isDelete=False).update(
                address=address,
                gender=gender,
                course_id=Couse.objects.get(id=course_id),
                session_id=Session.objects.get(id=session_year_id)
            )
            messages.success(request, "edited successfully")
            return redirect(resolve_url("core:student-list"))
        except:
            messages.warning(request, "check all fields")
            return redirect(reverse("core:edit-student", kwargs={'id': id}))        
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")

            address = request.POST.get("address")
            gender = request.POST.get("gender")
            course_id = request.POST.get("course_id")
            session_year_id = request.POST.get("session_year_id")

            if User.objects.filter(email=email, isDelete=False).exists():
                messages.warning(request, "email already taken")
                return redirect(reverse("core:add-student"))

            if User.objects.filter(username=username, isDelete=False).exists():
                messages.warning(request, "username already taken")
                return redirect(reverse("core:add-student"))

            user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            user_type="3",
                                            email=email,
                                            username=username,
                                            password=password
                                            )
            if request.FILES.get("profile_pic", "") != "" and request.FILES["profile_pic"] != None:
                user.profile_pic = request.FILES["profile_pic"]
                user.save()

            Student.objects.create(admin=user,
                                   address=address,
                                   gender=gender,
                                   course_id=Couse.objects.get(id=course_id),
                                   session_id=Session.objects.get(id=session_year_id)
                                   )
            messages.success(request, "student successfully saved")
            return redirect(reverse("core:student-list"))
        except:
            messages.warning(request, "check all fields")
            return redirect(reverse("core:add-student"))
    context = {
        "sessions": Session.objects.filter(isDelete=False),
        "courses": Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/student/add-student.html', context)

@login_required(login_url="core:account-login")
def studentEdit(request, id):
    context = {
        "student": Student.objects.get(pk=id),
        "sessions": Session.objects.filter(isDelete=False),
        "courses": Couse.objects.filter(isDelete=False)
    }
    return render(request, 'core/student/add-student.html', context)

@login_required(login_url="core:account-login")
def studentDelete(request, id):
    User.objects.filter(pk=id).update(
        isDelete=True
    )
    messages.success(request,"Student deleted")
    return redirect(reverse("core:student-list"))
