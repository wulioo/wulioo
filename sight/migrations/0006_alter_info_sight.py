# Generated by Django 3.2 on 2022-07-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sight', '0005_alter_info_sight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sight',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sight.sight', verbose_name='关联景点'),
        ),
    ]
