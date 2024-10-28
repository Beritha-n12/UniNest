from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, related_name="rooms", on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()

    def __str__(self):
        return f"{self.building.name} - {self.room_number}"
