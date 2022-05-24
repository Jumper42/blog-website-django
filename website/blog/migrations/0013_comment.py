# Generated by Django 4.0.4 on 2022-05-23 11:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_comments_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(500)])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.post')),
            ],
        ),
    ]
