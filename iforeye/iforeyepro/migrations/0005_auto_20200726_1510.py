# Generated by Django 3.0.6 on 2020-07-26 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iforeyepro', '0004_recording_text_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='text_file',
        ),
        migrations.AddField(
            model_name='recording',
            name='audio_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='audio_files'),
            preserve_default=False,
        ),
    ]