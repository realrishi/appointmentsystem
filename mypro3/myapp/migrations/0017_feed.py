# Generated by Django 2.0.7 on 2019-06-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20180808_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('fbto', models.CharField(max_length=200)),
                ('fbdesc', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='date published')),
                ('time', models.TimeField(verbose_name='time published')),
            ],
        ),
    ]
