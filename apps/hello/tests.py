import datetime

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from apps.hello.models import Profile


class ModelProfileTests(TestCase):
    def test_str(self):
        "tests if str returns correct string"
        obj = Profile.objects.create(name='Serhiy', surname='Stetskovych')
        self.assertEqual(str(obj), 'Serhiy Stetskovych')


class HomePageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = Profile(name='Serhiy', surname='Stetskovych')
        self.obj.date_of_birth = datetime.date(year=1986, month=1, day=24)
        self.obj.bio = 'my bio'
        self.obj.email = 'mail@email.com'
        self.obj.jabber = 'jabber@jabber.com'
        self.obj.skype = 'skypename'
        self.obj.other_contacts = 'othercontacts'
        self.obj.save()

    def test_home_page(self):
        "tests if main page exists and has a needed model"

        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.context['profile']), Profile)
        self.assertEqual(response.context['profile'].id, self.obj.id)
