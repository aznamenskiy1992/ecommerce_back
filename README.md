# Бэкенд для интернет-магазина

## Цель проекта:
Здесь будет описание

## Установка
1. Убедитесь, то у вас установлен Poetry. Если нет:
```
pip install --user poetry
```
2. Создайте виртуальное окружение
```
poetry install
```
3. Клонируйте репозиторий
```
git clone https://github.com/aznamenskiy1992/ecommerce_back.git
```

## Тестирование
Проект включает комплексные тесты для всех основных функций. Для запуска тестов используйте:
```
pytest tests/ -v
```

### Описание тестовых сценариев

#### Тестирование категорий товаров:
1. `test_add_category` - проверяет корректность создания новой категории
2. `test_add_product_in_category` - проверяет добавление товара в категорию
3. `test_add_not_object_product_in_category` - проверяет обработку ошибки при добавлении неверного типа товара
4. `test_print_products_in_category` - проверяет вывод списка товаров категории
5. `test_print_quantity_by_category` - проверяет вывод информации по остаткам товаров

#### Тестирование товаров:
1. `test_init_product` - проверяет корректность создания товара
2. `test_add_product_from_dict` - проверяет создание товара из словаря
3. `test_new_price_less_0` - проверяет обработку невалидной цены
4. `test_new_price_more_0` - проверяет установку валидной цены
5. `test_print_products_info` - проверяет вывод информации о товаре
6. `test_sum_products` - проверяет сложение стоимости товаров
7. `test_other_is_not_product_object` - проверяет обработку ошибки при сложении с не-товаром

#### Тестирование специализированных товаров:
1. `test_init_smartphone_class` - проверяет создание смартфона
2. `test_smartphone_isinstance_product` - проверяет наследование от Product
3. `test_init_lawn_grass_class` - проверяет создание газонной травы
4. `test_lawn_grass_isinstance_product` - проверяет наследование от Product
5. `test_add_smartphones` - проверяет сложение смартфонов
6. `test_error_for_add_smartphone_and_lawn_grass` - проверяет ошибку при сложении разных типов
7. `test_add_lawn_grass` - проверяет сложение газонных трав

### Покрытие тестами
Для проверки покрытия кода тестами используйте:
```
pytest --cov=src --cov-report=html
```
Отчет будет сгенерирован в директории `htmlcov/`

## Работа с классами и функциями

### Класс Category
Класс для представления категории товаров в магазине.

**Атрибуты:**
- `product_count` (int): Общее количество товаров во всех категориях (статический)
- `category_count` (int): Общее количество категорий (статический)
- `name` (str): Название категории
- `description` (str): Описание категории
- `products` (property): Свойство для получения форматированного списка товаров

**Методы:**
- `__init__(name, description, products)` - инициализирует категорию
- `add_product(product)` - добавляет товар в категорию
- `__str__()` - возвращает строку с информацией об остатках

**Пример использования:**
```python
products = [Product("Телевизор", "4K OLED", 100000, 5)]
category = Category("Электроника", "Техника для дома", products)
print(category)  # "Электроника, количество продуктов: 5 шт."
```

### Класс Product

Класс для представления товара в интернет-магазине.

#### Атрибуты:
| Атрибут       | Тип    | Описание                          | Доступность   |
|---------------|--------|-----------------------------------|---------------|
| `name`        | str    | Название товара                   | public        |
| `description` | str    | Описание товара                   | public        |
| `__price`     | float  | Приватное поле для хранения цены  | private       |
| `quantity`    | int    | Количество товара на складе       | public        |

#### Свойства:
- `price` (property):  
  Геттер/сеттер для работы с ценой товара.  
  При установке новой цены выполняется проверка на положительное значение.

#### Методы:

##### `__init__(name, description, price, quantity)`
Конструктор класса.  
**Параметры:**
- `name` (str) - название товара
- `description` (str) - описание товара
- `price` (float) - цена товара (должна быть > 0)
- `quantity` (int) - количество товара

**Пример:**
```python
product = Product("Ноутбук", "Игровой ноутбук", 120000, 3)
```

`new_product(product_dict)` (classmethod)
Фабричный метод для создания товара из словаря.
**Параметры:**

- `product_dict (dict)` - словарь с ключами:
    - name, 
    - description, 
    - price, 
    - quantity

**Возвращает:**
Экземпляр класса Product

**Пример:**
```python
data = {
    "name": "Наушники",
    "description": "Беспроводные",
    "price": 15000,
    "quantity": 10
}
product = Product.new_product(data)
```

`__str__()`
Возвращает строковое представление товара.

**Формат:**
`Название, цена руб. Остаток: кол-во шт.`

**Пример:**
```python
print(product)  # "Наушники, 15000 руб. Остаток: 10 шт."
```

`__add__(other)`
Позволяет складывать товары по формуле:
`(цена * количество) + (цена другого товара * его количество)`

**Параметры:**

`other (Product)` - другой товар для сложения

**Возвращает:**
Общую стоимость (float)

**Исключения:**

`TypeError` - если передан не объект Product

**Пример:**
```python
total = product1 + product2  # Сумма стоимостей товаров
```

**Особенности:**
1. Цена защищена от некорректных значений:
```python
product.price = -100  # Выведет предупреждение и не изменит цену
```
2. Поддерживает создание как напрямую, так и через фабричный метод
3. Имеет информативное строковое представление
4. Реализует логику сложения товаров по их общей стоимости

**Пример полного использования:**
```python
# Создание товара
p1 = Product("Мышь", "Беспроводная", 4500, 15)

# Изменение цены
p1.price = 5000  # Успешно
p1.price = -100  # Ошибка (цена не изменится)

# Получение информации
print(p1)  # "Мышь, 5000 руб. Остаток: 15 шт."

# Сложение с другим товаром
p2 = Product("Клавиатура", "Механическая", 8000, 7)
total_value = p1 + p2  # 5000*15 + 8000*7 = 131000
```
