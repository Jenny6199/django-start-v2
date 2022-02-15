from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for basket_item in self:
            basket_item.product.quantity += basket_item.quantity
            basket_item.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.product.name}, ({self.quantity})'

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def get_total_quantity(self):
        """return total quantity for user"""
        _items = self.get_items_cached
        return sum(list(map(lambda x: x.quantity, _items)))

    def get_total_cost(self):
        _items = self.get_items_cached
        return sum(list(map(lambda x: x.product_cost, _items)))

    @property
    def product_cost(self):
        """return cost of all products this type"""
        return self.product.price * self.quantity

    @classmethod
    def get_items(self, user):
        """return total items for user"""
        _items = Basket.objects.filter(user=user).select_related()
        return _items

    # def delete(self, *args, **kwargs):
    #     """Переопределяет метод удаления товара"""
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(self.__class__, self).delete(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     """Переопределяет метод сохранения товара"""
    #     if self.pk:
    #         old_basket_item = Basket.objects.get(pk=self.pk)
    #         self.product.quantity -= self.quantity - old_basket_item.quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(self.__class__, self).save(*args, **kwargs)
