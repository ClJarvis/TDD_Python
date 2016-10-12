'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVistorTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

  def tearDown(self):
      self.browser.quit()



  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')

    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    #user is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
    inputbox.send_keys('Buy peacock feathers')

    #User types an action in to test box
    inputbox.send_keys(Keys.ENTER)
    #do not need sleep
    import time
    time.sleep(10)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn('row_text', [row.text for row in rows])
          #page 57
        )
      )

    self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

#assert 'To Do LIST' in browser.title

#browser.quit()
'''
