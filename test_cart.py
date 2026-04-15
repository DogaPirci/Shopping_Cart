import unittest
from cart import ShoppingCart
class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item_sum(self):
        self.cart.add_item("Elma", 5.0, 2)
        self.assertEqual(self.cart.get_total(), 10.0)

    def test_ayni_urun_miktar_artisi(self):
        self.cart.add_item("Süt", 20.0, 1)
        self.cart.add_item("Süt", 20.0, 2)
        self.assertEqual(self.cart.get_item_count(), 3)

    def test_yuzde_indirim_kodu(self):
        self.cart.add_item("Kitap", 100.0, 1)
        self.cart.apply_discount("SAVE10")
        self.assertEqual(self.cart.get_total(), 90.0)

    def test_sinir_deger_indirimi(self):
        self.cart.add_item("Defter", 30.0, 1)
        self.cart.apply_discount("FLAT5")
        self.assertEqual(self.cart.get_total(), 25.0)

    def test_olmayan_urunu_sil(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("Hayali Ürün")
            
    def test_hatali_miktar_girisi(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Hata", 10.0, -1)
            
    def test_sepeti_temizle(self):
        self.cart.add_item("Kalem", 5.0, 1)
        self.cart.clear()
        self.assertEqual(self.cart.get_item_count(), 0)

if __name__ == '__main__':
    unittest.main()# pragma: no cover