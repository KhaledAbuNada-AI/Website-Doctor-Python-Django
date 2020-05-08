# Generated by Django 3.0.3 on 2020-04-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_remove_profile_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type_of_person',
        ),
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت الانضمام :'),
        ),
    ]