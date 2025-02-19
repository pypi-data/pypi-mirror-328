from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
import csv
from django.http import HttpResponse

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tel_str', 'address_str', 'subject', 'message', 'profession', 'device',
                    'created_at', 'its_budget']
    ordering = ('-created_at', )
    search_fields = ('name', 'email', 'tel', 'city')
    list_filter = ('subject', 'profession', 'device', 'its_budget')
    actions = ['export_as_csv']

    def tel_str(self, obj):
        return '({}) {}'.format(obj.tel_prefix, obj.tel)
    tel_str.short_description = 'Telefone'

    def address_str(self, obj):
        text = 'Rua: <strong>{}</strong> | Bairro: <strong>{}</strong> | Nº <strong>{}</strong> | Complemento: <strong>{}</strong> | Cidade/Estado: <strong>{}/{}</strong>'.format(
            obj.address or '-', obj.district or '-', obj.address_number or '-', obj.address_complement or '-', obj.city or '-', obj.state or '-')

        return mark_safe(text)
    address_str.short_description = 'Endereço'

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "Exportar para CSV"


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', )
    ordering = ('title', )
    search_fields = ('title', )


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    ordering = ['order']
    search_fields = ('title', )
    list_editable = ['order']
