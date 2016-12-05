from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    jabber = models.EmailField(null=True)
    skype = models.CharField(max_length=200, null=True)
    other_contacts = models.TextField(null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
