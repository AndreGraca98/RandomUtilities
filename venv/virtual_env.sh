# RUN: source virtual_env.sh
if ! [ -z $1 ]; then
    name=$1
else
    name=utils
fi

echo 'Installing conda packages...'
conda create --name $name --file conda_pkgs.txt
conda activate $name

echo 'Installing pip packages...'
pip install -r pip_pkgs.txt 

cd ..

# # To create pkgs files -> RUN: 
# conda list --explicit > conda_pkgs.txt
# pip list --format=freeze > pip_pkgs.txt