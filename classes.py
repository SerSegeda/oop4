import re


# --- Ієрархія тексту ---

class Letter:
    def __init__(self, char: str):
        self.char = char

    def __eq__(self, other):
        return isinstance(other, Letter) and self.char == other.char

    def __str__(self):
        return self.char


class Punctuation:
    def __init__(self, char: str):
        self.char = char

    def __eq__(self, other):
        return isinstance(other, Punctuation) and self.char == other.char

    def __str__(self):
        return self.char


class Word:
    def __init__(self, word_str: str):
        # Слово складається з масиву (списку) літер
        self.letters = [Letter(c) for c in word_str]

    def __eq__(self, other):
        return isinstance(other, Word) and self.letters == other.letters

    def __str__(self):
        return "".join(str(let) for let in self.letters)


class Sentence:
    def __init__(self, sentence_str: str):
        self.elements = []
        # Розбиваємо рядок на слова та знаки пунктуації
        tokens = re.findall(r"\w+|[^\w\s]", sentence_str)
        for token in tokens:
            if re.match(r"[^\w\s]", token):
                self.elements.append(Punctuation(token))
            else:
                self.elements.append(Word(token))

    def __eq__(self, other):
        return isinstance(other, Sentence) and self.elements == other.elements

    def __str__(self):
        res = ""
        for el in self.elements:
            if isinstance(el, Punctuation):
                res += str(el)
            else:
                res += (" " + str(el) if res else str(el))
        return res


class Text:
    def __init__(self, raw_string: str):
        # 1. Заміна табуляцій та множинних пробілів на один пробіл
        cleaned_string = re.sub(r'\s+', ' ', raw_string).strip()

        self.sentences = []

        # 2. Поділ на речення (розділяємо по крапці, знаку питання чи оклику)
        raw_sentences = re.split(r'(?<=[.!?])\s+', cleaned_string)
        for s in raw_sentences:
            if s:
                self.sentences.append(Sentence(s))

    def __eq__(self, other):
        return isinstance(other, Text) and self.sentences == other.sentences

    def __str__(self):
        return " ".join(str(s) for s in self.sentences)

    # Метод __lt__ потрібен, щоб функція sort() знала, як порівнювати ці об'єкти між собою
    def __lt__(self, other):
        return str(self) < str(other)


# --- Клас з Лабораторної №3 (модифікований) ---

class BuildingBlock:
    def __init__(self, name: str, hardness: float, block_id: int, resistance: float, light_level: int):

        # Замість базового str створюємо наш складений об'єкт Text
        self.name = Text(name)

        if not isinstance(hardness, (int, float)) or hardness < 0:
            raise ValueError("Твердість не може бути від'ємною")
        if not isinstance(block_id, int):
            raise TypeError("ID блоку має бути цілим числом")
        if not isinstance(light_level, int) or not (0 <= light_level <= 15):
            raise ValueError("Рівень світла має бути цілим числом від 0 до 15")

        self.hardness = float(hardness)
        self.block_id = block_id
        self.resistance = float(resistance)
        self.light_level = light_level

    def __eq__(self, other):
        if not isinstance(other, BuildingBlock):
            return False
        return (self.name == other.name and
                self.hardness == other.hardness and
                self.block_id == other.block_id and
                self.resistance == other.resistance and
                self.light_level == other.light_level)

    def __repr__(self):
        # При виводі конвертуємо об'єкт Text назад у рядок
        return f"Block(name='{str(self.name)}', id={self.block_id}, hardness={self.hardness}, res={self.resistance}, light={self.light_level})"
