
class  Elements_variable ():

    #capabilities
    desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "avd": "teste_desafio",
    "appPackage": "io.ionic.starter",
    "appActivity": ".MainActivity t7}",
    "automationName": "UIAutomator2"
    }

    #Login
    login_email = "//android.webkit.WebView[@text=\"Ionic App\"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText"
    login_email_value = "teste2023@gmail.com"
    login_password = "//android.widget.EditText[@text=\"Senha\"]"
    login_password_value = "6411638"
    Button_login = '//android.widget.Button[@text="Login"]'

    #Create_account
    Button_create_account = "//android.view.View[@text=\"Crie uma conta\"]"
    add_email_acconunt_ = '//android.webkit.WebView[@text="Ionic App"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText'
    add_email_acconunt_value = "test001@gmail.com"
    add_password_account = "//android.widget.EditText[@text=\"Senha\"]"
    add_password_account_value = "123456"
    add_password_account_repeat = "//android.widget.EditText[@text=\"Repita Senha\"]"
    add_password_account_repeat_value = "123456"
    Button_register = "//android.widget.Button[@text=\"Cadastrar\"]"

    #happy_path
    select_product1 = "//android.widget.Image[@text=\"6489f06c4f5b6\"]"
    add_product1 = '//android.widget.Button[@text="+"]'
    add_button_cart = '//android.widget.Button[@text="Adicionar R$ 0"]'

    #Checkout
    button_paymant = "//android.widget.Button[@text=\"Fazer Pagamento\"]"
    button_pay_now = "//android.widget.Button[@text=\"Pagar agora!\"]"
    button_ok = "//android.widget.Button[@text=\"OK\"]"

    #serch_field
    Elements_heroes = '(//android.view.View[@text="people Heróis"])[2]'
    Select_heroes = '//android.widget.Image[@text="538615ca33ab0"]'
    search_field = "//android.widget.EditText"
    search_field_value = "hulk"
    select_image = "//android.widget.Image[@text=\"5ba3ede961416\"]"

    #select_products_multiple
    Button_return_navigate = "//android.widget.Button[@text=\"arrow back\"]"
    select_product2 = "//android.widget.Image[@text=\"5df3fc8b3c883\"]"
    add_product2 = "//android.widget.Button[@text=\"+\"]"
    add_button_cart2 = '//android.widget.Button[@text="Adicionar R$ 0"]'