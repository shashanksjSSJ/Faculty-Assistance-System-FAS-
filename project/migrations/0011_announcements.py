# Generated by Django 4.1.4 on 2023-02-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_studentdata1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
    ]
