import matplotlib.pyplot as plt

# Dados
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril']
infracoes = [12, 19, 3, 5]

# Criar gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(meses, infracoes, color='salmon')
plt.title('Gráfico de Infrações')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Infrações')

# Exibir o gráfico
plt.tight_layout()
plt.show()
