from django.db import models

from django.conf import settings
from mainapp.models import Product


class Order(models.Model):
    """Модель заказа товара пользователем"""
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='обновлен',
        auto_now=True)
    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=FORMING)
    is_active = models.BooleanField(
        verbose_name='активен',
        default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        """Возвращает общее количество позиций в заказе"""
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        """Возвращает количество позиций в заказе по категориям"""
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        """Возвращает общую стоимость заказа"""
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    # переопределяем метод, удаляющий объект
    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    """Модель элемента заказа товара пользователем"""
    order = models.ForeignKey(
        Order,
        related_name="orderitems",
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0)

    def get_product_cost(self):
        """Возвращает стоимость позиции в заказе"""
        return self.product.price * self.quantity

    def delete(self):
        """Переопределяет метод удаления товара"""
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()
