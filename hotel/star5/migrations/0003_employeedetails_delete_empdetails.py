# Generated by Django 4.1.7 on 2023-02-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star5', '0002_empdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeedetails',
            fields=[
                ('EMPLOYEE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('EMPLOYEE_NAME', models.CharField(max_length=30)),
                ('DATE_OF_JOINING', models.CharField(max_length=30)),
                ('SALARY', models.DecimalField(decimal_places=3, max_digits=7)),
                ('MOBILE', models.CharField(max_length=20)),
                ('DESIGNATION', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='empdetails',
        ),
    ]
