import uvicorn
from fastapi import FastAPI, Response, status

from repository.DishRepository import DishRepository
from models.Dish import Dish

app = FastAPI()

dish_repository = DishRepository()


@app.get("/dishes")
def get_dishes():
    dishes = dish_repository.get_dishes()
    return dishes


@app.post("/dishes")
def create_dish(dish: Dish):
    return dish_repository.create(dish)


@app.delete("/dishes/{dish_id}", status_code=404)
def delete_dish(dish_id: str, response: Response):
    if dish_repository.delete_dish(dish_id):
        response.status_code = status.HTTP_204_NO_CONTENT

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info")
