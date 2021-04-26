from django.urls import path,include
from . import views

urlpatterns = [

    # add Student url
    path('addsapi', views.AddStudentAPI.as_view()),

    # add Guardian url
    path('addgapi', views.AddGuardianAPI.as_view()),

    # list all Students with Guardians url
    path('swgapi', views.StudentWithGuardianAPI.as_view()),

    # Return all active Students url
    path('asapi', views.ActiveStudentsAPI.as_view()),

    # Return all student who joined this year API
    path('dsapi', views.JoinDateStudentAPI.as_view()),
    
]