from django.db import models
from accounts.models import User
# Create your models here.
class Room(models.Model):
    number      = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    price       = models.FloatField()
    thumbnail = models.ImageField(upload_to='rooms', blank=True, null=True)

    def __str__(self):
        return f"{self.number}  {self.description}"


class Booking(models.Model):
    user    = models.ForeignKey(User, related_name='bookings',on_delete=models.CASCADE)
    room    = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()



    def __str__(self):
        return f"{self.user} has booked room number {self.room}  from {self.check_in} to {self.check_out}"
