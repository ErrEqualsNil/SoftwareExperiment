# Generated by Django 3.0 on 2020-12-04 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20201204_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='repair_crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='models.RepairCrew'),
        ),
    ]