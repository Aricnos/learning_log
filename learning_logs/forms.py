from django import forms
from .models import Topic, Entry

class TopicForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForms(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}