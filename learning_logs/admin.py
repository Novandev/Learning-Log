from django.contrib import admin

# Register your models here.

#IMPORT Topic model from models so it can be registered with the admin site for tracking
from learning_logs.models import Topic

admin.site.register(Topic)
