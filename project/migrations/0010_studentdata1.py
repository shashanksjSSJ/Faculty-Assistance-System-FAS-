# Generated by Django 4.1.4 on 2023-02-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_uploaddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('regno', models.CharField(max_length=10)),
                ('parentname', models.CharField(max_length=200)),
                ('emailid', models.EmailField(max_length=200)),
                ('parentemail', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('studentcg', models.CharField(max_length=4)),
                ('total1', models.IntegerField()),
                ('sub1', models.IntegerField()),
                ('total2', models.IntegerField()),
                ('sub2', models.IntegerField()),
                ('total3', models.IntegerField()),
                ('sub3', models.IntegerField()),
                ('total4', models.IntegerField()),
                ('sub4', models.IntegerField()),
            ],
        ),
    ]
