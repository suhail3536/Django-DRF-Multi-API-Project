from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.StudentsView),
    path('students/<int:pk>/',views.studentDetailView),

    
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),


      
    path('workers/', views.Workers.as_view()),
    path('workers/<int:pk>/',views.WorkerDetail.as_view()),

]