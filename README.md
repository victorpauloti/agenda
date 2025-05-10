Iniciar o projeto Django

```
python -m venv venv
. .venv/bin/activate
pip install django
django-admin startproject setupe .
python manage.py startapp agenda

criar app e add no settings

Migrations:
makemigrations - criando a migracao
migrate = aplica as lateracoes

```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```
```
criar app e add no settings

Migrations:
makemigrations - criando a migracao
migrate = aplica as lateracoes

Registrar o model no admin:
No admin do app criar uma classe e importar o models do app,
 usei recurso decorator do python (@admin.register(models.Contact))
 usar list_display (tupla) para listar campos no admin



```