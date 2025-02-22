Usage example
```python
from starsol_otp import TOTP, generate_random_base32_secret

secret = generate_random_base32_secret()
totp = TOTP(secret)

code = totp.generate()
print(code)
print(totp.verify(code))
```
