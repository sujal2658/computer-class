from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .forms import feedbackForm
from .models import Video, Comment,Like

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'home.html', {'username': username})


def about(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'about.html', {'username': username})

def contect(request):
    form = feedbackForm()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
    
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'contact.html', {'form':form, 'username': username})

@login_required(login_url='mustlogin')
def courses(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'courses.html', {'username': username})

def playlist(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'playlist.html', {'username': username})

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'profile.html', {'username': username})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('pass') 
        Conpass = request.POST.get('c_pass')
        
        if password != Conpass:
            return HttpResponse('password does not match')
        elif User.objects.filter(username__startswith=username):
            return HttpResponse('username is already taken please go back and create new one..')
        else:
            my_user = User.objects.create_user(username=username, email=email, password=Conpass) 
            my_user.save()
            return redirect('login')
    if request.user.is_authenticated:
        uusername = request.user.username
    else:
        uusername = "User"
    return render(request, 'register.html', {'username': uusername})


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('pass')
        user_1 = authenticate(request, username=uname, password=password)
        if user_1 is not None:
            auth_login(request, user_1)
            return redirect('home')
        else:
            return redirect('loginerror')
        
    if request.user.is_authenticated:
        uusername = request.user.username
    else:
        uusername = "User"
    return render(request, 'login.html', {'username': uusername})

def Logout(request):
    logout(request)
    return redirect('login')

def teacher_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'teacher_profile.html', {'username': username})

def teachers(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'teachers.html', {'username': username})

def update(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'home.html', {'username': username})

def watch_video(request, video_id):
    # Get the authenticated user's username or set it to "User" if not authenticated
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"

    # Retrieve the video object from the database based on the video_id
    video = get_object_or_404(Video, video_id=video_id)
    
    # Print the video ID for debugging
    print("Video ID:", video_id)
    
    comments = Comment.objects.filter(video=video)
    
    # Pass the username, video_url, and video_id to the template context
    context = {
        'username': username,
        'video_url': video.video_url,
        'comments': comments,
        'video': video,  # Pass the 'video' object itself instead of just the 'video_id'
    }

    return render(request, 'watch-video.html', context)


@login_required
def add_comment(request, video_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment_box')

        # Retrieve the video object based on the provided video_id
        video = get_object_or_404(Video, id=video_id)

        # Create the comment with the associated video
        Comment.objects.create(user=request.user, video=video, text=comment_text)
        
        # Redirect back to the watch video page
        return redirect('watch_video', video_id=video_id)
    else:
        # If it's not a POST request, redirect to the login page
        return redirect('login')


# views for error templates:

def loginerror(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'errortemps/loginerror.html', {'username': username})

def loginforcourse(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('pass')
        user_1 = authenticate(request, username=uname, password=password)
        if user_1 is not None:
            auth_login(request, user_1)
            return redirect('courses')
        else:
            return redirect('loginerror')
    
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "User"
    return render(request, 'errortemps/loginmust.html', {'username': username})

# like video

def like_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    user = request.user
    
    # Check if the user has already liked the video
    if Like.objects.filter(user=user, video=video).exists():
        # User has already liked the video, unlike it
        Like.objects.filter(user=user, video=video).delete()
        video.likes_count -= 1
        video.save()
    else:
        # User is liking the video for the first time
        Like.objects.create(user=user, video=video)
        video.likes_count += 1
        video.save()
    
    return redirect('watch_video', video_id=video_id)



