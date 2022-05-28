from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Activity, Comment
from .forms import ActivityForm, CommentForm


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ActivityList(generic.ListView):
    model = Activity
    template_name = "activities.html"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            results_list = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(excerpt__icontains=query)
                )
            return results_list
        else:
            return self.model.objects.all()


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
    success_url = reverse_lazy('activities')

    def test_func(self):
        material = self.get_object()
        return material.athlete == self.request.user


class CreateComment(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "create_comment.html"

    def form_valid(self, form):
        form.instance.athlete = self.request.user
        form.instance.activity = Activity.objects.get(pk=self.kwargs['pk'])
        self.success_url = '/activity_detail/' + str(
            Activity.objects.get(pk=self.kwargs['pk']).pk
            )
        return super().form_valid(form)


class UpdateComment(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    template_name = "update_comment.html"
    fields = ('content',)

    def test_func(self):
        material = self.get_object()
        return material.athlete == self.request.user


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "delete_comment.html"
    success_url = reverse_lazy('activities')

    def test_func(self):
        material = self.get_object()
        return material.athlete == self.request.user
