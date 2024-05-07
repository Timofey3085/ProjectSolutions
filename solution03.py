"""Создать класс Point, который представляет собой
   точку в двумерном пространстве.
   Класс должен иметь методы для инициализации координат точки,
   вычисления расстояния до другой точки,
   а также для получения и изменения координат."""
from math import hypot


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return f"Coordinates: ({self.x}, {self.y})"

    def distance(self, other_point):
        return hypot(self.x - other_point.x, self.y - other_point.y)


# Пример использования
point1 = Point(3, 4)
point2 = Point(8, 1)
print(point1.coordinates())
print(point1.distance(point2))
