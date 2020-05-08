# Generated by Django 3.0.3 on 2020-04-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200407_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_new',
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('أسنان', 'أسنان'), ('عظام', 'عظام')], max_length=50, null=True, verbose_name='دكتور :'),
        ),
    ]
