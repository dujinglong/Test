import os
import unittest
import time
import interfaceTest.getpathInfo
from HTMLTestRunner import HTMLTestRunner
from interfaceTest.core_package import Test_main
from interfaceTest.log_and_logresult_package import Log

logger = Log.logger


def report():
    suite = unittest.TestSuite()
    suite.addTests(map(Test_main.Interface, ["login", "college"]))
    date = time.strftime('%Y-%m-%d-%H-%M-%S')
    path = interfaceTest.getpathInfo.get_Path()
    config_path = os.path.join(path, 'result\\report-'+date+'.html')
    if suite is not None:
        fp = open(config_path, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='Test Report',
                                description='Test Description')

        # runner = xmlrunner.XMLTestRunner(output=config_path)  # jenkins report
        runner.run(suite)
        fp.close()
    else:
        logger.error("Have no case to test")
