# File: voter_analytics/models.py
# Author: David Myat (amyat@bu.edu), 10/28/2025
# Description: Define data models for the voter_analytics project
from django.db import models
from django.urls import reverse


# Create your models here.
class Voter(models.Model):
    """Store/represent the data from one voter record."""

    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.TextField()
    street_name = models.TextField()
    zip_code = models.TextField()
    apartment_number = models.TextField(blank=True)

    date_of_birth = models.DateField()
    registration_date = models.DateField()

    party_affiliation = models.CharField(max_length=2)
    precinct = models.TextField()

    # recent voting history
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()

    def __str__(self):
        """Return string representation of Voter object."""
        return (
            f"{self.last_name}, {self.first_name} ({self.street_name}, {self.zip_code})"
        )


def load_data():
    """Function to load data from CSV file into the Django model instance."""

    filename = ...
    f = open(filename)
    f.readline()

    for row in f:

        line = f.readline().strip()
        fields = line.split(",")

        voter = Voter(
            last_name=fields[0],
            first_name=fields[1],
            street_number=fields[2],
            street_name=fields[3],
            apartment_number=fields[4],
            zip_code=fields[5],
            date_of_birth=fields[6],
            registration_date=fields[7],
            party_affiliation=fields[8],
            precinct_number=fields[9],
            v20state=fields[10] == "1",
            v21town=fields[11] == "1",
            v21primary=fields[12] == "1",
            v22general=fields[13] == "1",
            v23town=fields[14] == "1",
        )

    print(f"Created result: {voter}")
