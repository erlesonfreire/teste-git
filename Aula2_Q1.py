nome = input('Informe o primeiro nome do funcionário: ')

valor_hora = {'Ana': 13.50, 'Carlos': 14, 'Maria': 14, 'Paulo': 14.50}
horas = {'Ana': 120, 'Carlos': 160, 'Maria': 150, 'Paulo': 200}

try:
    salario = horas[nome]*valor_hora[nome]
    print('O salário de', nome, 'é de', salario)
except:
    novas_horas = input('Informe as horas de trabalho de ' + nome + ': ')
    novo_valor_hora = input('Informe o valor que' + nome + 'recebe por hora: ')
    horas[nome] = novas_horas
    valor_hora[nome] = novo_valor_hora
    print('A lista de funcionários e valor por hora foram atualizada')
    print(horas)
    print(valor_hora)