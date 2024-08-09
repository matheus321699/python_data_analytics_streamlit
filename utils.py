def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

# Função de formatação para notação brasileira
def formato_brasileiro(x, pos):
    return f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

