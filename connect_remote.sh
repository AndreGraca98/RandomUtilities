## RUN: bash connect_remote.sh [remote_name]

if [ -z "$1" ]; then
    remote=servidor
else
    remote=$1
fi

echo "Connecting to $remote"


# Open htop on remote
gnome-terminal --geometry=140x11-0+900 --title="Monitoring CPU" -- bash -c "ssh -Xt $remote htop;exec bash"

# Open gpustat on remote
gnome-terminal --geometry=140x3-0+670 --title="Monitoring GPU" -- bash -c "ssh -Xt $remote<<EOT
conda activate i3d; 
gpustat -ucFP --watch --color;
EOT;exec bash"

# Open ssh terminal on remote
gnome-terminal --geometry=140x37-0+0 --title="SSH" -- bash -c "ssh -Xt $remote; exec bash" 

