# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def feesCollections(request):
    context = {
        "collections": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/accounts/fees-collections.html', context)

def addExpenses(request):
    return render(request, 'management/accounts/add-expenses.html')

def addFeesCollection(request):
    return render(request, 'management/accounts/add-fees-collection.html')

def addSalary(request):
    return render(request, 'management/accounts/add-salary.html')

def expenses(request):
    context = {
        "expenses": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/accounts/expenses.html', context)

def salary(request):
    context = {
        "salary": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/accounts/salary.html',context)


def event(request):
    return render(request, 'management/events/event.html')

def addEvent(request):
    return render(request, 'management/events/add-events.html')

def exam(request):    
    context = {
        "exams": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/exam-list/exam.html',context)

def addExam(request):    
    return render(request, 'management/exam-list/add-exam.html')

def editExam(request):    
    return render(request, 'management/exam-list/edit-exam.html')

def fees(request):    
    context = {
        "fees": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/fees/fees.html',context)

def addFees(request):    
    return render(request, 'management/fees/add-fees.html')

def holiday(request):
    context = {
        "holidays": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/holiday/holiday.html',context)

def addHoliday(request):
    return render(request, 'management/holiday/add-holiday.html')

def library(request):    
    context = {
        "library": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/library/library.html',context)

def addBooks(request):    
    return render(request, 'management/library/add-books.html')

def editBooks(request):    
    return render(request, 'management/library/edit-books.html')

def timeTable(request):
    context = {
        "timeTable": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    }
    return render(request, 'management/time-table/time-table.html',context)

def addTimeTable(request):
    return render(request, 'management/time-table/add-time-table.html')

def editTimeTable(request):
    return render(request, 'management/time-table/edit-time-table.html')

