# Generated by Django 4.1.6 on 2023-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcgapp', '0002_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='empdata',
            name='empid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
