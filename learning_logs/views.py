from django.shortcuts import render

#importing topics in order to have them render on the page correctly
from .models import Topic
# Create your views here.
# Home page view
def index(request):
    return render(request, 'logs/index.html')

# Topics page
def topics(request):
    '''Importing the topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)
