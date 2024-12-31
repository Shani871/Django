from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100,label="Email")
    name = forms.CharField(max_length=100,label="Name")
    feedback = forms.CharField(widget=forms.Textarea,label="Feedback")
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['feedback'].widget.attrs.update({'class': 'form-control'})