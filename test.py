from sigstore.oidc import IdentityToken

with open("./oidc-token.txt") as f:
    content = f.read().rstrip()
    token = IdentityToken(content)
    print("OK")
