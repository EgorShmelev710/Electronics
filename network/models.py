from django.db import models

NULLABLE = {'null': True, 'blank': True}


class ContactInfo(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class NetworkEntity(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    contacts = models.OneToOneField(ContactInfo, on_delete=models.CASCADE, verbose_name='контакты')
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                               verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_level(self):
        """
        Определяет уровень в иерархии по отношению к поставщику.
        """
        level = 0
        current_entity = self
        while current_entity.supplier:
            level += 1
            current_entity = current_entity.supplier
        return level

    def __str__(self):
        return f'{self.title} (Уровень иерархии: {self.get_level()})'

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'
