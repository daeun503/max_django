# Generated by Django 3.2.1 on 2021-05-08 16:08

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]