from django.contrib import admin
from .models import Activity
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Activity)
class ActivityAdmin(SummernoteModelAdmin):

    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_display = ('title', 'pub_date', 'athlete')
