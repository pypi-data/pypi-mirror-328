from django import forms
from ottoboni.contact import models
from ottoboni.core.flags import STATE_CHOICES


class ContactForm(forms.ModelForm):

    subject = forms.ModelChoiceField(queryset=models.Subject.objects.none(), empty_label='Assunto')
    profession = forms.ModelChoiceField(queryset=models.Profession.objects.all(), empty_label='Área de atuação', required=False)
    postal = forms.CharField()
    state = forms.ChoiceField(label='Estado', choices=STATE_CHOICES)

    class Meta:
        model = models.Contact
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = models.Subject.objects.filter(is_active=True).order_by('order')

    def clean_postal(self):
        postal = self.cleaned_data['postal']
        postal = postal.replace('-', '')
        return postal
