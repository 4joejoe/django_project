# Generated by Django 4.1.1 on 2022-09-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
