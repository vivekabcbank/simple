# Generated by Django 3.2.4 on 2023-02-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230221_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=100)),
                ('session_end', models.CharField(max_length=100)),
            ],
        ),
    ]
