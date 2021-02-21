import time

from selenium.webdriver.support.wait import WebDriverWait

from tool.get_logging import GetLogging

logger = GetLogging().get_logging()


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, time=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        logger.info("正在点击{}".format(loc))
        self.base_find_element(loc).click()
        logger.info("点击{}完成".format(loc))

    def base_input(self, loc, value):
        logger.info("正在查找{}".format(loc))
        el = self.base_find_element(loc)
        logger.info("点击{}完成".format(loc))
        logger.info("正在清空{}内容".format(loc))
        el.clear()
        logger.info("正在{}输入框里输入{}".format(loc, value))
        el.send_keys(value)
        logger.info("输入{}完成输入值{}".format(loc, value))

    def base_get_text(self, loc):
        logger.info("正在获取{}的文本".format(loc))
        return self.base_find_element(loc).text

    def base_get_screenshot(self):
        logger.info("正在截图")
        self.driver.get_screenshot_as_file("../screenshot/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
        logger.info("完成截图")

    def base_if_exist(self, loc):
        try:

            if self.base_find_element(loc, time=10):
                logger.info("正在查找是否存在{}".format(loc))
                return True
        except Exception as e:
            logger.error("error信息是{}".format(e))
            return False

    def base_back_to_index(self, url):
        logger.info("正在返回页面{}".format(url))
        try:
            self.driver.get(url)
            logger.info("成功返回{}".format(url))
        except Exception as e:
            logger.error("error信息是{}".format(e))

    def base_switch_to_iframe(self, frame):
        logger.info("正在切换到frame{}".format(frame))
        try:

            self.driver.switch_to.frame(frame)
            logger.info("成功切换frame")
        except Exception as e:
            logger.error("error信息是{}".format(e))

    def base_switch_to_default(self):
        logger.info("正在返回默认页面")
        try:
            self.driver.switch_to.default_content()
            logger.info("成功返回默认页面")
        except Exception as e:
            logger.error("error信息是{}".format(e))

    def base_switch_to_handle(self, title):
        try:
            # current_handle=self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if self.driver.title != title:
                    logger.info("当前页面title：{},期望页面title:{}".format(self.driver.title, title))
                    self.driver.switch_to.window(handle)
                    logger.info("完成切换handle")
                else:
                    logger.info("当前页面title：{},期望页面title:{}".format(self.driver.title, title))
                    logger.info("不用切换handle，需要测试的就是当前页面")
        except Exception as e:
            logger.error("error信息是{}".format(e))
