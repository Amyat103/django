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
    precinct_number = models.TextField()

    # recent voting history
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()

    voter_score = models.IntegerField()

    def __str__(self):
        """Return string representation of Voter object."""
        return (
            f"{self.last_name}, {self.first_name} ({self.street_name}, {self.zip_code})"
        )


def load_data():
    """Function to load data from CSV file into the Django model instance."""
    Voter.objects.all().delete()

    filename = "/Users/david/Downloads/newton_voters.csv"
    f = open(filename)
    f.readline()

    for line in f:
        fields = line.split(",")

        try:
            voter = Voter(
                last_name=fields[1],
                first_name=fields[2],
                street_number=fields[3],
                street_name=fields[4],
                apartment_number=fields[5],
                zip_code=fields[6],
                date_of_birth=fields[7],
                registration_date=fields[8],
                party_affiliation=fields[9],
                precinct_number=fields[10],
                v20state=fields[11] == "TRUE",
                v21town=fields[12] == "TRUE",
                v21primary=fields[13] == "TRUE",
                v22general=fields[14] == "TRUE",
                v23town=fields[15] == "TRUE",
                voter_score=int(fields[16]),
            )
            voter.save()
            print(f"Created voter: {voter}")
        except:
            print(f"skipped: {line}")
