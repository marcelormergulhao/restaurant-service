from uuid import uuid4
from models.Dish import Dish


class DishRepository:
    MOCK_DISHES = [
        Dish(id=uuid4(), name="Simple Pasta",
             price=1.5, ingredients=["Pasta, Tomato"]),
        Dish(id=uuid4(), name="Mac and Cheese",
             price=2.5, ingredients=["Pasta, Cheese"]),
        Dish(id=uuid4(), name="Pasta with Basil",
             price=3.5, ingredients=["Pasta, Basil"]),
        Dish(id=uuid4(), name="Pasta Aioli",
             price=4.5, ingredients=["Pasta, Garlic"])
    ]

    def get_dishes(self):
        return DishRepository.MOCK_DISHES

    def create_dish(self, dish):
        DishRepository.MOCK_DISHES.append(dish)
        return dish

    def delete_dish(self, dish_id):
        current_size = len(DishRepository.MOCK_DISHES)
        DishRepository.MOCK_DISHES = filter(lambda x: x.id != dish_id, DishRepository.MOCK_DISHES)
        updated_size = len(DishRepository.MOCK_DISHES)
        return current_size != updated_size
