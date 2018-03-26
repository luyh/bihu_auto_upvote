import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
import platform

class bihu_auto_upvote(unittest.TestCase):
    def setUp(self):
        systerm = platform.platform()
        print( "打开chrome" )
        if 'Darwin' in systerm:
            driver = webdriver.Chrome( '/Users/Hebbelu/Public/chromedriver' )
        else:
            chrome_options = Options()
            # specify headless mode
            chrome_options.add_argument( "--headless" )
            driver = webdriver.Chrome( chrome_options=chrome_options )
        driver.set_page_load_timeout( 300 )
        driver.set_script_timeout( 300 )

        self.driver = driver

    def test_get_jingma(self):
        driver = self.driver

        print( "打开金马bihu.com/9909" )
        driver.get( 'https://bihu.com/people/9909' )
        c1, c2 = self._findelement()
        print( c1, "\n", c2 )

        for i in range(5):
            try:
                print( "第", i, "次查询，延时10s" )
                c11, c22 = self._findelement()
                if (c1 != c11):
                    c1 = c11
                    print( c11, c22 )
                    requests.post( 'http://sc.ftqq.com/SCU23707T1a6b7b5527ba64588859a61ecfca18775ab65ce918f4f.send', \
                                   data={'text': c11, 'desp': c22} )
                driver.refresh()
                time.sleep( 10 )
            except:
                print('查询异常')
                time.sleep( 10 )



    def _findelement(self, num=3):
        driver = self.driver
        try:
            c1 = driver.find_element_by_class_name( "content1" ).text
            c2 = driver.find_element_by_class_name( "content2" ).text
        except:
            if num > 0:
                driver.refresh()
                time.sleep( 10 )
                return self._findelement(num - 1 )
            else:
                print( "3次没找到content1和content2对象，报错" )

        return c1, c2

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



