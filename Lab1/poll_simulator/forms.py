from django import forms
from .models import Candidates,Vote

class VoteForm(forms.ModelForm):
    nominee = forms.ModelChoiceField(
        queryset=Candidates.objects.all(),
        widget=forms.RadioSelect
    )
    class Meta:
        model = Vote
        fields = ('studentid','nominee')


class AddCandidateForm(forms.ModelForm):
    class Meta:
        model= Candidates
        fields = '__all__'
