from playwright.sync_api import Playwright, sync_playwright



def run(playwright, page):
    print("iniciando login")
    
    page.goto("https://painel-homol.matrixcargo.com.br/")
    
    page.locator("input[name=\"username\"]").click()
    
    page.locator("input[name=\"username\"]").fill("admin@matrixcargo.com.br")
    
    page.locator("input[name=\"username\"]").press("Tab")
    
    page.locator("input[name=\"password\"]").fill("admin")
    
    
    with page.expect_navigation():
        page.locator("input[name=\"password\"]").press("Enter")

    page.locator("text=​Organização >> div[role=\"button\"]").click()
    page.locator("li[role=\"option\"]:has-text(\"Org Test credentials\")").click()
    page.locator("div[role=\"button\"]:has-text(\"​\")").click()
    page.locator("li[role=\"option\"]:has-text(\"Default\")").click()