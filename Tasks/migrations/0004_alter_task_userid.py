# Generated by Django 4.1 on 2022-08-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_task_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='userId',
            field=models.CharField(max_length=100, null=True),
        ),
    ]