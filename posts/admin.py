from django.contrib import admin
from .models import Activity
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Activity)
class ActivityAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
