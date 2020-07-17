

import jwt as jwt
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1X2lkIjoiMTIzNDUifQ.lBTAPFU1xxDAi2Vrusfo67ypBai0vBr6O7KOt6CJf1s"
#print(jwt.decode(token, 'comp1531' , algorithms=['HS256']))
print(jwt.decode(token, verify=False))

# ## >> {'u_id': '12345'}

# No it is not signed correctly as line 5 was
# denied with a signature verification error

# HMACSHA256 Encoder
# HMACSHA256(
#   base64UrlEncode(header) + "." +
#   base64UrlEncode(payload),
  
# your-256-bit-secret
# )