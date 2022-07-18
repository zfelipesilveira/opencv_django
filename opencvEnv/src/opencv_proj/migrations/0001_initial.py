# Generated by Django 3.2.14 on 2022-07-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFiltered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('action', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
