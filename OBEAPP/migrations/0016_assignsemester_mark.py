# Generated by Django 4.0.3 on 2023-02-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OBEAPP', '0015_nonobemark_mark_obemark_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignsemester',
            name='mark',
            field=models.CharField(choices=[('ASSIGNED', 'ASSIGNED'), ('PENDING', 'PENDING')], default='PENDING', max_length=20, null=True),
        ),
    ]
