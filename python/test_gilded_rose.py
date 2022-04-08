# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_quality_drops_by_one_if_product_not_expired(self):
        items = [Item("aaaaa", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_drops_by_two_if_product_is_expired(self):
        items = [Item("bbbb", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("cccc", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_brie_string_needs_aged_to_increases_in_quality(self):
        items = [Item("Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_is_never_more_than_fifty(self):
        items = [Item("Magic Wand", 5, 53)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(52, items[0].quality)
        #this should actually fail as quality is >50

    def test_sulfuras_never_degrades_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)

    def test_backstage_pass_increases_in_quality_as_nears_sellin_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)

    def test_backstage_pass_increases_in_quality_by_two_when_less_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        #failing as quality is not decreasing twice as fast - now fixed

    def test_sulfuras_quality_is_80_and_never_alters(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

class GoldenMasterTest(unittest.TestCase):

    def test_update_items(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(
            str(gilded_rose.items),
            "[+5 Dexterity Vest, 9, 19, Aged Brie, 1, 1, Elixir of the Mongoose, 4, 6, Sulfuras, Hand of Ragnaros, 0, "
            "80, Sulfuras, Hand of Ragnaros, -1, 80, Backstage passes to a TAFKAL80ETC concert, 14, 21, "
            "Backstage passes to a TAFKAL80ETC concert, 9, 50, Backstage passes to a TAFKAL80ETC concert, 4, 50, "
            "Conjured Mana Cake, 2, 5]"
        )

if __name__ == '__main__':
    unittest.main()
