# Generated by Django 3.2 on 2022-07-05 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sight', '0002_comment_info_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sight.sight', verbose_name='关联景点'),
        ),
    ]