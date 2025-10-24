import random
import string

def generar_contrasena(longitud=12, usar_mayus=True, usar_num=True, usar_simb=True):
    """Genera una contraseña aleatoria.

    Args:
        longitud (int): Longitud de la contraseña.
        usar_mayus (bool): Incluir letras mayúsculas.
        usar_num (bool): Incluir números.
        usar_simb (bool): Incluir símbolos.

    Returns:
        str: Contraseña generada.
    
    caracteres = string.ascii_lowercase
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_num:
        caracteres += string.digits
    if usar_simb:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
    """

    Letras_min=string.ascii_lowercase
    Letras_may=string.ascii_uppercase
    Numeros=string.digits
    Simbolos=string.punctuation

    pool_total=Letras_min
    contrasena_garantizada=[]

    contrasena_garantizada.append(random.choice(Letras_min))
    if usar_mayus:
        pool_total+=Letras_may
        contrasena_garantizada.append(random.choice(Letras_may))
    if usar_num:
        pool_total+=Numeros
        contrasena_garantizada.append(random.choice(Numeros))
    if usar_simb:
        pool_total+=Simbolos
        contrasena_garantizada.append(random.choice(Simbolos))

    longitud_relleno=longitud-len(contrasena_garantizada)

    relleno=[]
    for _ in range(longitud_relleno):
        relleno.append(random.choice(pool_total))


    lista_contrasena=contrasena_garantizada+relleno
    random.shuffle(lista_contrasena)

    contrasena_final=''.join(lista_contrasena)
    return contrasena_final

pass_segura = generar_contrasena(longitud=16, usar_mayus=True, usar_num=True, usar_simb=True)
print(f"Contraseña segura (16 chars): {pass_segura}")

pass_simple = generar_contrasena(longitud=10, usar_mayus=False, usar_num=True, usar_simb=False)
print(f"Contraseña simple (10 chars, solo minúsculas y números): {pass_simple}")

pass_corta = generar_contrasena(longitud=3, usar_mayus=True, usar_num=True, usar_simb=True)
print(f"Contraseña muy corta (3 chars): {pass_corta}")