from django.shortcuts import render
from django.views import generic
from .models import Activity
from .forms import ActivityForm

# Create your views here.


class ActivityList(generic.ListView):
    model = Activity
    template_name = "index.html"


class ActivityView(generic.DetailView):
    model = Activity
    template_name = "activity_detail.html"


class CreateActivity(generic.CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "create_activity.html"
    # fields = ('title', 'athlete', 'content', 'excerpt')