from django import forms

class TicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())
    priority = forms.ChoiceField(required=False)

    def __init__(self, choices=None, initial=None, data=None):
        forms.Form.__init__(self, data)

        if choices:
            self.fields['priority'].choices = choices

        if initial:
            self.fields['priority'].initial = initial
