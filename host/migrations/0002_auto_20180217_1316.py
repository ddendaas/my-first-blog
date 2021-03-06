# Generated by Django 2.0.2 on 2018-02-17 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='bday',
            new_name='birthday',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='description',
        ),
        migrations.AddField(
            model_name='registration',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='registration',
            name='study',
            field=models.CharField(choices=[('HS', 'Highscool'), ('MBO', 'MBO')], default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
