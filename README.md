JWT Cracker for HS256 Algorithm
This script cracks an RS256 JWT token by modifying the header to use the HS256 algorithm and then attempts to decode the token using a wordlist for brute-forcing the secret key. It is useful for testing the security of JWT-based authentication systems.

Requirements

Python 3.x

PyJWT library

Install with: pip install pyjwt

Wordlist (e.g., rockyou2024.txt

How It Works
Decode the JWT Token: The script extracts the JWT header, decodes it, and then modifies it to use the HS256 algorithm instead of RS256.
Brute-force Attack: It attempts to decode the token with each key in the wordlist.
Output: The script prints the key that successfully decodes the token, along with the decoded payload.
Usage
Make sure the required libraries and wordlist are in place.
Run the script:
bash
Copy code

python jwt_cracker.py

Example Output
bash
Copy code
Successful decode with key: password123

Decoded JWT payload: {'sub': '', 'email': '', 'orgId': 87844, 'org': '', 'userType': 'OWNER', 'type': 'access', 'iat': 1729503250, 'exp': 1729506250}

Notes
Error Handling: The script handles expired, invalid, and unsupported tokens gracefully.

Security Warning: This script is for educational purposes and should only be used in a legal and authorized context (e.g., penetration testing with permission).
License
