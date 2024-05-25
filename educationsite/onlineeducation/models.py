from django.db import models
from django.contrib.auth.models import User

class feedbackModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    number = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name 
    
class Video(models.Model):
    title = models.CharField(max_length=100, null=True)
    video_id = models.IntegerField(unique=True)  
    video_url = models.CharField(max_length=255)
    likes_count = models.IntegerField(default=0) 

    def __str__(self):
        return f"Video {self.video_id}: {self.video_url}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.video_id} - {self.timestamp}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
