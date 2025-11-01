from django_filters import filterset
from .models import Hotel, Room


class HotelFilter(filterset.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'hotel_stars': ['gt','lt'],
        }

class RoomFilter(filterset.FilterSet):
    class Meta:
        model = Room
        fields = {
            'price': ['gt','lt']
        }