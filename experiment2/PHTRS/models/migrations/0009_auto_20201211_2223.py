# Generated by Django 3.0 on 2020-12-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_auto_20201211_2105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DamageFile',
            new_name='ReportFile',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='equipment_assigned',
        ),
        migrations.AlterField(
            model_name='potholes',
            name='repair_priority',
            field=models.IntegerField(default=-1),
        ),
    ]