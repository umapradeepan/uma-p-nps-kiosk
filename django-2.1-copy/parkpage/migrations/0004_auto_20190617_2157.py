# Generated by Django 2.2.2 on 2019-06-17 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpage', '0003_articleitem_lessonitem_newsitem_personitem_placeitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonitem',
            old_name='dir',
            new_name='url',
        ),
    ]
