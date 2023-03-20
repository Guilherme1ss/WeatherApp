# Previsão do tempo

Este é um programa em Python que usa a biblioteca Tkinter para criar uma interface gráfica do usuário (GUI) para exibir a previsão do tempo de uma cidade específica.

## Como usar

1. Insira o nome da cidade desejada no campo de texto na parte superior da janela.
2. Clique no botão de pesquisa para obter informações sobre o clima atual naquela cidade.

## Funcionalidades

- Exibe informações sobre temperatura, condição climática, velocidade do vento, umidade e pressão atmosférica.
- Usa a API do OpenWeatherMap para obter informações sobre o clima atual na cidade especificada pelo usuário.
- Usa a biblioteca geopy para obter informações sobre o fuso horário da cidade e exibir o horário local atual.
- Inclui tratamento de exceções para lidar com entradas inválidas do usuário.

## Requisitos

Para executar este programa, você precisará ter Python 3.9 instalado em seu computador. Você também precisará instalar as seguintes bibliotecas:

- Tkinter
- geopy
- timezonefinder
- requests
- pytz

Você pode instalar essas bibliotecas usando o comando `pip install` no terminal ou prompt de comando.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
