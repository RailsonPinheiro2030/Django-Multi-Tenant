# Django-Multi-Tenant

## Descrição

Este repositório é um exemplo prático e simplificado de uma aplicação multi-inquilino usando o Django. O projeto destina-se a ilustrar a implementação do design multi-tenancy no Django, uma abordagem comum em SaaS (Software as a Service), onde uma única instância da aplicação serve a múltiplos clientes ou "inquilinos". Cada inquilino tem seu próprio ambiente isolado com dados protegidos e seguros, garantindo que as informações não sejam compartilhadas entre inquilinos.


## Pré-requisitos

Para executar este projeto, você precisa ter:

- Docker (para execução em containers)

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/RailsonPinheiro2030/Django-Multi-Tenant
    ```


2. renomeie o arquivo `.env-example` para `.env` e preecha as variaveis

    ```bash
    POSTGRES_DB=database_name
    POSTGRES_USER=database_username
    POSTGRES_PASSWORD=database_password

    SECRET_KEY=django_secret_key

    #RABBITMQ SERVICES
    RABBITMQ_USER=rabbtmq_username
    RABBITMQ_PASSWORD=rabbtmq_password


    ###DJANGO TENANTS
    APP_NAME=your_app_name
    APP_DOMAIN=your_puclic_app_domain
    ```

3. Adicione o nome do dominio do tenant principal em $APP_DOMAIN e o nome da aplicação em $APP_NAME

    exemplo: APP_DOMAIN=localhost



## Configuração Local para Testar Tenants

Após criar um tenant, você pode testar localmente redirecionando o domínio escolhido para `localhost` no seu arquivo de hosts.

### Windows:

1. Navegue até `C:\Windows\System32\drivers\etc`.
2. Abra o arquivo `hosts` como administrador.
3. Adicione linhas para cada tenant que deseja testar. Por exemplo: 
    ```bash
        127.0.0.1 domain1.localhost
        127.0.0.1 domain2.localhost
        127.0.0.1 main3.localhost
    ```

    Substitua `domain1.localhost`, `domain2.localhost`, e `main3.localhost` pelos domínios dos seus tenants.

### Linux:

1. Abra um terminal.
2. Edite o arquivo `/etc/hosts` com privilégios de administrador (root). Por exemplo, use `sudo nano /etc/hosts`.
3. Adicione linhas similares às do Windows para cada tenant. Por exemplo:
    ```bash
        127.0.0.1 domain1.localhost
        127.0.0.1 domain2.localhost
        127.0.0.1 main3.localhost
    ```


Novamente, substitua os domínios de exemplo pelos seus.

Após editar e salvar o arquivo de hosts, tente acessar os domínios especificados pelo navegador para testar a configuração do tenant.



## Executando a Aplicação com Docker

1. Construa e inicie os contêineres com Docker Compose:

    ```bash
    docker-compose up --build
    ```

    Isso irá construir as imagens Docker necessárias e iniciar os contêineres.


2. Apos o build acesso a aplicação esta disponivel em http://localhost:8000
    


## Configuração gerais

1. Para disponibilizar o app do django no admin para o tenant expecifico voce deve usar o codigo abaixo:
    
    Para disponibilizar somente ao tenant public
    ```python
        from .models import myModel
        from django_tenants.admin import TenantAdminMixin

        class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
            def has_module_permission(self, request):
                return request.tenant.schema_name == 'public' 


        admin.site.register(myModel, ClientAdmin)
    ```

    Para disponibilizar somente aos tenants não public
     ```python
        from .models import myModel
        from django_tenants.admin import TenantAdminMixin

        class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
            def has_module_permission(self, request):
                if request.tenant.schema_name == 'public':
                    return False


        admin.site.register(myModel, ClientAdmin)
    ```

2. Para criar um superusuario para o tenant princiapal:
    ```bash
    docker-compose run djangotenants python manage.py create_tenant_superuser --schema=public
    ```


2. Ao acessar o admin em http://localhost:8000/admin voce pode criar mais tenants na opção client,
   assim que salvar sera dispada uma tarefa com aipo para a criação do schema do tenant,
   na opção domain voce adiciona o dominio do tenant, exemplo: localhost.constumer



3. Para criar um admin do inquilino voce deve usar o comando:
    ```bash
    docker-compose run djangotenants python manage.py create_tenant_superuser --schema=nome_do_schema_do_inquilino

    Assim voce pode acessar http://localhost.constumer:8000/admin e voce estara acessando o administrador do inquilino
    ```

### AIPO

1. Para usar o aipo voce deve definir o contexto do tenants:
    ```python
        from django_tenants.utils import schema_context

        with schema_context(schema_name):

    ```
    ou o decorador:
    ```python
        from django_tenants.utils import schema_context

        @schema_context(schema_name)
        def my_task():

    ```


## Como funciona
    - Os locatários são identificados pelo nome do host (ou seja, locatário.domínio.com). 
    Essas informações são armazenadas em uma tabela no public schema. Sempre que uma solicitação 
    é feita, o nome do host é usado para corresponder a um locatário no banco de dados. Se 
    houver uma correspondência, o caminho de pesquisa será atualizado para usar o schema deste 
    locatário. Portanto, a partir de agora todas as consultas ocorrerão no schema do locatário. 
    Por exemplo, suponha que você tenha um locatário customer http://customer.example.com, 
    qualquer solicitação recebida customer.example.com usará automaticamente o customer schema 
    e disponibilizará o locatário na solicitação. Se nenhum inquilino for encontrado, um erro 404 
    será gerado. Isso também significa que você deve ter um locatário para seu domínio principal, 
    normalmente usando o public schema.




## Estrutura de Diretórios e Arquivos

- `djangoTenants`: Diretório principal da aplicação.
- `urls_public.py`: Arquivo contendo as rotas públicas.
- `commands.txt`: Arquivo contendo os comandos padrões do django-tenant.

## Contribuição

Se deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua contribuição.
3. Faça suas alterações.
4. Envie um pull request.



## Links úteis

https://django-tenants.readthedocs.io/en/latest/


## Contato

Para mais informações, entre em contato com o mantenedor do projeto: [railsonp560@gmail.com](mailto:railsonp560@gmail.com).

