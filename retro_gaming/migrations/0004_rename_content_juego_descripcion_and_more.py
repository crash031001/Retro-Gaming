# Generated by Django 5.0.6 on 2024-08-09 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retro_gaming', '0003_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juego',
            old_name='content',
            new_name='DESCRIPCION',
        ),
        migrations.RenameField(
            model_name='juego',
            old_name='title',
            new_name='NOMBRE',
        ),
    ]
