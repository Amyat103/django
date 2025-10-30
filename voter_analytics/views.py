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
        return qs


class VoterDetailView(DetailView):
    """View to display a single voter's details."""

    template_name = "voter_analytics/voter_detail.html"
    model = Voter
    context_object_name = "voter"

    def get_context_data(self, **kwargs):
        """Provide context variable for the template."""

        context = super().get_context_data(**kwargs)
        r = context["voter"]

        # get data for graphs
        year_of_birth = r.date_of_birth.year

        party_affiliation = r.party_affiliation

        participated_v20 = r.v20state == "Y"
        participated_v21Town = r.v21town == "Y"
        participated_v21Primary = r.v21primary == "Y"
        participated_v22General = r.v22general == "Y"
        participated_v23Town = r.v23town == "Y"

        people = Voter.objects.all()

        # Pie chart plot
        pie_x = year_of_birth
        pie_y = people
        fig = go.Pie(labels=pie_x, values=pie_y)
        title_text = "Voter Age Distribution"
        graph_div_ages = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title=title_text),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_ages"] = graph_div_ages

        # Bar chart plot
        bar_x = party_affiliation
        bar_y = people
        fig = go.Bar(labels=bar_x, values=bar_y)
        title_text = "Voter Party Affiliation"
        graph_div_parties = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title=title_text),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_parties"] = graph_div_parties

        # Histogram plot
        his_x = [
            participated_v20,
            participated_v21Town,
            participated_v21Primary,
            participated_v22General,
            participated_v23Town,
        ]
        his_y = people
        fig = go.Histogram(x=his_x, y=his_y)
        title_text = "Voter Past Participation"
        graph_div_participation = plotly.offline.plot(
            {
                "data": [fig],
                "layout": go.Layout(title=title_text),
            },
            auto_open=False,
            output_type="div",
        )
        context["graph_div_participation"] = graph_div_participation
