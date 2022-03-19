# Generated by Django 3.2.12 on 2022-03-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPI', '0002_resumesection_one_to_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumesection',
            name='one_to_one',
        ),
        migrations.RemoveField(
            model_name='resumesection',
            name='skills_select',
        ),
        migrations.AddField(
            model_name='resumesection',
            name='skills_select',
            field=models.ManyToManyField(related_name='resumeSkills', to='mainAPI.requiredskills'),
        ),
        migrations.RemoveField(
            model_name='resumesection',
            name='your_skills',
        ),
        migrations.AddField(
            model_name='resumesection',
            name='your_skills',
            field=models.ManyToManyField(related_name='resumeYourSkills', to='mainAPI.requiredskills'),
        ),
    ]
