from django.shortcuts import render
from django.views import generic
from .models import Activity

# Create your views here.


class ActivityList(generic.ListView):
    model = Activity
    template_name = "index.html"


class ActivityView(generic.DetailView):
    model = Activity
    template_name = "activity_detail.html"
