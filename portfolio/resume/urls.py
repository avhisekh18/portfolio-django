
from django.urls import path
from . import views
urlpatterns = [
   path('', views.index,name="index"),
   path('home/',views.home, name="home"),
   path('about/',views.about, name="about"),
   path('projects/',views.project, name="projects"),
   path('contact/',views.contact, name="contact"),
   path('skills/',views.skills, name="skills"),
   path('register/',views.register_user,name="register"),
   path('login/',views.login_user,name="login")
   
]
