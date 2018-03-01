# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-01 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('datacenterlight', '0011_auto_20180220_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCLSectionPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('heading', models.CharField(blank=True, help_text='An optional heading for the Section', max_length=100, null=True)),
                ('content', djangocms_text_ckeditor.fields.HTMLField()),
                ('text_direction', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default=True, help_text='The alignment of text in the section', max_length=10)),
                ('html_id', models.SlugField(blank=True, help_text='An optional html id for the Section. Required to set as target of a link on page', null=True)),
                ('center_on_mobile', models.BooleanField(default=False, help_text='Select to center align content on small screens.')),
                ('background_gradient', models.BooleanField(default=False, help_text='Select to add a gradient background to the section.')),
                ('plain_heading', models.BooleanField(default=False, help_text='Select to keep the heading style simpler.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLNavbarDropdownPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('text', models.CharField(help_text='Text for the dropdown toggle', max_length=50)),
                ('target', models.CharField(default='', help_text='Optional Url or #id to navigate on click', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLContactPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('heading', models.CharField(blank=True, default='Contact', max_length=100)),
                ('organization_name', models.CharField(blank=True, default='ungleich GmbH', max_length=100)),
                ('email', models.EmailField(default='info@ungleich.ch', max_length=200)),
                ('address', models.CharField(blank=True, default='In der Au 7, Schwanden 8762', max_length=100)),
                ('country', models.CharField(blank=True, default='Switzerland', max_length=100)),
                ('form_header', models.CharField(blank=True, default='Send us a message.', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLFooterPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('copyright_label', models.CharField(blank=True, default='ungleich GmbH', help_text='Name of the company alongside the copyright year', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLLinkPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('target', models.CharField(help_text='Url or #id to navigate to', max_length=100)),
                ('text', models.CharField(help_text='Text for the menu item', max_length=50)),
                ('title', models.CharField(blank=True, help_text='Optional title text, that will be shown when a user hovers over the link', max_length=100, null=True)),
                ('separator', models.BooleanField(default=False, help_text='Select to include a separator after the previous link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLSectionIconPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('fontawesome_icon_name', models.CharField(help_text='Name of the fontawesome icon to use. <a href="https://fontawesome.com/v4.7.0/icons/" target="_blank">Refer docs.</a>', max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLSectionImagePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('caption', models.CharField(blank=True, help_text='Optional caption for the image.', max_length=100, null=True)),
                ('image', filer.fields.image.FilerImageField(help_text='Image file to be used in section. Add multiple plugins to add more than one image', on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLBannerListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('heading', models.CharField(blank=True, help_text='An optional heading for the Section', max_length=100, null=True)),
                ('html_id', models.SlugField(blank=True, help_text='An optional html id for the Section. Required to set as target of a link on page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DCLBannerItemPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('content', djangocms_text_ckeditor.fields.HTMLField()),
                ('banner_text', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Optional text to be shown as banner in other half.', max_length=100, null=True)),
                ('text_direction', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default=True, help_text='The alignment of text in the section', max_length=10)),
                ('banner_image', filer.fields.image.FilerImageField(blank=True, help_text='Optional image to be used in the banner in other half.', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
