from django.db import models
from django.utils import timezone
from app_base.models import BaseModel


class Contact(BaseModel):
    class Meta:
        db_table = 'contact'
        ordering = ['first_name', 'last_name']
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=True)
    prefix = models.IntegerField(null=False, blank=False)
    ddd = models.IntegerField(null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def mask_phone(self):
        return f'+{self.prefix} ({self.ddd}) {self.phone[:1]}.{self.phone[1:5]}-{self.phone[5:]}'
