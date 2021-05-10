Funcionalidade: Cadastrar novo usuário

  Cenário: cadastrar um novo usuário
  Dado que eu esteja na página de cadastro
  Quando criar um usuário corretamente
  """
    {
      "nome": "João da Silva",
      "email": "teste@teste.com",
      "senha": "12345678"
    }

  """
  Então a tabela de usuários cadastrados deve ser exibida
