# Generated by Django 4.2.6 on 2023-10-26 06:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_alter_post_thumbnail_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name="본문"),
        ),
        migrations.AlterField(
            model_name="post",
            name="thumbnail_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/%Y/%m/%d/", verbose_name="썸네일"
            ),
        ),
    ]