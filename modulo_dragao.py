def caca_ao_dragao(poderes_dragao, poder_magico):
    """
    Identifica os dragões que podem ser capturados com base no poder mágico do aventureiro.

    Args:
    poderes_dragao (list): Lista de inteiros representando o poder dos dragões.
    poder_magico (int): O poder mágico do aventureiro.

    Returns:
    list: Índices dos dragões que podem ser capturados.
    """
    return [i for i, poder in enumerate(poderes_dragao) if poder_magico > poder]
