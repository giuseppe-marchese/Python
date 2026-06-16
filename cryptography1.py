import hashlib

digest_bytes = hashlib.sha256(b"ciao").digest()     # bytes grezzi
digest_hex   = hashlib.sha256(b"ciao").hexdigest()  # stringa esadecimale leggibile
h = hashlib.sha256(b"ciao")

print(digest_bytes)   # b'\xb13\xa0\xc0\xe9...'
print(digest_hex)     # b133a0c0e9bee3be20163d2ad31d6248...
print(h.hexdigest())  # b133a0c0e9bee3be20163d2ad31d6248...

pippo = hashlib.sha256()
pippo.update(b"ciao ")
pippo.update(b"mondo")
print(f"ciao mondo: {pippo.hexdigest()}")   # equivalente a hashlib.sha256(b"ciao mondo").hexdigest()


print(hashlib.algorithms_available)   # mostra i diversi algoritmi quelli disponibili sul tuo sistema