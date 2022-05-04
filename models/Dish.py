from typing import List
from pydantic import BaseModel
from uuid import UUID


class Dish(BaseModel):
    id: UUID
    name: str
    price: float
    ingredients: List[str]
