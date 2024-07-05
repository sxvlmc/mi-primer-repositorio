def restar_hasta_que_se_pueda(numero_original, numero_para_restar):
    cantidad_de_veces_que_se_resto = 0
    while numero_original >= numero_para_restar:
        numero_original = numero_original - numero_para_restar
        cantidad_de_veces_que_se_resto = cantidad_de_veces_que_se_resto +1
    return[cantidad_de_veces_que_se_resto, numero_original]


resultado = restar_hasta_que_se_pueda(15,6)
print(resultado)


