# Generated by Django 3.2 on 2023-06-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='Project/images')),
                ('project_name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('desc2', models.TextField(blank=True)),
            ],
        ),
    ]
