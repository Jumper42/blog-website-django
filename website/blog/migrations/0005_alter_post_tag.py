# Generated by Django 4.0.4 on 2022-05-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_author_alter_post_content_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='post', to='blog.tag'),
        ),
    ]