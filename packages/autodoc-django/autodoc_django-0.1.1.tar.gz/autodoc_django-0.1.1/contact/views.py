from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import render
from ottoboni.contact import forms
from ottoboni.contact import models
from ottoboni.core.flags import STATE_CHOICES


class Contact(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = 'obrigado'

    def get_initial(self):
        if self.request.GET:
            initial = self.request.GET.dict()
            return initial
        else:
            return super(Contact, self).get_initial()

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['professions'] = models.Profession.objects.all()
        context['subjects'] = models.Subject.objects.filter(is_active=True).order_by('order')
        context['states'] = STATE_CHOICES
        return context

    def form_valid(self, form):
        form.save()
        body = 'Nome: {} <br>\
        Email: <a href="{}" target="_blank">{}</a><br>\
        Telefone: ({}) {} Ramal: {}<br>\
        Empresa: {} <br>\
        Área de atuação: {} <br>\
        CEP: {} <br>\
        Endereço: {}, Número {} {}, {} - {}, {} <br>\
        Assunto: {} <br>\
        Mensagem: {} <br>\
        Dispositivo: {}'.format(
            form.cleaned_data.get('name') or 'Não informado',
            form.cleaned_data.get('email') or 'Não informado',
            form.cleaned_data.get('email') or 'Não informado',
            form.cleaned_data.get('tel_prefix') or 'Não informado',
            form.cleaned_data.get('tel') or 'Não informado',
            form.cleaned_data.get('tel_sufix') or 'Não informado',
            form.cleaned_data.get('company') or 'Não informado',
            form.cleaned_data.get('profession') or 'Não informado',
            form.cleaned_data.get('postal') or 'Não informado',
            form.cleaned_data.get('address') or 'Não informado',
            form.cleaned_data.get('address_number') or 'Não informado',
            form.cleaned_data.get('address_complement') or '',
            form.cleaned_data.get('district') or 'Não informado',
            form.cleaned_data.get('city') or 'Não informado',
            form.cleaned_data.get('state') or 'Não informado',
            form.cleaned_data.get('subject') or 'Não informado',
            form.cleaned_data.get('message') or 'Não informado',
            form.cleaned_data.get('device') or 'Não detectado',
        )

        send_mail(
            'Contato do site',
            'Seguem os dados do cliente',
            settings.DEFAULT_FROM_EMAIL,
            settings.ADMINS_CONTATO,
            html_message=body,
            fail_silently=False,
        )

        return super(Contact, self).form_valid(form)


class ContactSuccess(View):
    def get(self, request):
        context = {'show_google_conversion': not settings.DEV}
        # context = { 'show_google_conversion': not settings.DEBUG }
        return render(request, 'success.html', context)
