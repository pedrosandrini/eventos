    @author [Pedro Henrique Garcia Sandrini]
    @email [sandrini.pedro@outlook.com]
    @desc [Sistema para gerenciamento de eventos.]

# Sistema de eventos univem.

**Descrição**: O sistema de gerenciamento de eventos do univem foi desenvolvido utilizando o python como linguagem de programação, por se tratar de um sistema web foi utilizado o microframework chamado **Flask**, quaisquer dúvidas consulte a documentação em: https://flask.palletsprojects.com/en/2.2.x/, o Flask já possui uma biblioteca interna para comunicação entre back-end e fron-end o **Jinja2** que pode ser consultado em: https://jinja.palletsprojects.com/en/3.1.x/

## Observações sobre os \_modules:

**Descrição**: O flask trabalha com blueprints que superficialmente são módulos da aplicação sendo cada um responsavel por uma parte vital do sistema, na arquitetura desta aplicação por coersão foi criado uma padrão de identificação de modulos da seguinte forma, **"NomeDoModulo_module"** dentro de cada módulo estão seus arquivos responsaveis pelo seu funcionamento.

## Observações sobre arquivos:

- **models.py**: Arquivo responsável pela definição dos modelos do banco de dados utilizados dentro da aplicação, os modelos foram construidos a partir da biblioteca **flask-sqlalchemy** quaisquer dúvidas consulte a documentação em: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/.

- **run.py**: Arquivo responsável pela inicialização da aplicação no servidor, e pelo contexto de processador shell do python.

- **config.py**: Arquivo responsável pelas definições e configurações do ambiente virtual (venv) do python, antes de iniciar a aplição o ambiente deve ser criado e configurado com as váriaveis descritas dentro do arquivo.

## Processo de inicialização para desenvolvimento:

  1 - Confirme se o argumento de create_app() no arquivo run.py está configrado com "os.getenv(('FLASK_CONFIG') or 'default')", caso esteja não crie uma variavel de ambiente para FLASK_CONFIG, deixe executar como default que ira criar um banco sqlite para fins de desenvolvimento.
