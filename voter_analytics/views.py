# File: voter_analytics/views.py
# Author: David Myat (amyat@bu.edu), 10/28/2025
# Description: Views for the voter_analytics project
from django.shortcuts import render
from django.views.generic import ListView

from .models import Voter


# Create your views here.
class VoterListView(ListView):
    """View to display voter results."""

    template_name = "voter_analytics/show_all_voters.html"
    model = Voter
    context_object_name = "voters"
    paginate_by = 100

    def get_queryset(self):
        """Return the queryset of voters."""
        qs = super().get_queryset()
        return qs


class VoterDetailView(ListView):
    """View to display a single voter's details."""

    template_name = "voter_analytics/voter.html"
    model = Voter
    context_object_name = "voter"
