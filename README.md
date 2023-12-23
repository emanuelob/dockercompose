Ambiente Dockerizado que inclui serviços como Flask, Roundcube para e-mail, Rocket.Chat para chat e MongoDB para banco de dados.

- [Vídeo executando o compose.yml](https://drive.google.com/file/d/1iR0YrCnHk_OsGgJ5jkc48FgHkZ4zjJG6/view?usp=sharing)

## Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina antes de começar.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como Usar

1. Clone este repositório para o seu ambiente local.

```bash
git clone https://github.com/emanuelob/dockercompose.git
```

2. Crie um arquivo .env com as variáveis de ambiente necessárias. 

```bash
cp .env.example .env
```

3. Execute o seguinte comando para construir e iniciar os serviços.

```bash
docker-compose up -d
```
ou
```bash
docker compose up
```

4. Agora, você pode acessar os serviços nos seguintes URLs:

. Web (Flask): http://localhost:5000

. E-mail (Roundcube): http://localhost:8081

. Chat (Rocket.Chat): http://localhost:3000

5. Para parar e remover os contêineres, execute:

```bash
docker-compose down
```
