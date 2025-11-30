# biz bu faylda boshqa fayllardagi functionlarni test qiluvchi codelarni yozamiz, Buning uchun biz unittest modulidan foydalanamiz
import unittest
from cheking_functions import  get_full_name

class NameTest(unittest.TestCase):
  def test_toliq_ism(self):
    name = get_full_name('usmanov', 'abduqahhor')
    self.assertEqual(name, "Usmanov Abduqahhor")

unittest.main()
