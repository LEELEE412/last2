# Generated by Django 4.2.16 on 2025-05-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='current_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_number',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
