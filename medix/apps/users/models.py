from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from users.select_choices import *
from datetime import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Created At'))
    modified_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_('Modified At'))

    class Meta:
        abstract = True

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank = True, null = True)

    custom_role = models.IntegerField(verbose_name=_('User Role'), choices=ROLE_TYPE_CHOICES, default=0)
    practice = models.IntegerField(verbose_name=_('Practice Specialisation'), choices=SPECIALISATION_TYPE_CHOICES, blank = True, null = True)
    institution = models.IntegerField(verbose_name=_('Institution Type'), choices=INSTITUTION_TYPE_CHOICES, blank = True, null = True)
    emergency_services = models.IntegerField(verbose_name=_('Service Type'), choices=SERVICES_TYPE_CHOICES, blank = True, null = True)
    gender = models.IntegerField(verbose_name=_('Gender'), choices=GENDER_CHOICES, blank = True, null = True)

    phone = models.CharField(_("Phone Number"), max_length=254, blank = True, null = True)
    national_identification_number = models.CharField(_("National Identification Number"), max_length=100, blank = True, null = True)
    trading_name = models.CharField(_("Trading Name"), max_length=254, blank = True, null = True)
    address_of_institution = models.TextField(_("Address Of Institution"), blank = True, null = True)
    contact_person = models.CharField(_("Contact Person"), max_length=254, blank = True, null = True)

    def __str__(self):
        return self.user.email