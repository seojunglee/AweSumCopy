# Generated by Django 4.0.3 on 2022-05-03 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_subtitle_videoid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtitle',
            old_name='videoid',
            new_name='video',
        ),
    ]
