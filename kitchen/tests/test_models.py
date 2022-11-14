from unittest import TestCase

from django.contrib.auth import get_user_model

from kitchen.models import DishType, Dish, Cook


class DishTypeModelTest(TestCase):

    def test_dishtype_str(self):
        dishtype = DishType.objects.create(
            name="Pizza"
        )
        expected_object_name = f"{dishtype.name}"
        self.assertEqual(str(dishtype), expected_object_name)


class DishModelTest(TestCase):

    def test_dish_str(self):
        dish = Dish.objects.create(
            name="Tiramisu",
        )
        self.assertEqual(str(dish), dish.model)


class CookModelTest(TestCase):

    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="sandychicks",
            password="123chicks",
            first_name="Sandy",
            last_name="Chicks",
            years_of_experience=8,
            position="Pastry Chef"
        )

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "Sandy Chicks (Pastry Chef)")

    def test_get_absolute_url(self):
        cook = Cook.objects.get(id=1)
        self.assertEqual(cook.get_absolute_url(), "/cooks/1/")

    def test_create_cook_with_experience(self):
        self.assertEqual(self.cook.username, "sandychicks")
        self.assertTrue(self.cook.check_password("123chicks"))
        self.assertEqual(self.cook.years_of_experience, 8)
