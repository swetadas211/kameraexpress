class product:
    def __init__(self,page):
        self.page=page

        self.homepage = page.locator('//a[@class="brand__logo"]')
        self.product = page.locator('(//div[@class="ke-carousel-container"])[2]/div/a[2]')
        self.product_btn = page.locator('//button[@class="full-width sf-button"]')
        self.add_to_cart = page.locator('(//button[@class="mini-cart-button sf-button--text no-underline sf-button"])[2]')
        self.cart = page.locator('(//button[@class="sf-button"])[2]')
    

    def add_product(self):
        self.homepage.click()
        self.page.wait_for_load_state('load')

        self.product.click()

        self.product_btn.click()
        self.page.wait_for_load_state('load')

        self.add_to_cart.click()
        self.page.wait_for_timeout(3000)

        self.cart.click()
        self.page.wait_for_timeout(3000)