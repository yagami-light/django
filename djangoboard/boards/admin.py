from django.contrib import admin
from .models import Board

from django.contrib import admin
from django.forms.widgets import TextInput

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField





class SampleModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            AddressField: {'widget': GoogleMapsAddressWidget},
            GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
                                }
admin.site.register(Board,SampleModelAdmin)
