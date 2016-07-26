from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    cover=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete = models.SET_NULL,
        related_name = '+'
    )
    profile_picture=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete = models.SET_NULL,
        related_name = '+'
    )
    welcome_text = RichTextField(blank=True)
    footer_message = models.CharField(max_length = 400,blank=True,null=True)


    content_panels = Page.content_panels + [

        FieldPanel('welcome_text'),
        ImageChooserPanel('cover'),
        ImageChooserPanel('profile_picture'),
        FieldPanel('footer_message'),
        FieldPanel('body', classname="full")
    ]
