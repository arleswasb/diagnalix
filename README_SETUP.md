# Diagnalix - Guia de Configuração (Linux/Ubuntu)

Este documento descreve o passo a passo para subir a estrutura do projeto Diagnalix em um ambiente Linux do zero.

## 1. Pré-requisitos do Sistema
Certifique-se de ter as bibliotecas de compilação e o Docker instalados:
* `sudo apt update && sudo apt install -y build-essential libpq-dev python3-dev redis-server docker.io docker-compose`
* Adicionar usuário ao grupo docker: `sudo usermod -aG docker $USER` (requer novo login).

## 2. Gerenciamento de Python (uv)
O projeto utiliza o `uv` para máxima performance:
* Instalação: `pipx install uv`
* Criar ambiente: `uv venv`
* Ativar: `source .venv/bin/activate`
* Instalar dependências: `uv pip install -r backend/requirements.txt`

## 3. Subindo a Infraestrutura (Docker)
Na raiz do projeto, onde está o `docker-compose.yml`:
```bash
# Subir containers em background
docker-compose up -d

# Verificar status
docker ps
