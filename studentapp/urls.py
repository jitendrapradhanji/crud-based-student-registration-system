from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('studentdetail/', views.StudentdetailView, name="studentdetail"),
    path('studentregistration/', views.StudentregistrationView,
         name='studentregistration'),
    path('delete/<id>/', views.DeleteView, name='delete'),
    path('update/<id>/', views.UpdateView, name='update'),
    path('contact/', views.ContactView, name='contact'),
    path('about/', views.AboutView, name='about'),
    path('register/', views.RegisterView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('welcome/', views.WelcomeView, name="welcome"),

]

# Login Page User Details

# Ramesh
# std123456


# manoj123
# stud123456
