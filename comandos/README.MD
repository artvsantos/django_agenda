Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

Configure o .gitignore

git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
teste 4

Migrando a base de dados do Django

python manager.py makemigrations
python manager.py migrate

Criando e modificando a senha de um super usuário Django

python manager.py createsuperuser
python manager.py changepassword USERNAME
