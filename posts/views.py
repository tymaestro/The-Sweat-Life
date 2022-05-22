from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Activity, Comment
from .forms import ActivityForm, CommentForm

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


class CreateActivity(LoginRequiredMixin, generic.CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = "create_activity.html"

    def form_valid(self, form):
        form.instance.athlete = self.request.user
        return super().form_valid(form)


class UpdateActivity(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Activity
    template_name = "update_activity.html"
    fields = ('title', 'content', 'excerpt')

    def test_func(self):
        material = self.get_object()
        return material.athlete == self.request.user


class DeleteActivity(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Activity
    template_name = "delete_activity.html"
    success_url = reverse_lazy('activity_list')

    def test_func(self):
        material = self.get_object()
        return material.athlete == self.request.user


# class CreateComment(LoginRequiredMixin, generic.CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = "create_activity.html"

#     def form_valid(self, form):
#         form.instance.athlete = self.request.user
#         return super().form_valid(form)
