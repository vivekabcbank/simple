# Generated by Django 3.2.4 on 2023-02-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='couse',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
