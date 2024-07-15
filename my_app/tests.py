from django.test import TestCase, SimpleTestCase
from django.urls import reverse

#home page test
#check respone status
class HomeTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    # check response template
    def test_home_page(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

#about page test
#check respone status
class aboutTest(SimpleTestCase):
    def test_about_page_status(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    # check response template
    def test_about_page(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'about.html')

# contact page test
#check respone status
class contactTest(SimpleTestCase):
    def test_contact_page_status(self):
        url = reverse('contact')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    # check response template
    def test_contact_page(self):
        url = reverse('contact')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'contact.html')

    