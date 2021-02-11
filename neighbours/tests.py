
from __future__ import unicode_literals
from django.test import TestCase
from .models import neighbourhood,Business,Profile,healthservices

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = neighbourhood(neighbourhood = 'nyamirambo')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,neighbourhood))

    def test_save(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood)>0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = neighbourhood(neighbourhood = 'nyamirambo')
        self.neighbourhood.save_neighbourhood()

        self.igihozo = Profile(avatar = '/avatar/default.png',description = 'happy neighbour',username = 'igihozo',name='stella',email='igihozo@user.com')

    def test_save(self):
        self.igihozo.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class BusinessTestClass(TestCase):
    def setUp(self):
        self.igihozo = Profile(first_name = 'igihozo',last_name='stella',username='igihozo',email='istellamarlyne@gmail.com')
        self.igihozo.save_profile()

        self.business = Business(name='Coffee Shop',email='coffeeshop@rwanda.com',location = 'Nyamirambo',user = self.igihozo)

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(profiles)>0)

    def tearDown(self):
        Profile.objects.all.delete()
        Business.objects.all().delete()

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Physiotherapy = healthservices(healthservices='Physiotherapy')

    def test_instance(self):
        self.assertTrue(isinstance(self.Physiotherapy,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Physiotherapy.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Physiotherapy.delete_healthservices('Physiotherapy')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)
