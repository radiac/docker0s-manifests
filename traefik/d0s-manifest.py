import crypt

from docker0s import App


class Traefik(App):
    env = {
        "LETSENCRYPT_EMAIL": "user@example.com",
        "DASHBOARD_URL": "traefik.example.com",
        "DASHBOARD_USER": "admin",
        "DASHBOARD_PASSWORD": "$1$vYYHQPAB$mY2QdlKwH0rknziBYKTV21",
    }

    @App.command
    def mkpass(self):
        password = input("Password: ")
        encoded = crypt.crypt(password, crypt.METHOD_MD5)
        print(encoded)
