from django.test import TestCase
from .models import Images, Profiles, Comments
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.




class ProfileTestClass(TestCase):
    def setup (self):
        self.user= User(username='hello',email='hello@gmail.com', password='hello123')
        self.user.save()

        self.profile=Profiles(images='/posts',bio='kenya love',user=self.user)
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profiles))

    def test_save_method(self):
        self.bio.save_bio()
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)


    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)

    def tearDown(self):
        Image.objects.all().delete()
