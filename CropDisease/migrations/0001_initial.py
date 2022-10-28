# Generated by Django 4.1.2 on 2022-10-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropname', models.CharField(max_length=50)),
                ('diseasename', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('diseaseimage', models.ImageField(upload_to='static/images/disease/')),
                ('identification', models.TextField()),
                ('prevention', models.TextField()),
                ('treatment', models.TextField()),
            ],
        ),
    ]