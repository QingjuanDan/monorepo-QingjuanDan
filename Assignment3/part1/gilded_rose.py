# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdateItem:
    # helper class to update each item's sell_in and quality
    def update_item(self, item):
        pass

    def set_limit(self, item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            item.quality = 50


class NormalItem(UpdateItem):
    def update_item(self, item):
        if item.quality <= 50 and item.quality > 0:
            if item.sell_in <= 0:
                item.quality -= 2
            else:
                item.quality -= 1
        item.sell_in -= 1
        self.set_limit(item)


class AgedBrie(UpdateItem):
    def update_item(self, item):
        if item.quality <= 50:
            item.quality += 1
        item.sell_in -= 1
        self.set_limit(item)


class Sulfuras(UpdateItem):
    def update_item(self, item):
        pass


class BackstagePasses(UpdateItem):
    def update_item(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in <= 10 and item.sell_in > 5:
            item.quality += 2
        elif item.sell_in <= 5 and item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0
        item.sell_in -= 1
        self.set_limit(item)


class Conjured(UpdateItem):
    def update_item(self, item):
        if 0 < item.quality <= 50:
            if item.sell_in <= 0:
                item.quality -= 4
            else:
                item.quality -= 2
        item.sell_in -= 1
        self.set_limit(item)


class ItemUpdateHandler:
    # helper class to find each kind of item, and return the process class
    def update_item_handler(self, item):
        if item.name == "Aged Brie":
            return AgedBrie()
        elif item.name == "Sulfuras":
            return Sulfuras()
        elif item.name == "Backstage passes":
            return BackstagePasses()
        elif item.name == "Conjured":
            return Conjured()
        else:
            return NormalItem()


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        update_handler = ItemUpdateHandler()
        for item in self.items:
            item_update = update_handler.update_item_handler(item)
            item_update.update_item(item)
