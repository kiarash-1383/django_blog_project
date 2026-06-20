from random import choices
from .models import *
from django import  forms

class TicketForm(forms.Form):

    subject = (
         ('bog', 'bog') ,
         ('pirincimpe', 'pirincimpe') ,
         ('nothing', 'nothing')
    )
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    type = forms.ChoiceField(choices = subject)

    def clean_name(self):

        name = self.cleaned_data['name']
        if name.isnumeric():
            raise forms.ValidationError('Name shudent be numeric')
        else:
            return name

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'title' ,'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.isnumeric():
            raise forms.ValidationError('Title shudent be numeric')
        return title