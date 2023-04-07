from accounts.views import UserRegisterView
from accounts.views import user_activate
from accounts.views import user_profile_view

from django.test import SimpleTestCase
from django.urls import resolve
from django.urls import reverse


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)
        # assert resolve(url).func.view_class == UserRegisterView, 'rweqgfqfewf'

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, user_profile_view)

    def test_activate_user_url_resolves(self):
        url = reverse('accounts:register_activate', kwargs={'sign': 'ioewutrljc3409ur90u43ri3j4'})
        self.assertEqual(resolve(url).func, user_activate)
