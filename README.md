# Projeto Agenda com Django, Docker e Postgres

## Descrição
O projeto utiliza conceitos de Django, Python, Docker e Yaml. Desenvolvido para simular agendamentos.
Em desenvolvimento...

### Infraestrutura
  - Python: 3.10.5 
  - Django: 4.2.2 
  - PostgreSQL: 14 
  - _Requisitos/bibliotecas disponíveis em requirements.txt_

### Instruções para uso
  - #### Garantir que tenha o docker/docker-compose instalado
  - #### Criar arquivo db.env com a seguintes informações de exemplo
      - DEBUG=True_ou_False
      - POSTGRES_DB=Nome_do_banco
      - POSTGRES_USER=Usuario
      - POSTGRES_PASSWORD=Senha
      - POSTGRES_SERVICE=Host
      - POSTGRES_PORT=Porta
    
  - #### Roda o comando na raiz do projeto (.../wep_app)
    - docker-compose up -d
  
  Se tudo deu certo, é só acessar http://localhost:8000/