# Generated by Django 3.2.4 on 2023-02-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_attendence_attendencereport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendencereport',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='attendencereport',
            name='student_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='core.student'),
        ),
    ]
