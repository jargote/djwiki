from django import forms


class WikiPageForm(forms.Form):
    """This form is used to clean data for a WikiPage and a ChangeLog instance.
    """

    body = forms.CharField(label='Page Body', widget=forms.Textarea)
    comments = forms.CharField(label='Comments', widget=forms.Textarea)
