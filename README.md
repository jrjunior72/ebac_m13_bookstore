# EBAC Módulo 13 — BookStore App

Este projeto é parte do curso de Python da EBAC, módulo 13, que introduz o uso do Django REST Framework (DRF).

## 🔧 Tecnologias utilizadas

- Python 3.13.5
- Django
- Django REST Framework
- Poetry

## 🚀 Setup do projeto 

Lista dos principais comandos usados para configurar o projeto e o ambiente.

### Criar o ambiente com Poetry
poetry init

### Instalar o Django
poetry add django

### Criar o projeto Django
poetry run django-admin startproject ebac_m13_bookstore .

### Instalar o Django REST Framework
poetry add djangorestframework

### Atualizar dependências
poetry update

### Rodar o servidor
poetry run python manage.py runserver

### Criar nova branch
git checkout -b project_setup

### Adicionar arquivos ao stage
git add .

### Commit das alterações
git commit -m "Configuração inicial do DRF e atualização do README"

### Subir a branch para o GitHub
git push origin project_setup

### Status
### Status
![Tests](https://github.com/jrjunior72/ebac_m13_bookstore/actions/workflows/workflow-pr.yml/badge.svg)


