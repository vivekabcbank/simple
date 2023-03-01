from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import User, Staff, Student, Couse, Subject
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse("core:account-login"))
        print(form.errors, len(form.errors))
        form = SignUpForm()
        return render(request, 'authentication/register.html', {"form": form})
    form = SignUpForm()
    return render(request, 'authentication/register.html', {"form": form})


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def doLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        # user = EmailBackend.authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == "1":
                return redirect("core:admin-dashboard")
            if user_type == "2":
                return redirect(reverse('core:staff-dashboard'))
            if user_type == "3":
                return redirect(reverse('core:student-dashboard'))
            else:
                messages.error(request, "User type not exists")
                return redirect(reverse('core:account-login'))
        else:
            messages.error(request, "Invalid credentials, try Again")
            return redirect(reverse('core:account-login'))
    elif request.user.id:
        user_type = User.objects.get(id=request.user.id).user_type
        if user_type == "1":
            return redirect("core:admin-dashboard")                
        if user_type == "2":
            return redirect(reverse('core:staff-dashboard'))                
        if user_type == "3":
            return redirect(reverse('core:student-dashboard'))                
        else:
            messages.error(request, "User type not exists")
            return redirect(reverse('core:account-login'))             
    else:
        return render(request, 'authentication/login.html')


def doLogout(request):
    logout(request)
    return redirect("core:account-login")


@login_required(login_url='core:account-login')
def home(request):    
    staff_count = Staff.objects.filter(isDelete=False).count()
    student_count = Student.objects.filter(isDelete=False).count()
    course_count = Couse.objects.filter(isDelete=False).count()
    subject_count = Subject.objects.filter(isDelete=False).count()

    student_gender_male = Student.objects.filter(gender="Male", isDelete=False).count()
    student_gender_female = Student.objects.filter(gender="Female", isDelete=False).count()
    student_gender_other = Student.objects.filter(gender="Others", isDelete=False).count()

    context = {
        "staff_count": staff_count,
        "student_count": student_count,
        "course_count":course_count,
        "subject_count":subject_count,
        "student_gender_male":student_gender_male,
        "student_gender_female":student_gender_female,
        "student_gender_other":student_gender_other,
    }
    return render(request, 'core/index.html', context)


def forgotPassword(request):
    return render(request, 'authentication/forgot-password.html')


def error404(request):
    return render(request, 'authentication/error-404.html')


def blankPage(request):
    return render(request, 'blank-page.html')


@login_required(login_url="core:account-login")
def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        "user": user
    }
    return render(request, 'core/profile.html', context)

@login_required(login_url="core:account-login")
def profileUpdate(request):
    if request.method == "POST":
        try:
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST.get("first_name", "")
            user.last_name = request.POST.get("last_name", "")
            if request.FILES.get("profile_pic", "") != "" and request.FILES["profile_pic"] != None:
                user.profile_pic = request.FILES["profile_pic"]
            if request.POST.get("password") != "" and request.POST.get("password") != None:
                user.set_password(request.POST.get("password"))
            user.save()
            messages.success(request, "Your profile updated successfully")            
            return redirect(reverse("core:profile"))
            # return redirect("/")
        except:
            messages.warning(request, "Failed to update your profile")
            return redirect(reverse("core:profile"))