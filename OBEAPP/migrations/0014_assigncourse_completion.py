# Generated by Django 4.0.3 on 2023-01-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OBEAPP', '0013_teacher_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigncourse',
            name='completion',
            field=models.CharField(choices=[('ASSIGNED', 'ASSIGNED'), ('PENDING', 'PENDING')], default='PENDING', max_length=20, null=True),
        ),
    ]