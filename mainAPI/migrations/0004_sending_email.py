# Generated by Django 3.2.12 on 2022-03-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0003_auto_20220319_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='sending_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]