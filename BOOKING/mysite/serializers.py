from .models import Country, UserProfile, City, Service, Hotel, HotelImage, Room, RoomImage, Booking, Review
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HotelListSerializer(serializers.ModelSerializer):
    city = CitySimpleSerializer()
    country = CountrySerializer()
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = '__all__'

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class CityDetailSerializer(serializers.ModelSerializer):
    hotel_city = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'city_img','hotel_city']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'




class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'

class RoomListSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id','room_image','room_number','room_type','room_status','price']




class RoomDetailSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)


    class Meta:
        model = Room
        fields = ['room_image','room_number','room_type','room_status','price','room_description']




class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    hotel_review = ReviewSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    hotel_room = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_image', 'hotel_review','hotel_name','city'
                  ,'hotel_stars','street','service','owner','description','get_avg_rating', 'get_count_people','hotel_room']



    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

