## Como rodar o servidor Flask

Basta acessar a pasta ```backend``` e rodar o arquivo ```app.py``` com o comando:

```python app.py```

## Visualizar a página web

Basta acessar a porta ```http://127.0.0.1:5000``` , digitar no input a operadora desejada e clicar em buscar.

## Consulta da rota 'buscar'
Para consultar a coleção Postman, basta importar o arquivo ```Busca Operadoras Flask API.postman_collection.json``` no app ou site do [Postman](https://www.postman.com).

Depois, executar a requisição GET na porta ```http://127.0.0.1:5000``` e na rota ```/buscar?termo=[Nome da Operadora]```