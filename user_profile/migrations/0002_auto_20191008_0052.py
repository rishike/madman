# Generated by Django 2.2.4 on 2019-10-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='picode',
            new_name='pincode',
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='user_profile.Profile'),
        ),
    ]
