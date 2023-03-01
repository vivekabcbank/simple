# Generated by Django 3.2.4 on 2023-02-26 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20230226_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_mark', models.IntegerField()),
                ('exam_mark', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
        ),
    ]
