# Generated by Django 4.1.2 on 2022-10-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropCultivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('climate_soil', models.TextField()),
                ('landpreparation', models.TextField()),
                ('varieties', models.TextField()),
                ('season_sowing', models.TextField()),
                ('irrigation', models.TextField()),
                ('interculture', models.TextField()),
                ('harvesting', models.TextField()),
                ('cropimage', models.ImageField(upload_to='static/images/cultivation/')),
            ],
        ),
    ]