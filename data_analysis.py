import os
import pandas
from matplotlib import pyplot


arquivo = rf"{os.environ.get('DATA_PATH')}"
print(f'Caminho do arquivo: {arquivo}')


dado = pandas.read_csv(arquivo, sep=',', encoding='UTF-8')
pyplot.plot(dado['mês'], dado['cabeças de gado'])
pyplot.show()
pyplot.bar(dado['mês'], dado['cabeças de gado'])
pyplot.show()

