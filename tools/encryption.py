import os
from pathlib import Path

import pandas as pd
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open(f"{Path.home()}/.fernet_key", "w") as f:
        f.write(str(key))


def get_key() -> bytes:
    with open(f"{Path.home()}/.fernet_key") as f:
        key = eval(f.readline())

    return key


def encrypt(message: str, key: bytes):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage


def decrypt(encMessage: str, key: bytes):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage


def create_credentials_csv(credentials_mid_path: str = "RandomUtilities/tools"):
    assert not os.path.isfile(str(Path.home() / credentials_mid_path / "credentials.csv")), "File credentials.csv already exists"
    # Comment the line above if you are sure you want to create a new credentials file
    key = get_key()

    data = [
        [encrypt("email@domain", key), encrypt("password", key)],
        [encrypt("email@domain", key), encrypt("password", key)],
        [encrypt("email@domain", key), encrypt("password", key)],
    ]
    df = pd.DataFrame(data, columns=["email", "password"], dtype=str)
    df.set_index(pd.Index([decrypt(d[0], key).split("@")[1].split(".")[0] for d in (data)]), inplace=True)
    df.to_csv(str(Path.home() / credentials_mid_path / "credentials.csv"), sep=" ", index_label="index")  # , index=None)


def get_data(domain: str, column_name: str, credentials_mid_path: str = "RandomUtilities/tools"):
    assert column_name in ["email", "password"], f"Column name {column_name} does not exist. Choose from [password, email]"

    key = get_key()
    df = pd.read_csv(str(Path.home() / credentials_mid_path / "credentials.csv"), sep=" ", index_col="index")  # , sep=" ")

    assert domain in df.index, f"Domain '{domain}' does not exist. Choose from {df.index.values}"

    return decrypt(eval(df.loc[domain, column_name]), key)


def get_email(domain: str):
    return get_data(domain=domain, column_name="email")


def get_pwd(domain: str):
    return get_data(domain=domain, column_name="password")


def get_credentials(domain: str):
    return get_email(domain=domain), get_pwd(domain=domain)


if __name__ == "__main__":
    # generate_key()
    # create_credentials_csv()

    # print(get_credentials("isr"))
    # print(get_credentials("sapo"))
    # print(get_credentials("gmail"))
    # print(get_credentials("google"))

    pass
