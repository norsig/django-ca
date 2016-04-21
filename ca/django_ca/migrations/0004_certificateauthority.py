# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0003_auto_20160106_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateAuthority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A human-readable name', max_length=32, unique=True)),
                ('serial', models.CharField(max_length=48)),
                ('created', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
                ('pub', models.TextField(verbose_name='Public key')),
                ('private_key_path', models.CharField(help_text='Path to the private key.', max_length=256)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='django_ca.CertificateAuthority')),
            ],
            options={
                'verbose_name': 'Certificate Authority',
                'verbose_name_plural': 'Certificate Authorities',
            },
            bases=(models.Model, ),
        ),
    ]
