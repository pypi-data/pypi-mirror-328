__version__ = '1.0.1'
__all__ = (
    'TOTP',
    'generate_random_base32_secret',
)

from .otp import TOTP, generate_random_base32_secret
