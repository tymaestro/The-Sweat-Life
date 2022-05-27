# Generated by Django 3.2.13 on 2022-05-27 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AlterField(
            model_name='activity',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.activity'),
        ),
    ]
