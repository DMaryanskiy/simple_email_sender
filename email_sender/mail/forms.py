from django import forms

class EmailForm(forms.Form):
    """ an email form with subject, recipents and message fields """
    subject = forms.CharField()
    recipents = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
