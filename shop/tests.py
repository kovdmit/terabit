from django.contrib.auth import get_user_model
# from somelib import send_email_notification
from django.test import TestCase


User = get_user_model()


def user_log_in(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExists:
        raise ValueError('User not found')

    if user.check_password(password):
        # send_email_notification('Вы вошли в систему')
        return True
    else:
        return False


class LoginTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth',
                                            email='e@ma.il',
                                            password='123')

    def test_get_user_false(self):
        """Проверяем вызов исключения при поиске пользователя."""
        self.assertRaisesRegex(ValueError,
                               'User not found',
                               user_log_in('False', 'False'))

    def test_get_user_true(self):
        """Проверяем результат отправки сообщения."""
        user_false = user_log_in(self.user.email, 'False')
        user_true = user_log_in(self.user.email, self.user.password)
        self.assertFalse(user_false)
        self.assertTrue(user_true)
