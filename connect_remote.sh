## RUN: bash connect_remote.sh [remote_name]

if [ -z "$1" ]; then
    remote=servidor
else
    remote=$1
fi

echo "Connecting to $remote"


# Open ssh terminal on remote
gnome-terminal --geometry=140x39 --title="SSH" -- bash -c "ssh -Xt $remote; exec bash" 

# Open gpustat on remote
gnome-terminal --geometry=140x3 --title="Monitoring GPU" -- bash -c "ssh -Xt $remote<<EOT
conda activate i3d; 
gpustat -ucFP --watch --color;
EOT;exec bash"

# Open htop on remote
gnome-terminal --geometry=140x11 --title="Monitoring CPU" -- bash -c "ssh -Xt $remote htop;exec bash"

