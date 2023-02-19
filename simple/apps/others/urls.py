from django.urls import path
from . import views
app_name = "others"
urlpatterns = [
    path('hostel/', views.hostel, name="hostel"),
    path('hostel/add-room/', views.addRoom, name="add-room"),    
    path('hostel/edit-room/', views.editRoom, name="edit-room"),

    path('sports/', views.sports, name="sports"),
    path('sports/add-sports/', views.addSport, name="add-sports"),    
    path('sports/edit-sports/', views.editSport, name="edit-sports"),

    path('transport/', views.transport, name="transport"),
    path('transport/add-transport/', views.addTransport, name="add-transport"),    
    path('transport/edit-transport/', views.editTransport, name="edit-transport"),
]
