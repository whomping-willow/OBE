# Generated by Django 4.0.3 on 2022-10-06 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OBEAPP', '0005_assignchairman'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignExamCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.teacher')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.assignsemester')),
            ],
        ),
    ]
