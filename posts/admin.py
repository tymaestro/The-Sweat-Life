from django.contrib import admin
from .models import Activity, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Activity)
class ActivityAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_display = ('title', 'pub_date', 'athlete')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('athlete', 'content')
    search_fields = ('athlete', 'name')
