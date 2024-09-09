curl -X POST http://127.0.0.1:5000/usuario -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alice@example.com\", \"password\": \"securepassword\", \"is_active\": true, \"cpf_cnpj\": \"12345678900\"}"


curl -X PUT http://127.0.0.1:5000/usuario/1 -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alice@example.com\", \"password\": \"newpassword\", \"is_active\": false, \"cpf_cnpj\": \"12345678900\"}"


curl -X GET http://127.0.0.1:5000/usuario/1


curl -X PUT http://127.0.0.1:5000/usuario/1/status -H "Content-Type: application/json" -d "{\"is_active\": false}"
