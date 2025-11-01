from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CountryViewSet, UserProfileViewSet, CityListAPIview,CityDetailAPIview,ServiceViewSet,
                    HotelListAPIview,HotelDetailAPIview,HotelImageViewSet,RoomListAPView, RoomDetailAPView, RoomImageViewSet, BookingViewSet, RegisterView,
                    CustomLoginView, LogoutView)

router = DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'hotel_image', HotelImageViewSet)
router.register(r'room_image', RoomImageViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('hotel/', HotelListAPIview.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIview.as_view(), name='hotel_detail'),
    path('city/', CityListAPIview.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIview.as_view(), name='city_detail'),
    path('room/', RoomListAPView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPView.as_view(), name='room_detail'),

]