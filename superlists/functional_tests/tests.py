from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class NewVisitorTest(LiveServerTestCase):
  def setUp(self):

      self.browser = webdriver.Firefox()
      self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_list_table(self, row_text):
      table = self.browser.find_element_by_id('id_list_table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn(row_text, [row.text for row in rows])


  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get(self.live_server_url)

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

    #user hites enter taken to new URL
    #page lists "1: buy a feather as an iten in a to-do table"
    inputbox.send_keys(Keys.ENTER)
    user_list_url = self.browser.current_url
    self.assertRegex(user_list_url, '/lists/.+')
    self.check_for_row_in_list_table('1: Buy peacock feathers')

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    '''self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
    '''
    self.assertTrue(
      any(row.text == '1: Buy peacock feathers' for row in rows),
      "New to-do item did not appear in table -- its text was:\n%s" % (
          table.text,
      )
  )
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)

# The page updates and show both items user has added to list
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
    self.check_for_row_in_list_table('1: Buy peacock feathers')

#new use Francis, comes along to site.

## We use a new browser session to make sure that no information
## of Edith's is coming through from cookies etc #
    self.browser.quit()
    self.browser = webdriver.Firefox()
# Francis visits the home page. There is no sign of Edith's (1st user) list

    self.browser.get(self.live_server_url)
    page_text = self.browser.find_elements_by_tag_name('body').text
    self.assertNotIn('Buy peacock feather', page_text)
    self.assertNotIn('make a fly', page_text)

#francis starts a new list by entering a new item
    inputbox = self.browser.find_elements_by_id('id_new_item')
    inputbox.send_keys('Buy milk')
    inputbox.send_keys(Keys.ENTER)

#francis gets his own unique URL
    francis_list_url = self.browser.current_url
    self.assertRegex(francis_list_url, '/lists/.+')
    self.assertNotEqual(francis_list_url, user_list_url)

#Again ther is no trace of other users list

    page_text = self.browser.find_element_by_tag_name('body').text
    self.assertNotIn('Buy peacock feathers', page_text)
    self.assertIn('Buy milk', page_text)

#satified they both go back to sleep

    self.fail('Finish the test')

