# Generated by Django 4.2.2 on 2023-06-16 11:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
