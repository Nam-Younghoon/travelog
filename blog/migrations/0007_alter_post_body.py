# Generated by Django 4.2.6 on 2023-10-26 06:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]