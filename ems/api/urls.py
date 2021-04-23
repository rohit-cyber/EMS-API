from django.urls import path,re_path
from . import views

urlpatterns = [

    #registration API
    path('registerapi/',views.RegistrationAPI.as_view()),

    #Login API
    path('loginapi/',views.LoginApiView.as_view()),
    path('logout/',views.LogoutView.as_view()),

    #Profile API
    re_path(r'^profileapi/',views.ProfileAPI.as_view()),
    
]