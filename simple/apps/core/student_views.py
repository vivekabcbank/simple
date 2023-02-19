from django.shortcuts import render, redirect

def studentDashboard(request):
    return render(request, 'core/student/student-dashboard.html')


def studentList(request):
    context = {
        "students" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, 'core/student/students.html',context)

def studentDetails(request):
    return render(request, 'core/student/student-details.html')

def studentAdd(request):
    return render(request, 'core/student/add-student.html')

def studentEdit(request):
    return render(request, 'core/student/edit-student.html')

