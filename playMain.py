from cmath import log
import this
from playwright.sync_api import Playwright, sync_playwright
import time
import login
from exemplos import NovaOs
import banco


cenario = [NovaOs().adicionaPedido,NovaOs().adicionaPedido]


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login.run(playwright, page)

    contador = 0
    while contador<len(cenario):
        result = cenario[contador](lib = playwright, pagina = page, custom=['teste3'], pedidoId="2bbcaf5c")
        contador+=1

banco.relatorio.append("dale")
