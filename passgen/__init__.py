import secrets
import string


def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(char.islower() for char in password)
                and any(char.isupper() for char in password)
                and sum(char.isdigit() for char in password) >= 3):
            break
    return password


def main():
    password = generate_password(16)
    print(f'Generated password: {password}')


if __name__ == '__main__':
    main()
