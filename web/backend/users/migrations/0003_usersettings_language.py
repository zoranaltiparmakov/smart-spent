# Generated by Django 2.1.2 on 2018-10-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181022_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='language',
            field=models.ForeignKey(default=1, on_delete=None, to='users.Language'),
        ),
    ]
