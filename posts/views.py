from django.shortcuts import render
from django.views import generic
from .models import Activity
from .forms import ActivityForm

# Create your views here.

# class IndexView(generic.View):
#     model = Activity
#     template_name = "index.html"


class ActivityList(generic.ListView):
    model = Activity
    template_name = "index.html"
    paginate_by = 6


class ActivityView(generic.DetailView):
    model = Activity
    template_name = "activity_detail.html"


class CreateActivity(generic.CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "create_activity.html"


class UpdateActivity(generic.UpdateView):
    model = Activity
    template_name = "update_activity.html"
    fields = ('title', 'content', 'excerpt')


class DeleteActivity(generic.DeleteView):
    model = Activity
    template_name = "delete_activity.html"