print('Introduce tu nota(A-F)')
nota = str(input())
nota = nota.upper()
match nota:
    case 'A':
        print('Nota excelente')
    case 'B':
        print('Nota buena')
    case 'C':
        print('Nota regular')
    case 'D':
        print('Nota suficiente')
    case 'F':
        print('Nota insuficiente')
    case other:
        print('Accion invalida')