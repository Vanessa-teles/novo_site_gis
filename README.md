# Gislaine Teles Engenharia - README

Este é um projeto Django para o site da Engenheira Gislaine Teles, especializada em vistorias técnicas e laudos para imóveis.

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django:

```
gislaine_site/
├── core/                      # App principal
│   ├── migrations/            # Migrações do banco de dados
│   ├── static/                # Arquivos estáticos
│   │   └── core/
│   │       ├── css/           # Arquivos CSS
│   │       ├── js/            # Arquivos JavaScript
│   │       └── images/        # Imagens
│   ├── templates/             # Templates HTML
│   │   └── core/
│   │       ├── base.html      # Template base
│   │       ├── index.html     # Página inicial
│   │       └── contato.html   # Página de contato
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py               # Formulário de contato
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                # URLs do app
│   └── views.py               # Views do app
├── gislaine_engenharia/       # Configurações do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configurações do Django
│   ├── urls.py                # URLs do projeto
│   └── wsgi.py
├── media/                     # Arquivos de mídia (uploads)
├── static/                    # Arquivos estáticos coletados
├── venv/                      # Ambiente virtual Python
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py                  # Script de gerenciamento do Django
└── requirements.txt           # Dependências do projeto
```

## Requisitos

- Python 3.8+
- Django 5.2+
- Pillow (para processamento de imagens)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gislaine-engenharia.git
cd gislaine-engenharia
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

6. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

7. Acesse o site em: http://127.0.0.1:8000/

## Configuração de E-mail

O projeto está configurado para enviar e-mails através do Gmail. Para usar sua própria conta:

1. Abra o arquivo `gislaine_engenharia/settings.py`
2. Atualize as seguintes configurações:
```python
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app'
```

Nota: Para o Gmail, você precisa usar uma "Senha de App" e não sua senha normal.

## Personalização

### Imagens
- Substitua as imagens em `core/static/core/images/` com suas próprias imagens
- Atualize os caminhos nos templates conforme necessário

### Conteúdo
- Edite os templates em `core/templates/core/` para atualizar o conteúdo do site
- Personalize o CSS em `core/static/core/css/custom.css`

## Implantação

Para implantar em produção:

1. Configure as variáveis de ambiente para produção
2. Colete os arquivos estáticos:
```bash
python manage.py collectstatic
```

3. Configure um servidor web como Nginx ou Apache
4. Use Gunicorn ou uWSGI como servidor WSGI

## Contato

Para dúvidas ou suporte, entre em contato com o desenvolvedor.
