# Generated by Django 3.0.3 on 2020-04-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='google',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Google'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Twitter'),
        ),
    ]
