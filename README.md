# Projeto-Devops-codigo-certo
Repositóro tem como objetivo principal introduzir e praticar conceitos fundamentais de DevOps Jr através da implementação de um pipeline de CI/CD para uma aplicação web simples.

### Criando uma aplicação web simples
Utilizando Python criei uma aplicação web que retorna uma mensagem simples com o arquivo app.py:
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
### Aplicação para testar app.py:
teste_app.py
```plaintext
import unittest  # para criar testes unitários.
from wsgiref.simple_server import make_server # Para simular servidor http
import io # Para capturar saida do servidor da aplicação

def application(environ, start_response):
    # Simular comportamento da aplicação
    path = environ['PATH_INFO']
    headers = [('Content-Type', 'text/html')]

    if path == '/':
        start_response('200 OK', headers)
        return [b'<h1>Ola, este e meu  projeto devops codigo certo!</h1>']
    else:
        start_response('404 Not Found', headers)
        return [b'<h1>Not Found</h1>']

class TestApp(unittest.TestCase):

    def setUp(self):
        self.capture_buffer = io.StringIO()

    def test_application(self):
        environ = {'PATH_INFO': '/'}
        application(environ, self.capture_buffer.write)
        self.capture_buffer.seek(0)
        response_html = self.capture_buffer.read()
        self.assertEqual(response_html, '<h1>Ola, este e meu  projeto devops codigo certo!</h1>')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

### Definindo um Dockerfile para a containerização:
```plaintext
| FROM python:3.10
|
|  WORKDIR main
|
|
| COPY . .
|
| EXPOSE 5000
|
| CMD ["python", "app.py"]

```
### Criando e executando uma imagem de docker
```plaintext
Com os arquivos app.py e Dockerfile criados uitlizei a platadorma Killercoda: https://killercoda.com/playgrounds/scenario/ubuntu.
Foi criado um cenário ubunto no qual digitei os segintes comandos no terminal:

-  docker build -t python-test .
   comando utilizado para criar a imagem, a opção '-t' permite que você defina o nome de sua imagem. nosse caso,escolhi 'python-test', mas você pode usar o nome que preferir.

- docker run python-test
  Comando utilizado para executar a imagem do contêiner

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

