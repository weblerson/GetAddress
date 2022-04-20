# GetAddress
GetAddress é um projeto que busca as informações do endereço buscando por CEP ou pelo bairro ou rua. Este projeto é feito com javascript e usa Bootstrap + AJAX.

# Instalação das Bibliotecas
Esta aplicação faz uso do FastAPI e o servidor Uvicorn para habilitar a API que vai ser consumida pelo código JavaScript.

Para realizar a instalação, vá para a raiz do projeto e digite ```pip install -r requirements.txt``` que automaticamente o gerenciador de pacotes do Python irá instalar todas as bibliotecas necessárias.

# Uso
Para usar é bem simples: 

Primeiro, deve-se habilitar a API para que o código JavaScript possa consumí-la para disponibilizar os nomes dos estados e suas respectivas cidades no método de busca por endereço.

Depois, basta abrir um arquivo HTML, preencher os campos necessários e apertar o botão escrito "Buscar" que automaticamente a aplicação irá fazer uma requisição http para a API do ViaCEP, que irá retornar uma resposta com as informações do endereço como CEP, complemento, logradouro etc.

# Habilitar API
Para habilitar a API com os estados e cidades, entre na pasta "API" e digite ```uvicorn API:app```. Dessa forma, a API entrará no ar.

# Abrir a aplicação
Existem duas formas para acessar a aplicação: abrindo o arquivo HTML diretamente no navegador ou subindo um servidor por meio de uma função com o protocolo WSGI.

# Abrir a aplicação por meio de um servidor
*Windows:*

Para abrir um servidor no Windows, será usado o servidor Waitress.

Para isso, navegue até a raiz do projeto e passe o comando ```waitress-serve --listen=127.0.0.1:{porta de sua escolha} server:CEP``` para abrir um servidor com o arquivo CEP.html ou ```waitress-serve --listen=127.0.0.1:{porta de sua escolha} server:Address``` para abrir um servidor com o arquivo Address.html.

*Linux:*

Para abrir um servidor no Linux, será usado o servidor Gunicorn.

Para isso, navegue até a raiz do projeto e passe o comando ```gunicorn -b {porta de sua escolha} server:CEP``` para abrir um servidor com o arquivo CEP.html ou ```gunicorn -b {porta de sua escolha} server:Address``` para abrir um servidor com o arquivo Address.html.

Tanto o CEP.html quanto o Address.html fazem a busca por informações de endereço usando informações diferentes. Enquanto o CEP.html faz uma requisição usando o CEP, o Address.html faz uma requisição usando o estado, cidade e bairro ou rua.

# Campo de estado e cidade vazios
Se a aplicação Address não estiver exibindo os nomes dos estados na select box, deve ser porque a API não foi colocada no ar. Para resolver, coloque a API no ar e recarregue a página Address.html.