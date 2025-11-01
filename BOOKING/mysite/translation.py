from modeltranslation.translator import TranslationOptions,register
from .models import Country, City, Room, Hotel

@register(City)
class CountryTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)