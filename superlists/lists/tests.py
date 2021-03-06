from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.models import Item, List
from lists.views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


'''    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0) '''
class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

 #       response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
          '/lists/new',
          data={'item_text': 'A new list item'}
        )
        new_list = List.objects.first()
#        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))



class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_item(self):
      list_ = List()
      list_.save()

      frist_item = Item()
      frist_item.text = 'The first (ever) list item'
      frist_item.list = list_
      frist_item.save()

      second_item = Item()
      second_item.text = 'Item the second'
      second_item.list = list_
      second_item.save()

      saved_list = List.objects.first()
      self.assertEqual(saved_list, list_)

      saved_items = Item.objects.all()
      self.assertEqual(saved_items.count(), 2)

      first_saved_item = saved_items[0]
      second_saved_item = saved_items[1]
      self.assertEqual(first_saved_item.text, 'The first (ever) list item')
      self.assertEqual(first_saved_item.list,list_)
      self.assertEqual(second_saved_item.text, 'Item the second')
      self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def tests_display_all_items(self):
      list = List.objects.create()
#      Item.objects.create(text='itemey 1')
#     Item.objects.create(text='itemey 2')

#      response = self.client.get('/lists/the-only-list-in-the-world/')

#      self.assertContains(response, 'itemey 1')
 #     self.assertContains(response, 'itemey 2')



