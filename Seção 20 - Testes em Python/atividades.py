def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'
    return f'Estou comendo {comida} por que {final}'

def dormir(num_horas):
    if num_horas < 8:
        final = 'Continuo cansado após dormir por 4 horas. :('
    else:
        final = 'Putz dormir muito! Estou atrasado vou me atrasar :( '
    return final

def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

