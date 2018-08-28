from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField, FilerFileField


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


class UngleichHeaderWithBackgroundImageSlider(CMSPlugin):
    carousel_data_interval = models.IntegerField(default=2000)


class UngleichHeaderWithBackgroundVideoSliderItem(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_header_item_poster",
        on_delete=models.SET_NULL,
        help_text='The background image or poster image for video.'
    )
    image_portrait = FilerImageField(
        null=True,
        blank=True,
        related_name="ungleich_header_item_poster_sm",
        on_delete=models.SET_NULL,
        verbose_name="Image (portrait)",
        help_text='Optional background image or poster image for video (for tall screens).'
    )
    video = FilerFileField(
        null=True,
        blank=True,
        related_name="ungleich_header_item_video",
        on_delete=models.SET_NULL,
        help_text='Leaving this blank will make the image as the background.'
    )
    heading = models.CharField(
        blank=True, null=True, max_length=100,
        help_text='An optional title for this slide.',
    )
    description = models.TextField(
        blank=True, null=True,
        help_text='An optional description for this slide.'
    )
    btn_link = models.CharField(
        max_length=100, blank=True, null=True,
        help_text=(
            'Url or #id to navigate on click. If this field is left empty, no '
            'button would be displayed.'
        )
    )
    btn_text = models.CharField(
        blank=True, null=True, max_length=50,
        help_text='Text for the button, if a link is provided.'
    )


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


class UngleichFooter(CMSPlugin):
    copyright_label = models.CharField(
        max_length=100, default='', blank=True,
        help_text='Name of the company alongside the copyright year'
    )
    link_text = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Text for the link on the right part of footer'
    )
    link_url = models.URLField(
        blank=True, null=True,
        help_text='Url to the link in footer'
    )
    twitter_url = models.URLField(
        blank=True, null=True,
        help_text='If empty, twitter btn will not be visible'
    )
    linkedin_url = models.URLField(
        blank=True, null=True,
        help_text='If empty, linkedin btn will not be visible'
    )
    github_url = models.URLField(
        blank=True, null=True,
        help_text='If empty, github btn will not be visible'
    )
    facebook_url = models.URLField(
        blank=True, null=True,
        help_text='If empty, facebook btn will not be visible'
    )
    youtube_url = models.URLField(
        blank=True, null=True,
        help_text='If empty, youtube btn will not be visible'
    )
