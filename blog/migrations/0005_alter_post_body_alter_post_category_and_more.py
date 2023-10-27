# Generated by Django 4.2.6 on 2023-10-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_remove_post_tags_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(verbose_name="내용"),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
                verbose_name="카테고리",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="thumbnail_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/blog/%Y%m%d",
                verbose_name="썸네일",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, verbose_name="제목"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]