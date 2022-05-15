from django.urls import path
from . import views


urlpatterns = [
    path('', views.ActivityList.as_view(), name='activity_list'),
    path('activities/<int:pk>', views.ActivityView.as_view(), name='activity_detail'),
]
