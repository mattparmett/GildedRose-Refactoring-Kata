# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.max_quality = 50
        self.min_quality = 0

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in -= 1
            quality_change = -1  # by default quality decr by 1 each day

            if item.name == "Aged Brie":
                quality_change = 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    quality_change = -item.quality
                elif item.sell_in <= 5:
                    quality_change = 3
                elif item.sell_in <= 10:
                    quality_change = 2
                else:
                    quality_change = 1

            elif "Conjured" in item.name:
                quality_change = -2

            item.quality += quality_change

            if item.quality > self.max_quality:
                item.quality = self.max_quality

            if item.quality < self.min_quality:
                item.quality = self.min_quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
