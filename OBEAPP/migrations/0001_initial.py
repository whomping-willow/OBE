# Generated by Django 4.0.3 on 2022-10-05 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AssignSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=200, null=True)),
                ('course_name', models.CharField(max_length=200, null=True)),
                ('credit', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], null=True)),
                ('course_type', models.CharField(choices=[('Lab', 'Lab'), ('Theory', 'Theory')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st Year 1st Semester', '1st Year 1st Semester'), ('1st Year 2nd Semester', '1st Year 2nd Semester'), ('2nd Year 1st Semester', '2nd Year 1st Semester'), ('2nd Year 2nd Semester', '2nd Year 2nd Semester'), ('3rd Year 1st Semester', '3rd Year 1st Semester'), ('3rd Year 2nd Semester', '3rd Year 2nd Semester'), ('4th Year 1st Semester', '4th Year 1st Semester'), ('4th Year 2nd Semester', '4th Year 2nd Semester')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startYear', models.CharField(max_length=200, null=True)),
                ('endYear', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Finished', 'Finished')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=20, null=True)),
                ('roll', models.IntegerField(null=True)),
                ('exam_roll', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('batch', models.IntegerField(null=True)),
                ('department', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('LPR', 'LPR'), ('Leave', 'Leave'), ('Retired', 'Retired')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('faculty_name', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AssignTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.assigncourse')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='AssignStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.assignsemester')),
                ('student', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.student')),
            ],
        ),
        migrations.CreateModel(
            name='AssignSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.department')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.session')),
            ],
        ),
        migrations.AddField(
            model_name='assignsemester',
            name='semester',
            field=models.ForeignKey(max_length=300, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.semester'),
        ),
        migrations.AddField(
            model_name='assignsemester',
            name='session',
            field=models.ForeignKey(max_length=300, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.assignsession'),
        ),
        migrations.AddField(
            model_name='assigncourse',
            name='course',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.course'),
        ),
        migrations.AddField(
            model_name='assigncourse',
            name='semester',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OBEAPP.assignsemester'),
        ),
    ]
