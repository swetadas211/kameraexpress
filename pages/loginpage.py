class login:
    def __init__(self,page):
        self.page = page

        # Cookie popup
        self.cookie = page.locator('//button[@class="is--regular"]')

        # Login button
        self.button = page.locator("(//span[text()='Log in'])[2]")
        
        # Login popup button
        self.popup = page.locator('(//button[@class="sf-button"])[2]')
        
        # Credentials
        self.email = page.locator('//input[@type="email"]')
        self.password = page.locator('//input[@type="password"]')
        
        #login button
        self.login = page.locator("//input[@id='btn_login']")

    def login_click(self):
        self.cookie.click()

        self.button.hover()
        self.page.wait_for_load_state('load')

        self.popup.click()

        self.email.fill("swetadas211@gmail.com")
        self.password.fill('123456')
        self.page.wait_for_load_state('load')

        self.login.click()
        self.login.click()

        self.page.wait_for_timeout(3000)

