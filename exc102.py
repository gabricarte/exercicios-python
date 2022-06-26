def fatorial(n, show=False):
    """
    ->Calcula o valor de fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não o número a ser calculado.
    :return: O valor fatorial do número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5, show=True))
