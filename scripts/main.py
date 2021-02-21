import time
import unittest

from tool.HTMLTestRunner import HTMLTestRunner

suite=unittest.defaultTestLoader.discover("./")
report_dir="../report/{}.html".format(time.strftime("%Y_%m_%s %H_%M_%S"))

with open(report_dir,"wb") as f:
    HTMLTestRunner(f,title="TPshop商城自动化报告").run(suite)
