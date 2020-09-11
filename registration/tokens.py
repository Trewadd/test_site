from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import baseconv
from django.conf import settings


class AccountLoginTokenGenerator(PasswordResetTokenGenerator):

    @staticmethod
    def timestamp(self):
        return baseconv.base62.encode(int(settings.FALSE_TIME))

    def make_token(self, user):
        return self._make_token_with_timestamp(user, int(settings.FALSE_TIME))

    def _make_hash_value(self, user, timestamp=timestamp):
        login_timestamp = 0
        return str(user.pk) + user.password + str(login_timestamp) + str(timestamp)+ str(user.email)


account_token = AccountLoginTokenGenerator()

