# Generated by Django 3.2.7 on 2021-09-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_board_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=550, verbose_name='content'),
        ),
    ]