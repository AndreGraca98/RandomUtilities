
if [ -z "$1" ]; then
    remote=servidor
else
    remote=$1
fi


if [ -z "$2" ]; then
    mode="windows"
else
    mode=$2
fi


gnome-terminal --window -- bash -c "bash helper_connect.sh $remote $mode"