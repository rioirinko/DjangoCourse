# Generated by Django 2.1.2 on 2018-10-10 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_auto_20181010_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='course_br',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='course_con',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_cat',
            new_name='course',
        ),
    ]
