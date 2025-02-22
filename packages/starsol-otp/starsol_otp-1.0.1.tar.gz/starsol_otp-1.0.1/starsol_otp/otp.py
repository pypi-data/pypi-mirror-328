import base64
import hashlib
import hmac
import secrets
import struct
import time
from typing import Any, Optional
from urllib.parse import quote

__all__ = (
    'TOTP',
    'generate_random_base32_secret',
)


def b32decode(s: str) -> bytes:
    """
    Decodes a Base32 encoded string into bytes, padding with '=' if necessary.

    :param s: The Base32 encoded string to be decoded.
    :type s: str
    :return: The decoded bytes from the Base32 encoded string.
    :rtype: bytes
    """
    if filler := len(s) % 8:
        s += '=' * (8 - filler)
    return base64.b32decode(s)


def get_hashlib_fn(s: str) -> Any:
    """
    Retrieves a hashing function from the hashlib module based on the given algorithm name.

    :param s: The name of the hashing algorithm to retrieve.
    :type s: str
    :return: The hash function corresponding to the given algorithm name.
    :rtype: Any
    :raises ValueError: If the algorithm name is not available in hashlib.
    """
    s = s.lower()
    if s not in hashlib.algorithms_available:
        raise ValueError(f'Unknown hashlib algorithm: {s}')
    return getattr(hashlib, s)


class TOTP:
    """
    Time-Based One-Time Password (TOTP) generator and verifier class.

    This class implements the TOTP algorithm as specified in RFC 6238. It can generate
    TOTP codes, verify them, and produce a URL for use with TOTP client applications.

    :ivar __secret: The secret key for the TOTP algorithm, base32 encoded.
    :ivar __secret_bytes: The secret key in bytes, decoded from base32.
    :ivar period: The time period in seconds for which each TOTP code is valid.
    :ivar digits: The number of digits in the TOTP code.
    :ivar digest: The hash function used to generate the TOTP code.

    :param secret: The secret key for the TOTP algorithm, base32 encoded.
    :param period: The time period in seconds for which each TOTP code is valid (default 30).
    :param digits: The number of digits in the TOTP code (default 6).
    :param digest: The hash function used to generate the TOTP code (default hashlib.sha1).

    :type secret: str
    :type period: int, optional
    :type digits: int, optional
    :type digest: Any, optional
    """

    __secret: str
    __secret_bytes: bytes
    period: int
    digits: int
    digest: Any

    def __init__(
        self,
        secret: str,
        period: int = 30,
        digits: int = 6,
        digest: Any = hashlib.sha1,
    ):
        self.__secret = secret
        self.period = period
        self.digits = digits
        if isinstance(digest, str):
            self.digest = get_hashlib_fn(digest)
        else:
            self.digest = digest
        self.__secret_bytes = b32decode(self.__secret)

    def generate(self, timestamp: Optional[int] = None) -> str:
        """
        Generates a token based on the provided timestamp or the current time if no timestamp is given.

        :param timestamp: The Unix timestamp used for generating the token. If None, the current time will be used.
        :type timestamp: int or None, optional
        :return: The generated token as a string.
        :rtype: str
        """

        timestamp = timestamp or int(time.time())
        counter = int(timestamp / self.period)
        return self._generate_with_counter(counter)

    def _generate_with_counter(self, counter: int) -> str:
        """
        Generate a token based on a given counter value using HMAC-based one-time password algorithm.

        :param counter: The counter value used to generate the token. Must be a positive integer.
        :type counter: int
        :raises ValueError: If the counter is negative.
        :return: A string representing the generated token.
        :rtype: str
        """
        if counter < 0:
            raise ValueError('Counter must be positive integer')
        hmac_digest = hmac.new(
            self.__secret_bytes, struct.pack('>Q', counter), self.digest
        ).digest()
        offset = hmac_digest[-1] & 0x0F
        binary = struct.unpack('>I', hmac_digest[offset : offset + 4])[0] & 2147483647
        token = binary % (10**self.digits)
        return f'{token:0{self.digits}}'

    def verify(
        self, code: str, timestamp: Optional[int] = None, window: int = 0
    ) -> bool:
        """
        Verifies if the given code is valid for a specific timestamp within a given window.

        This method checks if the provided code matches any generated code within the range of
        the current timestamp plus or minus the number of periods specified by the window, where
        each period is defined by the instance's period attribute.

        :param code: The code to verify.
        :type code: str
        :param timestamp: The reference timestamp for verification (defaults to current system time if None).
        :type timestamp: int or None, optional
        :param window: The number of periods to check on each side of the timestamp.
                       A window of 0 checks the code for the exact timestamp only.
        :type window: int, optional
        :return: True if the code is valid within the specified window, False otherwise.
        :rtype: bool
        """
        timestamp = timestamp or int(time.time())
        return any(
            self.generate(timestamp + self.period * offset) == code
            for offset in range(-window, window + 1)
        )

    def url(self, name: str, issuer: Optional[str] = None) -> str:
        """
        Generate a URL for a TOTP (Time-based One-Time Password) authentication.

        This method constructs a URL that can be used to configure a TOTP client
        (like Google Authenticator or similar apps) with the necessary parameters
        for generating time-based one-time passwords.

        :param name: The unique label for the account associated with the TOTP.
        :type name: str
        :param issuer: The name of the issuer or service providing the TOTP.
        :type issuer: str | None, optional
        :return: A URL string in the format expected by TOTP client applications.
        :rtype: str
        """
        label = quote(name)
        params = {
            'secret': self.__secret,
            'period': self.period,
            'digits': self.digits,
            'algorithm': self.digest().name.upper(),
        }
        if issuer:
            issuer = quote(issuer)
            label = f'{issuer}:{label}'
        params_str = '&'.join(f'{k}={v}' for k, v in params.items())
        return f'otpauth://totp/{label}?{params_str}'


def generate_random_base32_secret(length: int = 32) -> str:
    """
    Generate a random Base32 encoded secret string of a specified length.

    :param length: The desired length of the Base32 encoded secret. Default is 32 characters.
    :type length: int
    :return: A Base32 encoded string representing the secret.
    :rtype: str
    """
    bytes_len = (length * 5) // 8
    return base64.b32encode(secrets.token_bytes(bytes_len)).decode('utf-8')[:length]
