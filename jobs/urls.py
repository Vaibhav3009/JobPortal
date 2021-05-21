from django.urls import path
from . import views
 
app_name = 'jobs'
 
urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.jobsresult, name='result'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('profiledata/', views.profiledata, name='profiledata'),
    # path('import/', views.import_view, name='import'),
    ]