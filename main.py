from classes import *


# Зверніть увагу: ми навмисно передаємо зайві пробіли та табуляції (\t).
# Клас Text автоматично прибере їх під час ініціалізації.
blocks = [
    BuildingBlock("Stone Block.", 1.5, 1, 6.0, 0),
    BuildingBlock("Dirt Block.", 0.5, 2, 0.5, 0),
    BuildingBlock("Glowstone.", 0.3, 3, 0.3, 15),
    BuildingBlock("Obsidian.", 50.0, 4, 1200.0, 0),
    BuildingBlock("Glass Block.", 0.3, 5, 0.3, 0)
]

# Сортування працюватиме так само, бо ми додали метод __lt__ у клас Text
blocks.sort(key=lambda b: (b.name, -b.hardness))

print("--- Відсортовані блоки (назви нормалізовані) ---")
for b in blocks:
    print(b)

# При пошуку передаємо ідеально відформатований рядок (1 пробіл)
target = BuildingBlock("Stone Block.", 1.5, 1, 6.0, 0)
print(f"\n--- Результат пошуку ідентичного до '{target.name}' ---")

if target in blocks:
    found_block = blocks[blocks.index(target)]
    print(f"ЗНАЙДЕНО: {found_block}")
else:
    print("Об'єкт не знайдено.")
