from django.db import models


class Subscriber (models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()


    def __str__(self):
        return 'Name: %sEmail: %s' % (self.name, self.email)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "My Subscribers"
