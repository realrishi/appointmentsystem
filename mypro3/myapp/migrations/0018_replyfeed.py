# Generated by Django 2.0.7 on 2019-06-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replyfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('replyfto', models.CharField(max_length=200)),
                ('replyfdesc', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='date published')),
                ('time', models.TimeField(verbose_name='time published')),
            ],
        ),
    ]
