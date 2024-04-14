# Generated by Django 3.2.7 on 2021-09-22 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_board_last_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleEditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited_by_username', models.CharField(blank=True, max_length=255, null=True)),
                ('edited_from', models.TextField(blank=True, max_length=450, null=True)),
                ('edited_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('edited_to', models.TextField(blank=True, max_length=450, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
