from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("content/<str:id>",views.content,name="content"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    
    
]
