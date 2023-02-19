from django.shortcuts import render, redirect

def teacherDashboard(request):
    return render(request, 'core/teacher/teacher-dashboard.html')

def teacherList(request):
    context = {
        "teachers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, 'core/teacher/teachers.html',context)

def teacherDetails(request):
    return render(request, 'core/teacher/teacher-details.html')

def teacherAdd(request):
    return render(request, 'core/teacher/add-teacher.html')

def teacherEdit(request):
    return render(request, 'core/teacher/edit-teacher.html')


def departmentList(request):
    context = {
        "departments" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, 'core/department/departments.html',context)

def departmentAdd(request):
    return render(request, 'core/department/add-department.html')

def departmentEdit(request):
    return render(request, 'core/department/edit-department.html')

def subjectList(request):
    context = {
        "subjects" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, 'core/subject/subjects.html',context)

def subjectAdd(request):
    return render(request, 'core/subject/add-subject.html')

def subjectEdit(request):
    return render(request, 'core/subject/edit-subject.html')