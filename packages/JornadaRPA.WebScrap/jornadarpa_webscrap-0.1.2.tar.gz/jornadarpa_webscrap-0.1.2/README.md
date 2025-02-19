# JornadaRPA.WebScrap

JornadaRPA.WebScrap é um módulo Python projetado para facilitar o scraping de dados de tabelas em páginas web, utilizando o BotCity Web Automation e Pandas.

---

## 🚀 Funcionalidades
- Extrai dados tabulares de páginas web.
- Suporte para automação com o framework BotCity.
- Retorna os dados em um DataFrame do Pandas.

---

## 🛠️ Pré-requisitos
Certifique-se de ter os seguintes pacotes instalados:
- `botcity-framework-web`
- `pandas`

Para instalá-los:
```bash
pip install botcity-framework-web pandas

## 📦 Como usar

1. Inicie o BotCity WebBot

from botcity.web import WebBot

# Inicializando o bot
bot = WebBot()
bot.start_browser()
bot.navigate_to("https://sua-pagina-web.com")

2. Use o módulo WebScrap
from jornadaRPA.webScrap import Webscrap

# Configurando o scraper
scraper = Webscrap()

# Extraindo dados da tabela
data = scraper.webscrap(
    inBot=bot,
    inLines=10,               # Máximo de linhas a extrair
    inNext="//button[@id='next']",  # XPath do botão "Próximo"
    inXPATH="//table[@id='data']"  # XPath da tabela
)

# Visualizando os dados
print(data)


## 🛡️ Licença
Este projeto está licenciado sob a MIT License. Você pode usar, modificar e distribuir este código livremente, desde que mantenha os créditos.


## 📫 Contato
Se você tiver dúvidas, sugestões ou problemas, entre em contato:

Email: alexdiogo@desafiosrpa.com.br

---


