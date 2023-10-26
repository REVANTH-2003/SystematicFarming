# Generated by Django 4.2 on 2023-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_remove_user_is_authenticated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]