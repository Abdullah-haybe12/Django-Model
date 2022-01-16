# Generated by Django 3.2.8 on 2022-01-16 22:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('VZ', '0003_project_thema'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='partner',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ADRZ', 'ADRZ'), ('CZ Zorgkantoor', 'CZ Zorgkantoor'), ('Emergis', 'Emergis'), ('Hoornbeek', 'Hoornbeek')], default=[1], max_length=37),
        ),
        migrations.AddField(
            model_name='project',
            name='project_leider',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sophie Aberson', 'Sophie Aberson'), ('Rianne Deij', 'Rianne Deij'), ('Tamar Duivewaarde', 'Tamar Duivewaarde'), ('Anjali Geensen', 'Anjali Geensen')], default=[1], max_length=59),
        ),
    ]
