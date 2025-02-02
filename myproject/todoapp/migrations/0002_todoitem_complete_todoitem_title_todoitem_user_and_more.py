# Generated by Django 5.0.6 on 2024-06-09 14:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='title',
            field=models.CharField(default='To do item', max_length=200),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterOrderWithRespectTo(
            name='todoitem',
            order_with_respect_to='user',
        ),
    ]
