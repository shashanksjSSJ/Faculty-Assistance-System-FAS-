# Generated by Django 4.1.4 on 2023-03-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_student_delete_sendmailstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('studentname', models.CharField(max_length=100)),
            ],
        ),
    ]