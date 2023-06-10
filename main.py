""""
Foi feito em pyhton um programa onde foi calculado o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
"""

estado = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'OUTROS': 19849.53
}
total_faturamento = sum(faturamento.values())

percentual_representacao = {
    estado: (faturamento / total_faturamento) * 100
    for estado, faturamento in faturamento.items()
}
for estado, percentual in percentual_representacao.items():
    print(f'{estado}: {percentual:.2f}%')


