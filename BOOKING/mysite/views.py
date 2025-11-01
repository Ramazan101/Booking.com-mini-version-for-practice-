from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .filters import HotelFilter, RoomFilter

from .models import Country, UserProfile, City, Service, Hotel, HotelImage, Room, RoomImage, Review, Booking
from .serializers import (CountrySerializer, UserProfileSerializer, CityListSerializer,CityDetailSerializer,
                          ServiceSerializer, HotelListSerializer, HotelDetailSerializer,
                          RoomImageSerializer, ReviewSerializer, HotelImageSerializer, BookingSerializer,
                          UserSerializer, LoginSerializer, RoomListSerializer, RoomDetailSerializer )
from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CityListAPIview(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIview(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class HotelListAPIview(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['hotel_name']
    filterset_class = HotelFilter

class HotelDetailAPIview(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer



class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer



class RoomListAPView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter


class RoomDetailAPView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer






