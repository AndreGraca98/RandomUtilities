# remote

## Usage

Assuming user is in `RandomUtilities/remote/`

### Connect to a remote domain and open gpustats and htop

```bash
bash connect_remote.sh
# OR
bash connect_remote.sh [remote_user@remote_domain] ['windows' | 'tabs']

```

## In this folder

- [x]  `connect_remote.py` :: creates new gnome terminal window and calls *helper_connect.py*
- [x]  `helper_connect.py` :: creates new tabs and runs htop and gpustats
