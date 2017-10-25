from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    UngelichContactUsSection, UngelichTextSection, Service, ServiceItem,
    About, AboutItem, SectionWithImage
)


def get_section_id(plugin_instance, default):
    """
    A helper function to get the section id from a given menu text
    :param plugin_instance:
    :param default: The default section id to return in case a section id
                    is not found
    :return: The section id for the plugin_instance
    """
    section_id = default
    if hasattr(plugin_instance, 'menu_text'):
        menu_words = plugin_instance.menu_text.split()
        if len(menu_words) > 0:
            section_id = menu_words[0]
    return section_id


@plugin_pool.register_plugin
class SectionWithImagePlugin(CMSPluginBase):
    model = SectionWithImage
    render_template = "ungleich_page/glasfaser/section_with_image.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'image': instance.image,
            'object': instance,
            'placeholder': placeholder
        })
        return context


@plugin_pool.register_plugin
class SectionContact(CMSPluginBase):
    model = UngelichContactUsSection
    render_template = "ungleich_page/glasfaser/section_contact.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SectionContact, self).render(
            context, instance, placeholder
        )
        context['instance'] = instance
        context['section_id'] = get_section_id(instance, 'contact')
        return context


@plugin_pool.register_plugin
class SectionTextParagraphDCL(CMSPluginBase):
    model = UngelichTextSection
    render_template = "ungleich_page/glasfaser/section_text_dcl.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SectionTextParagraphDCL, self).render(
            context, instance, placeholder
        )
        context['instance'] = instance
        context['section_id'] = get_section_id(instance, 'your')
        return context


@plugin_pool.register_plugin
class SectionTextParagraphGlasfaser(CMSPluginBase):
    model = UngelichTextSection
    render_template = "ungleich_page/glasfaser/section_text_glasfaser.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SectionTextParagraphGlasfaser, self).render(
            context, instance, placeholder
        )
        context['instance'] = instance
        context['section_id'] = get_section_id(instance, 'our')
        return context


@plugin_pool.register_plugin
class GlasfaserServicesPlugin(CMSPluginBase):
    name = "Glasfaser Services Plugin"
    model = Service
    render_template = "ungleich_page/glasfaser/section_services.html"
    cache = False
    allow_children = True
    child_classes = ['GlasfaserServicesItemPlugin']

    def render(self, context, instance, placeholder):
        context['service_instance'] = instance
        context['section_id'] = get_section_id(instance, 'services')
        return context


@plugin_pool.register_plugin
class GlasfaserServicesItemPlugin(CMSPluginBase):
    name = "Glasfaser Service Item Plugin"
    model = ServiceItem
    render_template = "ungleich_page/glasfaser/_services_item.html"
    cache = False
    require_parent = True
    parent_classes = ['GlasfaserServicesPlugin']

    def render(self, context, instance, placeholder):
        context = super(GlasfaserServicesItemPlugin, self).render(
            context, instance, placeholder
        )
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class GlasfaserAboutPlugin(CMSPluginBase):
    name = "Glasfaser About Plugin"
    model = About
    render_template = "ungleich_page/glasfaser/section_about.html"
    cache = False
    allow_children = True
    child_classes = ['GlasfaserAboutItemPlugin']

    def render(self, context, instance, placeholder):
        context['about_instance'] = instance
        context['section_id'] = get_section_id(instance, 'about')
        return context


@plugin_pool.register_plugin
class GlasfaserAboutItemPlugin(CMSPluginBase):
    name = "Glasfaser About Item Plugin"
    model = AboutItem
    render_template = "ungleich_page/glasfaser/_about_item.html"
    cache = False
    require_parent = True
    parent_classes = ['GlasfaserAboutPlugin']

    def render(self, context, instance, placeholder):
        context = super(GlasfaserAboutItemPlugin, self).render(
            context, instance, placeholder
        )
        context['instance'] = instance
        return context
