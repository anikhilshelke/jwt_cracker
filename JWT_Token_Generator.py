import jwt
import datetime

# Secret key for signing the token
SECRET_KEY = 'jwtldw02'

# Header
headers = {
    "alg": "HS256",
    "typ": "JWT"
}

# Payload
payload = {
    "username": "admin",  # Example username for admin
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Expiration set to 1 hour
    "iat": datetime.datetime.utcnow()  # Issued at time
}

# Encode the token using the secret key and HS256 algorithm
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=headers)

# Print the JWT
print(f"Generated JWT: {token}")
