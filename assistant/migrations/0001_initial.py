# Generated by Django 3.1.4 on 2020-12-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aemail', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('assistant_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('org', models.CharField(max_length=200)),
            ],
        ),
    ]