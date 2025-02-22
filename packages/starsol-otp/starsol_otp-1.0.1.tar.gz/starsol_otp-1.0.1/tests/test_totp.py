import time
import unittest

from starsol_otp import TOTP, generate_random_base32_secret


class TestTOTP(unittest.TestCase):
    def setUp(self) -> None:
        self.secret = generate_random_base32_secret()

    def test_totp(self) -> None:
        totp = TOTP(self.secret)
        token = totp.generate()
        self.assertTrue(totp.verify(token))
        wrong_token = token[:-1] + '0' if token[-1] != '0' else '9'
        self.assertFalse(totp.verify(wrong_token))

    def test_totp_period(self) -> None:
        totp = TOTP(self.secret, period=60)
        timestamp = int(time.time())
        token = totp.generate()
        self.assertTrue(totp.verify(token))
        self.assertTrue(totp.verify(token, timestamp=timestamp + 58, window=1))
        self.assertFalse(totp.verify(token, timestamp=timestamp + 122, window=1))
        self.assertTrue(totp.verify(token, timestamp=timestamp + 118, window=2))

    def test_totp_digits(self) -> None:
        totp = TOTP(self.secret, digits=8)
        token = totp.generate()
        self.assertEqual(len(token), 8)
        self.assertTrue(totp.verify(token, window=1))
