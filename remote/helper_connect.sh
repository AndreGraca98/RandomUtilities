## RUN:  ################ OLD: bash connect_remote.sh [remote_name]
remote=$1
mode=$2

echo "Connecting to $remote"

if [[ $mode == "tabs" ]]; then
    ## Opens in different tabs
    # Open ssh terminal on remote
    gnome-terminal --tab -t 'SSH' -- bash -c "ssh -Xt $remote; exec bash"
    # Open htop on remote
    gnome-terminal --tab -t 'Monitoring CPU' -- bash -c "ssh -Xt $remote htop;exec bash"
    # Open gpustat on remote
    gnome-terminal --tab -t 'Monitoring GPU' -- bash -c "ssh -Xt $remote<<EOT
    gpustat -ucFP --watch --color;
    EOT;exec bash"

elif [[ $mode == "windows" ]]; then
    ## Opens in different windows
    # Open ssh terminal on remote
    gnome-terminal --geometry=140x37-0+0 --title="SSH" -- bash -c "ssh -Xt $remote; exec bash" 
    # Open htop on remote
    gnome-terminal --geometry=140x11-0+900 --title="Monitoring CPU" -- bash -c "ssh -Xt $remote htop;exec bash"
    # Open gpustat on remote
    gnome-terminal --geometry=140x3-0+670 --title="Monitoring GPU" -- bash -c "ssh -Xt $remote<<EOT
    gpustat -ucFP --watch --color;
    EOT;exec bash"
else
    echo "Mode $mode unkown! Must be either 'windows' or 'tabs'"
    exec bash
fi
