from django.urls import path , include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', views.EmployeesViewSet, basename='employees') #for model viewsets, we don't need to specify the basename if the queryset is defined in the viewset. However, if you want to customize the basename, you can do so by providing it explicitly.
 


urlpatterns = [

    path('students/', views.studentsView),#this will handle the GET and POST requests for the students list and creation
    path('students/<int:pk>/', views.StudentDetailView),#this will handle the GET, PUT, and DELETE requests for a specific student based on their primary key (pk) 


    #path('employees/', views.Employees.as_view()),#this will handle the GET and POST requests for the employees list and creation
    #path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),#this will handle the GET, PUT, and DELETE requests for a specific employee based on their primary key (pk)


    path('', include(router.urls)),#this will handle the GET and POST requests for the employees list and creation using viewsets
]