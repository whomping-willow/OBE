# Generated by Django 4.0.3 on 2022-10-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OBEAPP', '0009_alter_nonobemark_att_alter_nonobemark_sem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonobemark',
            name='att',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='nonobemark',
            name='sem',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='nonobemark',
            name='tt1',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='nonobemark',
            name='tt2',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='nonobemark',
            name='tt3',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]