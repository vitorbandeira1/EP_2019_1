# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:25:07 2019

@author: Vitor Bandeira
"""    
while not game_over:
    cenario_atual = cenarios[nome_cenario_atual]

    print(cenario_atual['titulo'])
    print("-"*len(cenario_atual["titulo"]))
    print(cenario_atual['descricao'])

