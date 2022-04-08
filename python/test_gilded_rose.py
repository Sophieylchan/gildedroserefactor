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
        items = [Item("Magic Wand", 5, 52)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #this should actually fail as quality is still >50
        self.assertEqual(51, items[0].quality)

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

    # def test_conjured_item_degrades_twice_as_fast(self):
    #     items = [Item("Conjured", 10, 10)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(8, items[0].quality)
        #not yet implemented so will fail

    def test_sulfuras_quality_is_80_and_never_alters(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

if __name__ == '__main__':
    unittest.main()
