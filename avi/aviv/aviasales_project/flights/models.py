from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origin} to {self.destination}"

class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=150)
    passenger_age = models.IntegerField()
    passenger_email = models.EmailField()

    def __str__(self):
        return f"Ticket for {self.passenger_name} on flight {self.flight}"

