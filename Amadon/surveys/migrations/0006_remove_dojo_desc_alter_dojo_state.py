# Generated by Django 5.1.2 on 2024-11-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_dojo_desc_ninja_dojo_alter_dojo_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=5),
        ),
    ]