# Generated by Django 3.2.7 on 2021-10-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0003_alter_invitation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_token',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Token'),
        ),
    ]
