# Generated by Django 4.0.1 on 2022-01-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_rename_gussed_game_guessed_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='selected_words',
            field=models.JSONField(default={'correct': [], 'wrong': []}, verbose_name='SelectedWords'),
        ),
    ]
