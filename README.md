# Flix API

Flix API é uma API REST desenvolvida com Django e Django REST Framework (DRF) para gerenciamento de informações sobre filmes e atores. A autenticação é feita com JWT.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL (ou outro banco de dados configurado)
- JWT para autenticação
- Flake8 como linter

## Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
```

### 2. Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` e defina as configurações necessárias, como a chave secreta do Django e as credenciais do banco de dados.

### 5. Aplicar migrações
```bash
python manage.py migrate
```

### 6. Criar um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 7. Executar o servidor
```bash
python manage.py runserver
```

## Importação de Atores via CSV

A API inclui um comando para importar atores a partir de um arquivo CSV.

### Formato esperado do CSV
```csv
name,birthday,nationality
"Leonardo DiCaprio",1974-11-11,"Americano"
"Natalie Portman",1981-06-09,"Israelense"
```

### Executando a importação
```bash
python manage.py import_actors caminho/para/arquivo.csv
```

## Testes e Qualidade de Código

### Rodar testes automatizados
```bash
python manage.py test
```

### Analisar padrões de código com Flake8
```bash
flake8
```

## Endpoints Principais

A API possui endpoints para gerenciamento de filmes e atores. Abaixo estão alguns exemplos:

### Autenticação
- `POST /api/v1/token/` - Obter token JWT
- `POST /api/token/refresh/` - Atualizar token JWT

### Atores
- `GET /api/v1/actors/` - Listar todos os atores
- `POST /api/v1/actors/` - Criar um novo ator

### Filmes
- `GET /api/v1/movies/` - Listar todos os filmes
- `POST /api/v1/movies/` - Criar um novo filme

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias:
1. Fork este repositório.
2. Crie uma branch para sua funcionalidade: `git checkout -b minha-funcionalidade`
3. Faça commit das mudanças: `git commit -m "Adiciona nova funcionalidade"`
4. Envie para o repositório remoto: `git push origin minha-funcionalidade`
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

