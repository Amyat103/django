# File: voter_analytics/views.py
# Author: David Myat (amyat@bu.edu), 10/28/2025
# Description: Views for the voter_analytics project
import plotly
import plotly.graph_objs as go

from django.shortcuts import render
from django.views.generic import DetailView, ListView

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

        party = self.request.GET.get("party_affiliation")
        if party:
            qs = qs.filter(party_affiliation=party)

        min_birth_year = self.request.GET.get("min_birth_year")
        if min_birth_year:
            qs = qs.filter(date_of_birth__year__gte=min_birth_year)

        max_birth_year = self.request.GET.get("max_birth_year")
        if max_birth_year:
            qs = qs.filter(date_of_birth__year__lte=max_birth_year)

        score = self.request.GET.get("voter_score")
        if score:
            qs = qs.filter(voter_score=score)

        if self.request.GET.get("v20state"):
            qs = qs.filter(v20state=True)

        if self.request.GET.get("v21town"):
            qs = qs.filter(v21town=True)

        if self.request.GET.get("v21primary"):
            qs = qs.filter(v21primary=True)

        if self.request.GET.get("v22general"):
            qs = qs.filter(v22general=True)

        if self.request.GET.get("v23town"):
            qs = qs.filter(v23town=True)

        return qs

    def get_context_data(self, **kwargs):
        """Provide context for the template."""

        context = super().get_context_data(**kwargs)
        context["birth_years"] = range(1920, 2010)
        return context


class VoterDetailView(DetailView):
    """View to display a single voter's details."""

    template_name = "voter_analytics/voter_detail.html"
    model = Voter
    context_object_name = "voter"


class GraphsView(ListView):
    """View to display graphs."""

    template_name = "voter_analytics/graphs.html"
    model = Voter
    context_object_name = "voters"

    def get_queryset(self):
        """Return the queryset of voters."""
        qs = super().get_queryset()

        party = self.request.GET.get("party_affiliation")
        if party:
            qs = qs.filter(party_affiliation=party)

        min_birth_year = self.request.GET.get("min_birth_year")
        if min_birth_year:
            qs = qs.filter(date_of_birth__year__gte=min_birth_year)

        max_birth_year = self.request.GET.get("max_birth_year")
        if max_birth_year:
            qs = qs.filter(date_of_birth__year__lte=max_birth_year)

        score = self.request.GET.get("voter_score")
        if score:
            qs = qs.filter(voter_score=score)

        if self.request.GET.get("v20state"):
            qs = qs.filter(v20state=True)

        if self.request.GET.get("v21town"):
            qs = qs.filter(v21town=True)

        if self.request.GET.get("v21primary"):
            qs = qs.filter(v21primary=True)

        if self.request.GET.get("v22general"):
            qs = qs.filter(v22general=True)

        if self.request.GET.get("v23town"):
            qs = qs.filter(v23town=True)

        return qs

    def get_context_data(self, **kwargs):
        """Provide context variable for the template."""

        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()
        birth_years = {}

        for voter in voters:
            year = voter.date_of_birth.year
            if year not in birth_years:
                birth_years[year] = 0
            birth_years[year] += 1

        y = list(birth_years.values())
        x = list(birth_years.keys())
        fig = go.Bar(x=x, y=y)
        graph_div_ages = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title="Voter Age Distribution"),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_ages"] = graph_div_ages

        parties = {}
        for voter in voters:
            party = voter.party_affiliation
            if party not in parties:
                parties[party] = 0
            parties[party] += 1

        y = list(parties.values())
        x = list(parties.keys())
        fig = go.Pie(labels=x, values=y)
        graph_div_parties = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title="Voter Party Affiliation"),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_parties"] = graph_div_parties

        x = [
            "v20state",
            "v21town",
            "v21primary",
            "v22general",
            "v23town",
        ]
        y = [
            voters.filter(v20state=True).count(),
            voters.filter(v21town=True).count(),
            voters.filter(v21primary=True).count(),
            voters.filter(v22general=True).count(),
            voters.filter(v23town=True).count(),
        ]
        fig = go.Bar(x=x, y=y)
        graph_div_participation = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title="Voter Past Participation"),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_participation"] = graph_div_participation
        context["birth_years"] = range(1920, 2010)

        return context
