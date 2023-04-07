from accounts.models import User

from django.test import TestCase


class TestModels(TestCase):
    username = None

    @classmethod
    def setUpTestData(cls):
        cls.username = 'user_1'

        User.objects.create(
            username=cls.username,
            password='123qwe!@#',
            email='user_1@test.com',
            first_name='Test'
        )

    def setUp(self):
        self.user = User.objects.get(username=self.username)

    def test_avatar_label_is_correct(self):
        avatar_label = self.user._meta.get_field('avatar').verbose_name
        self.assertEqual(avatar_label, 'avatar')

    def test_city_max_length(self):
        meta = self.user._meta.get_field('city')
        self.assertEqual(meta.max_length, 50)
        self.assertTrue(meta.null)
        self.assertTrue(meta.blank)

    def test_convert_user_to_str(self):
        self.assertEqual(str(self.user), self.username)
