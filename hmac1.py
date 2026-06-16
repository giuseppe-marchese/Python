import hmac
import hashlib

chiave    = b"chiave_segreta"
messaggio = b"dati da autenticare"

tag = hmac.new(chiave, messaggio, digestmod=hashlib.sha256)
print(tag.hexdigest())
# 6b4e9e7b2f8c1a3d…
