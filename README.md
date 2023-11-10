# Django-Multi-Tenant

## Descrição

Este repositório é um exemplo prático e simplificado de uma aplicação multi-inquilino usando o Django. O projeto destina-se a ilustrar a implementação do design multi-tenancy no Django, uma abordagem comum em SaaS (Software as a Service), onde uma única instância da aplicação serve a múltiplos clientes ou "inquilinos". Cada inquilino tem seu próprio ambiente isolado com dados protegidos e seguros, garantindo que as informações não sejam compartilhadas entre inquilinos.


## Pré-requisitos

Para executar este projeto, você precisa ter:

- Python 3.8 ou superior
- PostgreSQL
- Docker e Docker Compose (para execução em containers)

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/RailsonPinheiro2030/Django-Multi-Tenant
    ```

2. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ``` 

3. Crie um arquivo chamado `.env` onde você irá especificar as configurações de acesso ao banco:

    ```bash
    SECRET_KEY=django-secret-key
    DEBUG=1  # 0 para False, 1 para True
    POSTGRES_DB=nome_do_banco_postgres
    POSTGRES_USER=usuario_postgres
    POSTGRES_PASSWORD=senha
    POSTGRES_HOST=host_postgres
    POSTGRES_PORT=porta_postgres
    DOMAIN_NAME=dominio_do_tenant_publico
    APP_NAME=nome_do_tenant_publico
    ```


4. O domminio do tenant principal deve ser o nome do host que esta na $DOMAIN_NAME o nome deve ser defindo na $APP_NAME



## Executando a Aplicação com Docker

1. Construa e inicie os contêineres com Docker Compose:

    ```bash
    docker-compose up --build
    ```

    Isso irá construir as imagens Docker necessárias e iniciar os contêineres.

2. A aplicação estará acessível em `http://dominio_do_tenant_publico:8000`.



3. Para parar e remover os contêineres, use:

    ```bash
    docker-compose down
    ```

    Adicione `-v` para remover também os volumes.


5. Para criar um novo inquilino execupe o comando:
    ```bash
    docker-compose run djangotenants python manage.py create_tenant
    ```
    Voce sera solicitado pelo no input as informações do inquilino, o dominio deve ser o $DOMAIN_NAME.inquilino por exemplo: localhost.costomer


6. Para que voce possa acessar seu inquilino voce deve definir o host do inquilino como um subdominio no seu dns exemplo http://localhost.consumer:8000



7. Para criar um admin do inquilino voce deve usar o comando:
    ```bash
    docker-compose run djangotenants python manage.py create_tenant_superuser --schema=nome_do_schema_do_inquilino

    Assim voce pode acessar http://localhost.consumer:8000/admin e voce estara acessando o administrador do inquilino
    ```


8. para criar um novo app voce deve execultar o comando:
    ```bash
    docker-compose run djangotenants python manage.py startapp meu_app

    Apos concluir toda a criação do app voce deve colocalo em > settings.py TENANT_APPS(meu_app) se o seu app for destinado aos inquilinos,
    apos isso execulte o comando python manage.py makemigrations e python manage.py migrate_schemas --shared para que o app possa ser adicionado no schema dos inquilinos.
    ```


## Como funciona
    - Os locatários são identificados pelo nome do host (ou seja, locatário.domínio.com). 
    Essas informações são armazenadas em uma tabela no public schema. Sempre que uma solicitação é feita, o nome do host é usado para corresponder a um locatário no banco de dados. Se houver uma correspondência, o caminho de pesquisa será atualizado para usar o schema deste locatário. Portanto, a partir de agora todas as consultas ocorrerão no schema do locatário. Por exemplo, suponha que você tenha um locatário customer http://customer.example.com, qualquer solicitação recebida customer.example.com usará automaticamente o customer schema e disponibilizará o locatário na solicitação. Se nenhum inquilino for encontrado, um erro 404 será gerado. Isso também significa que você deve ter um locatário para seu domínio principal, normalmente usando o public schema.

    
    


## Estrutura de Diretórios e Arquivos

- `djangoTenants`: Diretório principal da aplicação.
- `urls_public.py`: Arquivo contendo as rotas públicas.

## Contribuição

Se deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua contribuição.
3. Faça suas alterações.
4. Envie um pull request.



## Licença

Este projeto está licenciado sob a licença MIT.

## Links úteis

https://django-tenants.readthedocs.io/en/latest/


## Contato

Para mais informações, entre em contato com o mantenedor do projeto: [railsonp560@gmail.com](mailto:railsonp560@gmail.com).

