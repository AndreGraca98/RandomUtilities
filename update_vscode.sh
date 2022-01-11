
read -p 'Make sure your work is saved before updating... Ready? [y]/n: ' opt

if [ "$opt" == "y" ] || [ "$opt" == "Y" ] || [ -z "$opt" ]; then
    echo "Updating vscode..." 
    sudo pkill -9 code
    wget 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64' -O /tmp/code_latest_amd64.deb
    sudo dpkg -i /tmp/code_latest_amd64.deb
    code
else
    echo "Did not update vscode..."
fi

