from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Activity, Comment


@admin.register(Activity)
class ActivityAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_display = ('title', 'pub_date', 'athlete')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('activity', 'content')
    search_fields = ('athlete', 'name')
