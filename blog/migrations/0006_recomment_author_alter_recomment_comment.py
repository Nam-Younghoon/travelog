# Generated by Django 4.2.6 on 2023-10-31 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_remove_comment_parent_comment_recomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="recomment",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recomment",
            name="comment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replys",
                to="blog.comment",
            ),
        ),
    ]
