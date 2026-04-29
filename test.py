from classes import *
import unittest

class TestBuildingBlockSystem(unittest.TestCase):
    def test_text_cleaning_tabs_and_spaces(self):
        """Перевірка видалення зайвих пробілів та табуляцій."""
        raw_text = "Stone\t\tBlock   \t."
        text = Text(raw_text)
        self.assertEqual(str(text), "Stone Block.")

    def test_text_sentence_splitting(self):
        """Перевірка правильного розбиття тексту на окремі речення."""
        raw_text = "First! Second. Third?"
        text = Text(raw_text)
        self.assertEqual(len(text.sentences), 3)

    def test_sentence_parsing_words_and_punctuation(self):
        """Перевірка розпізнавання слів та розділових знаків у реченні."""
        sentence = Sentence("Hello, world!")
        self.assertEqual(len(sentence.elements), 4)
        self.assertIsInstance(sentence.elements[1], Punctuation)
        self.assertIsInstance(sentence.elements[2], Word)

    def test_word_and_letter_creation(self):
        """Перевірка розбиття слова на масив літер."""
        word = Word("Cat")
        self.assertEqual(len(word.letters), 3)
        self.assertEqual(word.letters[0].char, "C")

    def test_text_comparison_less_than(self):
        """Перевірка магічного методу __lt__ для майбутнього сортування."""
        text1 = Text("Alpha Block.")
        text2 = Text("Zebra Block.")
        self.assertTrue(text1 < text2)

    def test_building_block_creation(self):
        """Перевірка успішного створення блоку та ініціалізації поля Text."""
        block = BuildingBlock("Stone", 1.5, 1, 6.0, 15)
        self.assertEqual(str(block.name), "Stone")
        self.assertEqual(block.light_level, 15)


if __name__ == "__main__":
    unittest.main()