from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contect/', views.contect, name='contect'),
    path('courses/', views.courses, name='courses'),
    path('login/', views.login, name='login'),
    path('playlist/', views.playlist, name='playlist'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),
    path('teachers/', views.teachers, name='teachers'),
    path('update/', views.update, name='update'),
    path('watch_video/<int:video_id>/', views.watch_video, name='watch_video'),
    path('loginerror/', views.loginerror, name='loginerror'),
    path('u_must_have_to_login/', views.loginforcourse, name='mustlogin'),
    path('add_comment/<int:video_id>/', views.add_comment, name='add_comment'),
    path('like_video/<int:video_id>/', views.like_video, name='like_video'),
]
