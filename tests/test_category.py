def test_category_init(category_one) -> None:
    assert category_one.name == "Смартфоны"
    assert category_one.description == (
        "Смартфоны, как средство не только коммуникации, но и получение " "дополнительных функций для удобства жизни"
    )
    assert category_one.products[0].name == "Samsung Galaxy S23 Ultra"

    assert category_one.category_count == 1
    assert category_one.product_count == 1
