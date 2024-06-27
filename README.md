# Projeto-Devops-codigo-certo
Repositóro tem como objetivo principal introduzir e praticar conceitos fundamentais de DevOps Jr através da implementação de um pipeline de CI/CD para uma aplicação web simples.

### Criando uma aplicação web simples
Utilizando Python criei uma aplicação web que retorna uma mensagem simples:
```plaintext
|from wsgiref.simple_server import make_server # Essa função é importada para criar um servidor HTTP simples para executar aplicações web compatíveis com o WSGI.

def application(environ, start_response):
  # Obtendo caminho solicitado path
  path = environ['PATH_INFO']

  # definindo cabeçalhos
  headers = [('Content-Type', 'text/html')]

  # Definindo resposta com base no caminho
  if path == '/':
      start_response('200 OK', headers)
      return [b"<h1>Ola, este e meu  projeto devops codigo certo!</h1>"] ## É esta mensagem que aparecerá quando acessar a porta 8000
  else:
      # Se não lidar com o caminho, responda com o erro (404 Not Found)
      start_response('404 Not Found', headers)
      return [b"<h1>Not Found</h1>"]

with make_server('', 8000, application) as httpd:
  print("Serving on port 8000...")
  httpd.serve_forever()


```


   #### Estrutura do Projeto:
```plaintext
project-root/
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── cd.yml
│
├── src/
│   ├── app.py (ou a estrutura da aplicação escolhida)
|     
├── tests/
│   ├── test_app.py (ou a estrutura de testes apropriada)
│
├── Dockerfile
├── README.md
└──.
```

