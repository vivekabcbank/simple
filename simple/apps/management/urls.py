from django.urls import path
from . import views
app_name = "management"
urlpatterns = [
    path('management/accounts/fees-collections/', views.feesCollections, name="fees-collections"),
    path('management/accounts/add-expenses/', views.addExpenses, name="add-expenses"),        
    path('management/accounts/add-fees-collection/', views.addFeesCollection, name="add-fees-collection"),
    path('management/accounts/add-salary/', views.addSalary, name="add-salary"),
    path('management/accounts/expenses/', views.expenses, name="expenses"),
    path('management/accounts/salary/', views.salary, name="salary"),

    path('management/event/', views.event, name="event"),
    path('management/exam/', views.exam, name="exam"),        
    path('management/fees/', views.fees, name="fees"),
    path('management/holiday/', views.holiday, name="holiday"),
    path('management/library/', views.library, name="library"),
    path('management/time-table/', views.timeTable, name="time-table"),

    path('management/event/add-events/', views.addEvent, name="add-events"),
    path('management/exam/add-exam/', views.addExam, name="add-exam"),        
    path('management/exam/edit-exam/', views.editExam, name="edit-exam"),
    path('management/fees/add-fees/', views.addFees, name="add-fees"),
    path('management/holiday/add-holiday/', views.addHoliday, name="add-holiday"),
    path('management/library/add-books/', views.addBooks, name="add-books"),
    path('management/library/edit-books/', views.editBooks, name="edit-books"),
    path('management/time-table/add-time-table/', views.addTimeTable, name="add-time-table"),
    path('management/time-table/edit-time-table/', views.editTimeTable, name="edit-time-table"),
]
