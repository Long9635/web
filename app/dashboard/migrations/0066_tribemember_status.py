# Generated by Django 2.2.4 on 2019-11-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0065_tribemember'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribemember',
            name='status',
            field=models.CharField(blank=True, choices=[('accepted', 'accepted'), ('pending', 'pending'), ('rejected', 'rejected')], max_length=20),
        ),
    ]
