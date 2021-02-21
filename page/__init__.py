from selenium.webdriver.common.by import By

URL = "http://39.105.18.132:81/"
"""login"""
login_link = By.LINK_TEXT, "登录"
username = By.CSS_SELECTOR, "#username"
password = By.CSS_SELECTOR, "#password"
verify_code = By.CSS_SELECTOR, "#verify_code"
submit_btn = By.CSS_SELECTOR, ".J-login-submit"
error_text = By.CSS_SELECTOR, ".layui-layer-content"
error_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
logout_link = By.LINK_TEXT, "安全退出"

"""cart"""
goods_item = By.CSS_SELECTOR, ".floor-goods-item"
join_cart = By.CSS_SELECTOR, "#join_cart"
join_success = By.CSS_SELECTOR, ".conect-title>span"
success_frame = "layui-layer-iframe1"
close_frame = By.CSS_SELECTOR, ".layui-layer-ico"

"""order"""
my_cart = By.CSS_SELECTOR, ".share-shopcar-index"
select_all = By.CSS_SELECTOR, ".checkCart"
take_order = By.CSS_SELECTOR, ".gwc-qjs"
order_person = By.CSS_SELECTOR, ".consignee>b"
submit_order = By.CSS_SELECTOR, ".Sub-orders"
order_success_info = By.CSS_SELECTOR, ".erhuh>h3"

"""pay"""
my_order = By.LINK_TEXT, "我的订单"
pay_now_btn = By.CSS_SELECTOR, ".ps_lj"
delivery_radio = By.CSS_SELECTOR, "[value='pay_code=cod']"
confirm_payment = By.CSS_SELECTOR, ".button-confirm-payment"
pay_success_info = By.CSS_SELECTOR, ".erhuh>h3"