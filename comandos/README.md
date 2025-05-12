Rodas server: 
python manage.py runserver

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
python manage.py startapp contact

# Configure o .gitignore
git initpython manage.py runserver

git add .
git commit -m 'Mensagem'
git log
git remote add origin URL_DO_GIT

Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact

Migrando a base de dados do Django: a cada mudança devemos colocar esse código
python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME