from django.shortcuts import render
from django.db.models import Count
from django.db.models.aggregates import Max
from .models import Candidates,Vote
from.forms import VoteForm, AddCandidateForm
from django.views.generic import View,ListView

class VoteView(View):
    def get(self, request):
        form = VoteForm()
        return render(request, 'vote.html',{'form':form})
    
    def post(self,request):
        form = VoteForm(request.POST)
        # import code; code.interact(local=dict(globals(), **locals()))
        if form.is_valid():
            studentid= form.cleaned_data['studentid']
            nominee= form.cleaned_data['nominee']
            form.save()
            return render(request, 'voted.html', {"message": "Voted Successfully"})
        else:
            return render(request, 'voted.html', {"message": form.errors["studentid"]})

class VoteResultView(ListView):
    model = Vote
    template_name = "poll_result.html"
    context_object_name = "form"

    def get_queryset(self,**kwargs):
        result = Vote.objects.values('nominee__candidate').annotate(vote_count=Count('nominee')).order_by()

        list(result.values("nominee__candidate", "vote_count"))
        return result


class VoteReportView(ListView):
    model = Vote
    template_name = "voting_report.html"
    context_object_name = "form"

    def get_queryset(self,**kwargs):
        result = Vote.objects.values('nominee__candidate').annotate(vote_count=Count('nominee')).order_by('-vote_count')
        # import code; code.interact(local=dict(globals(), **locals()))
        list(result.values("nominee__candidate", "vote_count"))
        return result[:2]
        

class AddCandidateView(View):
    def get(self, request):
        form = AddCandidateForm()
        return render(request, 'add.html',{'form':form})
    
    def post(self,request):
        form = AddCandidateForm(request.POST)
        # import code; code.interact(local=dict(globals(), **locals()))
        if form.is_valid():
            form.save()
            return render(request, 'add.html',{'form' :form, "message": "Added Successfully"})    




