# Generated by Django 4.2.6 on 2023-10-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]