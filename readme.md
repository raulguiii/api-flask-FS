CRIAR USUARIO
curl -X POST http://127.0.0.1:5000/usuario -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alaaice@example.com\", \"password\": \"securepassword\", \"is_active\": true, \"cpf_cnpj\": \"12345678900\"}"


ATUALIZAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1 -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alice@example.com\", \"password\": \"newpassword\", \"is_active\": false, \"cpf_cnpj\": \"12345678900\"}"


BUSCAR USUARIO PELO ID
curl -X GET http://127.0.0.1:5000/usuario/1


INATIVAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1/status -H "Content-Type: application/json" -d "{\"is_active\": false}"


ATIVAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1/status -H "Content-Type: application/json" -d "{\"is_active\": true}"


SALVAR PRODUTO
curl -X POST http://localhost:5000/produto -H "Content-Type: application/json" -d '{"nome": "Produto1", "quantidade": 10, "preco": 19.99}'


ATUALIZAR PRODUTO 
curl -X PUT http://127.0.0.1:5000/produto/1 -H "Content-Type: application/json" -d "{\"nome\": \"Produto Atualizado\", \"quantidade\": 20}"
