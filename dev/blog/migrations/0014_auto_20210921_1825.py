# Generated by Django 3.2.7 on 2021-09-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210919_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': "Article's"},
        ),
        migrations.AddField(
            model_name='board',
            name='board_view_counts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='board view count'),
        ),
    ]
