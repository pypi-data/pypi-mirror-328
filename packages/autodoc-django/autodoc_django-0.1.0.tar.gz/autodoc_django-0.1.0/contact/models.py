from django.db import models


class Profession(models.Model):
    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Área de atuação'
        verbose_name_plural = 'Áreas de atuação'


class Subject(models.Model):
    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(verbose_name='Ativo?', default=True)
    order = models.IntegerField('Ordem', null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'


class Contact(models.Model):
    def __str__(self):
        return str(self.email)

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    tel_prefix = models.IntegerField('DDD')
    tel = models.CharField('Telefone', max_length=11)
    tel_sufix = models.IntegerField('Ramal', null=True, blank=True)
    company = models.CharField('Empresa', max_length=100, null=True, blank=True)
    profession = models.ForeignKey(
        Profession,
        verbose_name='Área de atuação',
        related_name='contacts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    postal = models.IntegerField('CEP', null=True, blank=True)
    state = models.CharField('Estado', max_length=200, null=True, blank=True)
    city = models.CharField('Cidade', max_length=200, null=True, blank=True)
    district = models.CharField('Bairro', max_length=200, null=True, blank=True)
    address = models.CharField('Endereço', max_length=200, null=True, blank=True)
    address_number = models.IntegerField('Número', null=True, blank=True)
    address_complement = models.CharField(
        'Complemento', max_length=200, null=True, blank=True
    )
    subject = models.ForeignKey(
        Subject,
        verbose_name='Assunto',
        related_name='contacts',
        on_delete=models.CASCADE,
    )
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Enviado em', auto_now_add=True)
    device = models.CharField('Dispositivo', max_length=100, null=True, blank=True)
    its_budget = models.BooleanField('É um orçamento?', default=False)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
