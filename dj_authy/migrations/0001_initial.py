# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import phonenumber_field.modelfields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authy_id', models.CharField(max_length=64, null=True, db_index=True)),
                ('cellphone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, db_index=True)),
                ('is_smartphone', models.BooleanField(default=True)),
                ('data', jsonfield.fields.JSONField(default={})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='authyprofile',
            unique_together=set([('authy_id', 'cellphone')]),
        ),
    ]
