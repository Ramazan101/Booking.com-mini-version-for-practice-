from django.contrib import admin
from .models import (Country, UserProfile, City, Service, Hotel, HotelImage, Room, RoomImage, Booking, Review)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Country, City)
class CountryAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Review)
