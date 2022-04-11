# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items, max_quality=50, min_quality=0, legendary_quality=80):
        self.items = items
        self.max_quality = max_quality
        self.min_quality = min_quality
        self.legendary_quality = legendary_quality

    def update_quality(self):
        for item in self.items:
            item.update_quality()

# Factory
class ItemUpdate(object):
    def update(self, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Conjured Mana Cake":
            return Conjured(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)

# Normal items
class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1


class AgedBrie(Item):
    def update_quality(self):
        # increase quality
        if self.quality < 50:
            self.quality = self.quality + 1
                # if sell in days have passed, increase quality twice
            if self.sell_in <= 0:
                self.quality = self.quality + 1

                # decrease sell_in days
        self.sell_in = self.sell_in - 1


class Sulfuras(Item):
    def update_quality(self):
        pass


class Conjured(Item):
    def update_quality(self):
        self.quality = (self.quality - 2) if self.quality > 2 else 0
        self.sell_in = self.sell_in - 1


class Backstage(Item):
    def update_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in = self.sell_in - 1

    # instances
    # def update_quality(self):
    #
    #     for item in self.items:
    #         if item.name == "Aged Brie":
    #             self.update_aged_brie(item)
    #         elif item.name == "Sulfuras, Hand of Ragnaros":
    #             self.update_sulfuras(item)
    #         elif item.name == "Backstage passes to a TAFKAL80ETC concert":
    #             self.update_backstage_passes(item)
    #         elif item.name == "Conjured Mana Cake":
    #             self.update_conjured_mana_cake(item)
    #         else:
    #             self.update_normal_items(item)
    #
    # def update_normal_items(self, item):
    #     # decrease quality
    #     if item.quality > self.min_quality:
    #         item.quality = item.quality - 1
    #         # if sell in days have passed, decrease quality twice
    #         if item.sell_in <= 0:
    #             item.quality = item.quality - 1
    #
    #     # decrease sell_in days
    #     item.sell_in = item.sell_in - 1
    #
    # def update_sulfuras(self, item):
    #     item.quality == self.legendary_quality
    #     print(self.items[3])
    #
    #
    # def update_aged_brie(self, item):
    #     # increase quality
    #     if item.quality < self.max_quality:
    #         item.quality = item.quality + 1
    #         # if sell in days have passed, increase quality twice
    #         if item.sell_in <= 0:
    #             item.quality = item.quality + 1
    #
    #         # decrease sell_in days
    #     item.sell_in = item.sell_in - 1
    #
    # def update_backstage_passes(self, item):
    #     # increase quality
    #     if 10 >= item.sell_in > 5:
    #         item.quality = item.quality + 2
    #     elif 5 >= item.sell_in > 0:
    #         item.quality = item.quality + 3
    #     elif item.sell_in <= 0:
    #         item.quality = 0
    #     else:
    #         item.quality = item.quality + 1
    #
    #     if item.quality > self.max_quality:
    #         item.quality = self.max_quality
    #
    #     # decrease sell_in days
    #     item.sell_in = item.sell_in - 1
    #
    # def update_conjured_mana_cake(self, item):
    #     # decrease quality twice
    #     if item.quality > self.min_quality:
    #         item.quality = item.quality - 2
    #         # if sell in days have passed, decrease quality twice
    #         if item.sell_in <= 0:
    #             item.quality = item.quality - 2
    #
    #     if item.quality < self.min_quality:
    #         item.quality = self.min_quality
    #
    #     # decrease sell_in days
    #     item.sell_in = item.sell_in - 1