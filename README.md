# RandomUtilities

Random utility files

## Usage

Assuming user is in `RandomUtilities/`

```bash
cd venv
source virtual_env.sh
```

## In this repo

- [x]  `remote/update_vscode.sh` :: update vscode
- [x]  `remote/connect_remote.sh` :: connect to remote
- [x]  `fresh_install.sh` :: install important things such as anaconda, gparted, git...  
- [x]  `personal_email.sh` :: sends an email with subject, body and an attacment using bash mailutils
- [x]  `email_tools/email_class.py` :: send an email with subject, body and an attacment using python smtplib
- [x]  `email_tools/runner_wrapper.py` :: wrapper to send an email notification if error occurs
- [x]  `email_tools/encryption.py` :: encrypt and decrypt data using Fernet encryption. Create and retrieve encrypted credentials

## Test email tools Usage

Assuming user is in `RandomUtilities/`

```bash
python email_test_test_file.py
```
