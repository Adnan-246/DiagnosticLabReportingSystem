# Generated by Django 3.1.4 on 2020-12-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demail', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(max_length=100)),
            ],
        ),
    ]