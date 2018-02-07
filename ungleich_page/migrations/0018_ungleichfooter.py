# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-02-06 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('ungleich_page', '0017_auto_20171219_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='UngleichFooter',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                       parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('copyright', models.CharField(
                    blank=True, default='', max_length=100,
                    help_text='Name of the company alongside the copyright year')),
                ('link_text', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('link_url', models.URLField(blank=True,
                                             help_text='Url to the link in footer', null=True)),
                ('twitter_url', models.URLField(
                    blank=True, help_text='If empty, twitter btn will not be visible', null=True)),
                ('linkedin_url', models.URLField(
                    blank=True, help_text='If empty, linkedin btn will not be visible', null=True)),
                ('github_url', models.URLField(
                    blank=True, help_text='If empty, github btn will not be visible', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
