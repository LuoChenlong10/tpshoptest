from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
# url = "http:localhost:80"
url = "https://hmshop-test.itheima.net/"

"""以下为登录页元素配置信息"""
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.ID, "username"
# 密码
login_password = By.ID, "password"
# 验证码
login_verify_code = By.ID, "verify_code"
# 点击登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 获取异常文本信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击异常提示框
login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
#安全退出按钮
login_logout_btn = By.PARTIAL_LINK_TEXT, "安全退出"

'''主页购物车配置'''
search_input_box = By.ID, "q" #主页搜索框
search_btn = By.CSS_SELECTOR, ".ecsc-search-button" #搜索按钮
add_to_cart = By.CSS_SELECTOR, "div.xs_img .lazy-list" #添加购物车，前往详情页
add_to_cart_btn = By.CSS_SELECTOR, "#join_cart" #加入购物车
cart_add_after_iframe = By.CSS_SELECTOR, "#layui-layer-iframe1" #加入购物车后会出现一个iframe
cart_add_result = By.CSS_SELECTOR, ".connect-title"#在iframe中定位到加入购物车的结果，成功或者失败
cart_windows_close = By.CSS_SELECTOR, ".layui-layer-close" #关闭弹出窗口

'''主页购物车配置'''
cart_btn = By.CSS_SELECTOR, ".c-n.fl" #购物车
select_all_btn = By.CSS_SELECTOR, ".checkall.checkFull"#全选购物车商品
go_to_pay = By.CSS_SELECTOR, ".paytotal"#去结算
goods_person = By.CSS_SELECTOR, ".invoice_tt"#收货人
order_submit_btn = By.CSS_SELECTOR, "#submit_order"#提交订单
submit_result = By.CSS_SELECTOR, ".erhuh>h3"#提交结果

'''主页我的订单配置'''
my_order_link = By.PARTIAL_LINK_TEXT,"我的订单"
my_order_title = "我的订单"
to_pay_now = By.CSS_SELECTOR, ".ps_lj"#立即支付
pay_title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
pay_way = By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"#货到付款支付方式的图标
confirm_pay_way = By.CSS_SELECTOR, ".button-style-5.button-confirm-payment"
pay_result = By.CSS_SELECTOR, ".erhuh>h3"

'''口技'''






