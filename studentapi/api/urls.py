from django.urls import path,include
from . import views

urlpatterns = [
    #test
    path('test',views.test),


    # student form for registration
    path('student',views.student_form),


    # send mail url
    path('particular_send_mail/<int:id>',views.particular_send_mail,name='particular_send_mail'),

    # add Student url
    path('add_student_api/', views.AddStudentAPI.as_view(),name='add_student_api'),

    # add Guardian url
    path('add_guardian_api/', views.AddGuardianAPI.as_view()),

    # list and add all Students with Guardians url
    path('student_with_guardian_api/', views.StudentWithGuardianAPI.as_view()),

    # Return all active Students url
    path('active_student_api/', views.ActiveStudentsAPI.as_view()),

    # Return all evaluation pass/fail  Students url
    path('student_evaluation_api/', views.EvalStudentAPI.as_view()),

    # Sort student API
    path('student_sort_api/', views.SortStudentAPI.as_view()),

    # Return all student who joined this year API
    path('date_api/', views.JoinDateStudentAPI.as_view()),

    # Student Detail and Delete API
    path('student_api/', views.StudentDetailDeleteAPI.as_view()),
    path('student_api/<int:pk>', views.StudentDetailDeleteAPI.as_view()),

    # Student list with pagination
    path('student_list_api/', views.StudentList.as_view()),

    #Login API
    path('loginapi/',views.LoginApiView.as_view()), #apply in postman in POST
    path('logout/',views.LogoutView.as_view()), #apply in postman in POST
]


