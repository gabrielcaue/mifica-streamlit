def autenticar_usuario(usuario, senha):
    # Simulação simples
    usuarios_validos = {
        "ana": "123",
        "bruno": "abc",
        "carlos": "xyz"
    }
    return usuarios_validos.get(usuario) == senha
