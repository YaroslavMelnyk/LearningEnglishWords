from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=50, verbose_name="User name")
    email = models.EmailField(max_length=100, verbose_name="Email")
    subject = models.CharField(max_length=50, verbose_name="Subject")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date/Time")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return "%s (%s) %s..." % (self.username, self.email, self.message[0:10])
