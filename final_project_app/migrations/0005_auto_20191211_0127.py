# Generated by Django 3.0 on 2019-12-11 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('final_project_app', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]