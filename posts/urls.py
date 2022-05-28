""" Modules """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('activities', views.ActivityList.as_view(), name='activities'),
    path(
        'activity_detail/<int:pk>',
        views.ActivityView.as_view(),
        name='activity_detail'
        ),
    path(
        'create_activity/',
        views.CreateActivity.as_view(),
        name='create_activity'
        ),
    path(
        'update_activity/<int:pk>',
        views.UpdateActivity.as_view(),
        name='update_activity'
        ),
    path(
        'delete_activity/<int:pk>',
        views.DeleteActivity.as_view(),
        name='delete_activity'
        ),
    path(
        'create_comment/<int:pk>',
        views.CreateComment.as_view(),
        name='create_comment'
        ),
    path(
        'update_comment/<int:pk>',
        views.UpdateComment.as_view(),
        name='update_comment'
        ),
    path(
        'delete_comment/<int:pk>',
        views.DeleteComment.as_view(),
        name='delete_comment'
        ),
]
