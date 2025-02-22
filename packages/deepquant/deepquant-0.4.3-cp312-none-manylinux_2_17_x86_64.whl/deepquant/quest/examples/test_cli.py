#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/4/20 14:54
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : __init__.py
import os
import unittest
import warnings
from unittest.mock import Mock

from click.testing import CliRunner

import deepquant.quest.sdk as yhsdk
from deepquant import gid

gid.init('gidtest', 'gid#2024')


class TestUpdate(unittest.TestCase):

    def setUp(self):
        def side_effect(*args):
            print(*args)
            return args

        yhsdk.cmds.pip_install = Mock(side_effect=side_effect)
    '''
    def test_update_with_no_product(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.update, [])
        output = result.output
        self.assertIn("yhsdk", output, "不包含yhsdk")
        self.assertIn("https://pypi.tuna.tsinghua.edu.cn/simple/\n", output, "默认清华源")

    def test_update_with_i(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.update, ["-i https://py.ricequant.com/simple/"])
        output = result.output
        self.assertTrue(output.endswith("https://py.ricequant.com/simple/\n"), "参数无效")

    def test_update_with_error_product(self):
        from deepquant.quest.sdk.const import PRODUCTS
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.update, ["rqdata"])
        output = result.output
        out_str = "PRODUCT可选为:{}\n,当前为{}。".format(PRODUCTS, "rqdata")
        self.assertIn(out_str, output, "产品参数错误提示错误")
'''
    def test_update_data(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.update_data, ["-dD:/sendData/ricequant/", "--base"])
        output = result.output
        self.assertTrue(output, '')

'''
class TestLicense(unittest.TestCase):

    def setUp(self):
        os.environ['RQDATAC2_CONF'] = "tcp://license:LgWjKyJl71S-PTXCdwEIlzKlU3Qqyn27gzPs6Xc1v7flJKPhIokNZCb0aoMg8PjaJYUPGfXBdyTkjve-53V7lySjvrNL9A94gf6ZpVv0XMum_2ebQkq2_KDDW2uhBHmsLkC7H2RgtTSAOJ1T3MBc0tRzh8-W5DJIxfSiFjfbrrk=iF1HruSX_Z3zYaJ77zAGh_4yr1PnL3AviSUGey8aDfOZI4MKIo4n2Bw9UtKPKviFTWqeOqYd0JAzClsXj5wvca_WA3hfHgA-4C8yibC9J2qjj1ZK4prXbw8FpgW5oRyUMYCC_0dCr13cJ8h6dx2Xwecg7RUCZVuUB-0cTLtgr4s=@rqdatad-pro.ricequant.com:16011"
        os.environ['RQSDK_LICENSE'] = "tcp://license:LgWjKyJl71S-PTXCdwEIlzKlU3Qqyn27gzPs6Xc1v7flJKPhIokNZCb0aoMg8PjaJYUPGfXBdyTkjve-53V7lySjvrNL9A94gf6ZpVv0XMum_2ebQkq2_KDDW2uhBHmsLkC7H2RgtTSAOJ1T3MBc0tRzh8-W5DJIxfSiFjfbrrk=iF1HruSX_Z3zYaJ77zAGh_4yr1PnL3AviSUGey8aDfOZI4MKIo4n2Bw9UtKPKviFTWqeOqYd0JAzClsXj5wvca_WA3hfHgA-4C8yibC9J2qjj1ZK4prXbw8FpgW5oRyUMYCC_0dCr13cJ8h6dx2Xwecg7RUCZVuUB-0cTLtgr4s=@rqdatad-pro.ricequant.com:16011"

    def test_info(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.license, ["info"])
        output = result.output
        self.assertIn('剩余有效天数', output, "license info 提示错误")
        output = result.output
        self.assertIn('产品', output, "license info 提示错误")
        self.assertIn('开启', output, "license info 提示错误")
        self.assertIn('剩余有效天数', output, "license info 提示错误")

        os.environ.pop('RQDATAC2_CONF')
        os.environ.pop('RQSDK_LICENSE')
        result = runner.invoke(yhsdk.cmds.license, ["info"])
        output = result.output
        self.assertIn('当前环境没有配置 license', output, "无license时 info 提示错误")

        os.environ['RQSDK_LICENSE'] = "tcp://18670306315:12345678@rqdatad-pro.ricequant.com:16011"
        result = runner.invoke(yhsdk.cmds.license, ["info"])
        output = result.output
        self.assertIn('LICENSE不可用', output, "license 设置错误时 info 提示错误")


class TestConfig(unittest.TestCase):
    def setUp(self):
        if 'RQDATAC2_CONF' in os.environ:
            os.environ.pop('RQDATAC2_CONF')
        if 'RQSDK_LICENSE' in os.environ:
            os.environ.pop('RQSDK_LICENSE')

    
    def test_set_rqdatac(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.config,
                               ["--rqdatac", "tcp://license:LgWjKyJl71S-PTXCdwEIlzKlU3Qqyn27gzPs6Xc1v7flJKPhIokNZCb0aoMg8PjaJYUPGfXBdyTkjve-53V7lySjvrNL9A94gf6ZpVv0XMum_2ebQkq2_KDDW2uhBHmsLkC7H2RgtTSAOJ1T3MBc0tRzh8-W5DJIxfSiFjfbrrk=iF1HruSX_Z3zYaJ77zAGh_4yr1PnL3AviSUGey8aDfOZI4MKIo4n2Bw9UtKPKviFTWqeOqYd0JAzClsXj5wvca_WA3hfHgA-4C8yibC9J2qjj1ZK4prXbw8FpgW5oRyUMYCC_0dCr13cJ8h6dx2Xwecg7RUCZVuUB-0cTLtgr4s=@rqdatad-pro.ricequant.com:16011"])
        output = result.output
        self.assertIn('当前 rqdatac license 已设置为', output, "设置rqdatac license")
    
    def test_show(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.config, ["--show"])
        output = result.output
        self.assertEqual(output, "")
    
    def test_option_license(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.license, ["-l", "license:LgWjKyJl71S-PTXCdwEIlzKlU3Qqyn27gzPs6Xc1v7flJKPhIokNZCb0aoMg8PjaJYUPGfXBdyTkjve-53V7lySjvrNL9A94gf6ZpVv0XMum_2ebQkq2_KDDW2uhBHmsLkC7H2RgtTSAOJ1T3MBc0tRzh8-W5DJIxfSiFjfbrrk=iF1HruSX_Z3zYaJ77zAGh_4yr1PnL3AviSUGey8aDfOZI4MKIo4n2Bw9UtKPKviFTWqeOqYd0JAzClsXj5wvca_WA3hfHgA-4C8yibC9J2qjj1ZK4prXbw8FpgW5oRyUMYCC_0dCr13cJ8h6dx2Xwecg7RUCZVuUB-0cTLtgr4s="])
        output = result.output
        self.assertIn('产品', output, "license info 提示错误")
        self.assertIn('开启', output, "license info 提示错误")
        self.assertIn('剩余有效天数', output, "license info 提示错误")
    '''
'''
class TestVersion(unittest.TestCase):

    def test_cli_version(self):
        runner = CliRunner()
        import deepquant.quest.sdk as yhsdk
        result = runner.invoke(yhsdk.cmds.version, [])
        text = result.output
        print("text:",text)

        self.assertIn("yhsdk", text, "yhsdk 不在version展示中")
        self.assertIn("yhsdk==" + yhsdk.__version__, text, "未展示yhsdk版本")
        self.assertIn("rqdatac==", text, "未展示rqdatac版本，rqdatac为必要包")
'''
'''

class TestInstall(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", message="numpy.dtype size changed")
        warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

        def side_effect(*args):
            print(*args)
            return args

        yhsdk.cmds.pip_install = Mock(side_effect=side_effect)

    def test_install_with_error_product(self):
        from deepquant.quest.sdk.const import PRODUCTS
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.install, ["rqdata"])
        output = result.output
        out_str = "请输入正确的产品名称".format(PRODUCTS, "rqdata")
        self.assertIn(out_str, output, "产品参数错误提示错误")

    def test_install_with_no_product(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.install, [])
        output = result.output
        out_str = "请输入产品名称"
        self.assertIn(out_str, output, "产品提示错误")

    def test_install_with_right_product(self):
        runner = CliRunner()
        result = runner.invoke(yhsdk.cmds.install, ["yhalpha_plus"])
        output = result.output
        out_str = "yhsdk[yhalpha_plus]"
        self.assertIn(out_str, output, "安装输入错误")

'''
