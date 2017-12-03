from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class UngelichPicture(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="image",
        on_delete=models.SET_NULL
    )
    title = HTMLField()


class SectionWithImage(UngelichPicture):
    menu_text = models.CharField(max_length=100, default="", blank=True)
    price_tag_image = FilerImageField(
        null=True,
        blank=True,
        related_name="price_tag_image",
        on_delete=models.SET_NULL
    )
    price_tag_url = models.URLField(max_length=300, default="", blank=True)


class UngelichContactUsSection(CMSPlugin):
    menu_text = models.CharField(max_length=100, default="", blank=True)
    email = models.EmailField(max_length=200, default="info@ungleich.ch")
    contact_text = models.CharField(
        max_length=100, default="Contact", blank=True
    )
    organization_name = models.CharField(
        max_length=100, default="ungleich GmbH", blank=True
    )
    address = models.CharField(
        max_length=100, default="In der Au 7, Schwanden 8762", blank=True
    )
    country = models.CharField(
        max_length=100, default="Switzerland", blank=True
    )
    contact_form_header_text = models.CharField(
        max_length=100, default="Send us a message.", blank=True
    )


class UngelichTextSection(CMSPlugin):
    menu_text = models.CharField(max_length=100, default="", blank=True)
    title = models.CharField(max_length=200)
    description = HTMLField()


class Service(CMSPlugin):
    menu_text = models.CharField(max_length=100, default="", blank=True)
    title = models.CharField(max_length=200)
    sub_title = HTMLField()

    def __str__(self):
        return self.title


class ServiceItem(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="service_item_image",
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=200)
    description = HTMLField()

    def __str__(self):
        return self.title


class About(Service):
    pass


class AboutItem(UngelichPicture):
    inverted = models.BooleanField(default=False)
    link_url = models.URLField(max_length=300, default="", blank=True)

    def __str__(self):
        alignment = "Right" if self.inverted else "Left"
        return "{alignment} - {title}".format(
            alignment=alignment, title=self.title
        )


class UngleichServiceItem(ServiceItem):
    data_replaced_image = FilerImageField(
        null=True,
        blank=True,
        related_name="service_item_data_replaced_image",
        on_delete=models.SET_NULL
    )


class UngleichSimpleHeader(CMSPlugin):
    background_image = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_simple_header_background_image",
        on_delete=models.SET_NULL
    )
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_simple_header_image",
        on_delete=models.SET_NULL
    )
    text = HTMLField()


class UngleichHeader(CMSPlugin):
    background_image = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_header_background_image",
        on_delete=models.SET_NULL
    )
    carousel_data_interval = models.IntegerField(default=5000)


class UngleichHeaderItem(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_header_item_image",
        on_delete=models.SET_NULL
    )
    description = HTMLField()


class UngleichProductItem(ServiceItem):
    url = models.URLField(max_length=300, default="", blank=True)


class UngleichProduct(Service):
    section_class = models.CharField(max_length=100, default="", blank=True)


class UngleichCustomer(Service):
    section_class = models.CharField(max_length=100, default="", blank=True)
    carousel_data_interval = models.IntegerField(default=3000)
    bottom_text = HTMLField(
        default='<h3 class="section-subheading text-muted">*ungleich means '
                'not equal to (≠) U+2260.</h3>'
    )


class UngleichCustomerItem(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="customer_item_image",
        on_delete=models.SET_NULL
    )
    url = models.URLField(max_length=300, default="", blank=True)
    description = HTMLField()


class UngleichHTMLOnly(CMSPlugin):
    name = models.CharField(max_length=50, default="", blank=True)
    HTML = HTMLField()

    def __str__(self):
        return self.name
