# Generated by Django 2.2.2 on 2019-06-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkpage', '0005_auto_20190617_2202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleItem',
        ),
        migrations.DeleteModel(
            name='NewsItem',
        ),
        migrations.DeleteModel(
            name='PersonItem',
        ),
        migrations.DeleteModel(
            name='PlaceItem',
        ),
    ]
