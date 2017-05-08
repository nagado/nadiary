from django import forms

class NewPostForm(forms.Form):
    header = forms.CharField(label='title', max_length=250, widget=forms.TextInput(attrs={'size': 100}))
    body = forms.CharField(label='text', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}))
