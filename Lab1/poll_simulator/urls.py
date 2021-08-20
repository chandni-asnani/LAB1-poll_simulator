from django.contrib import admin
from django.urls import path, include
from .views import VoteView, VoteResultView, VoteReportView,AddCandidateView
from django.views.generic import TemplateView


urlpatterns = [
    path("vote", VoteView.as_view(), name="vote"),
    path("poll_result",  VoteResultView.as_view(), name="poll_result"),
    path("voting_report", VoteReportView.as_view(), name="voting_report"),
    path("add", AddCandidateView.as_view(), name="add"),


]