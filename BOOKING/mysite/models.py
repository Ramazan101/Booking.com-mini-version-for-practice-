from django.contrib.auth.models import AbstractUser
from django.db import models, router
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)
    country_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.country_name

class UserProfile(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    STATUS_CHOICES = (
    ('client', 'client'),
    ('owner', 'owner')
    )
    user_image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)],
                                      null=True, blank=True)
    phone = PhoneNumberField()
    status = models.CharField(choices=STATUS_CHOICES, default='SIMPLE',max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class City(models.Model):
    city_name = models.CharField(max_length=32)
    city_img = models.ImageField(upload_to='images/', null=True, blank=True)



    def __str__(self):
        return self.city_name


class Service(models.Model):
    service_name = models.CharField(max_length=32)
    service_img = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotel_city')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    hotel_stars = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                          MaxValueValidator(5)])
    street = models.CharField(max_length=100)
    postal_index = models.PositiveIntegerField()
    service = models.ManyToManyField(Service)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def get_avg_rating(self):
        score = self.hotel_review.all()
        if score.exists():
            return round(sum([i.stars for i in score]) / score.count(), 2)
        return 0

    def get_count_people(self):
        return self.hotel_review.count()

    def __str__(self):
        return self.hotel_name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_image')
    hotel_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.hotel}, {self.hotel_image}'

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room')
    room_number = models.IntegerField()
    TYPE_CHOICES = (
        ('LUX','LUX'),
        ('ECONOMIC','ECONOMIC'),
        ('FAMILY','FAMILY'),
        ('ONE_PLEASE','ONE_PLEASE'),
    )
    room_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    STATUS_CHOICES_ROOM = (
        ('свободен','свободен'),
        ('занят','занят')
    )
    room_status = models.CharField(max_length=20, choices=STATUS_CHOICES_ROOM)
    room_description = models.TextField()
    price = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.hotel}, {self.room_number}'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.room}, {self.room_image}'


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.hotel},{self.user}'


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_review')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    commit = models.TextField()
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)])

    def __str__(self):
        return f'{self.hotel}, {self.user},{self.stars}'










