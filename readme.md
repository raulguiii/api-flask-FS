crie um codigo com python, flask e sqlite com as seguintes necessidades: Criar Usuário

CRIAR USUARIO
Método: POST
URL: /usuario
Campos:
name
email
password
is_active
cpf_cnpj


ATUALIZAR USUARIO
Método: PUT
URL: /usuario/{id}
Campos:
name
email
password
is_active
cpf_cnpj

Encontrar Usuário pelo ID
Método: GET
URL: /usuario/{id}

Inativar ou Ativar usuário pelo ID
Método: PUT
URL: /usuario/{id}/status
Campos:
is_active