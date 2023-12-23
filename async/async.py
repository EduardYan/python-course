def twitter():
    print('t: leyendo')
    yield
    print('t: comentando')
    yield
    print('t: cuestionando')
    yield
    print('t: leyendo otras cosas')

def estudiar():
    print('e: Leyendo resumen')
    yield
    print('e: hablando sobre el tema')
    yield
    print('e: armando cuestionario')


def loop(tasks):
    while tasks:
        actual = tasks.pop(0)

        try:
            next(actual)

            tasks.append(actual)

        except StopIteration:
            pass


loop([twitter(), estudiar()])
