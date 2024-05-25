from django.contrib import admin
from .models import feedbackModel, Video, Comment, Like

admin.site.register(feedbackModel)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
