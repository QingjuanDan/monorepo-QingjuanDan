# -*- coding: utf-8 -*-

import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_aged_brie(self):
        aged_brie_item = Item("Aged Brie", 5, 49)
        gilded_rose = GildedRose([aged_brie_item])

        # Verify that the quality of Aged Brie increases and its sell_in value decreases
        gilded_rose.update_quality()
        self.assertEqual(aged_brie_item.quality, 50)
        self.assertEqual(aged_brie_item.sell_in, 4)

        # Test for over 50
        gilded_rose.update_quality()
        self.assertEqual(aged_brie_item.quality, 50)

    def test_update_quality_sulfuras(self):
        sulfuras_item = Item("Sulfuras", 10, 80)
        gilded_rose = GildedRose([sulfuras_item])

        # Confirm that the quality and sell_in values of Sulfuras remain unchanged
        gilded_rose.update_quality()
        self.assertEqual(sulfuras_item.quality, 80)
        self.assertEqual(sulfuras_item.sell_in, 10)

    def test_update_quality_normal(self):
        other_item = Item("other one", 2, 20)
        gilded_rose = GildedRose([other_item])

        # Ensure Normal item quality and sell_in decrease
        gilded_rose.update_quality()
        self.assertEqual(other_item.quality, 19)
        self.assertEqual(other_item.sell_in, 1)

        # Test for sell_in below 0
        gilded_rose.update_quality()
        self.assertEqual(other_item.quality, 18)
        self.assertEqual(other_item.sell_in, 0)

        # Test for quality not going below 0 when sell_in < 0
        gilded_rose.update_quality()
        self.assertEqual(other_item.quality, 16)
        self.assertEqual(other_item.sell_in, -1)

        # Test for quality not going above 50
        other_item1 = Item("other one", 2, 55)
        gilded_rose1 = GildedRose([other_item1])
        gilded_rose1.update_quality()
        self.assertEqual(other_item1.quality, 50)
        self.assertEqual(other_item1.sell_in, 1)

    def test_update_quality_backstage_passes(self):
        # Backstage Passes - more than 10 days left
        backstage_item_1 = Item("Backstage passes", 15, 20)
        gilded_rose_1 = GildedRose([backstage_item_1])

        gilded_rose_1.update_quality()
        self.assertEqual(backstage_item_1.quality, 21)
        self.assertEqual(backstage_item_1.sell_in, 14)

        # Backstage Passes - 10 days left
        backstage_item_2 = Item("Backstage passes", 10, 30)
        gilded_rose_2 = GildedRose([backstage_item_2])

        gilded_rose_2.update_quality()
        self.assertEqual(backstage_item_2.quality, 32)
        self.assertEqual(backstage_item_2.sell_in, 9)

        # Backstage Passes - 5 days left
        backstage_item_3 = Item("Backstage passes", 5, 45)
        gilded_rose_3 = GildedRose([backstage_item_3])

        gilded_rose_3.update_quality()
        self.assertEqual(backstage_item_3.quality, 48)
        self.assertEqual(backstage_item_3.sell_in, 4)

        # Backstage Passes - 0 days left (concert day)
        backstage_item_4 = Item("Backstage passes", 0, 50)
        gilded_rose_4 = GildedRose([backstage_item_4])

        gilded_rose_4.update_quality()
        self.assertEqual(backstage_item_4.quality, 0)
        self.assertEqual(backstage_item_4.sell_in, -1)

        # Backstage Passes - already expired
        backstage_item_5 = Item("Backstage passes", -2, 10)
        gilded_rose_5 = GildedRose([backstage_item_5])

        gilded_rose_5.update_quality()
        self.assertEqual(backstage_item_5.quality, 0)
        self.assertEqual(backstage_item_5.sell_in, -3)

    def test_update_quality_conjured(self):
        # Conjured item - more than 0 days left
        conjured_item_1 = Item("Conjured", 5, 30)
        gilded_rose_1 = GildedRose([conjured_item_1])

        gilded_rose_1.update_quality()
        self.assertEqual(conjured_item_1.quality, 28)
        self.assertEqual(conjured_item_1.sell_in, 4)

        # Conjured item - 0 days left
        conjured_item_2 = Item("Conjured", 0, 30)
        gilded_rose_2 = GildedRose([conjured_item_2])

        gilded_rose_2.update_quality()
        self.assertEqual(conjured_item_2.quality, 26)
        self.assertEqual(conjured_item_2.sell_in, -1)

        # Conjured item - already expired
        conjured_item_3 = Item("Conjured", -2, 20)
        gilded_rose_3 = GildedRose([conjured_item_3])

        gilded_rose_3.update_quality()
        self.assertEqual(conjured_item_3.quality, 16)
        self.assertEqual(conjured_item_3.sell_in, -3)

        # Conjured item - quality not going below 0
        conjured_item_4 = Item("Conjured", 3, 1)
        gilded_rose_4 = GildedRose([conjured_item_4])

        gilded_rose_4.update_quality()
        self.assertEqual(conjured_item_4.quality, 0)
        self.assertEqual(conjured_item_4.sell_in, 2)


if __name__ == '__main__':
    unittest.main()

