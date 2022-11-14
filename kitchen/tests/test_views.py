from unittest import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook
from kitchen.views import DishTypeListView


class PublicAllViewsTests(TestCase):
    def test_login_required_dishtype(self) -> None:
        res = self.client.get(reverse("kitchen:dishtype-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_dish(self) -> None:
        res = self.client.get(reverse("kitchen:dish-list"))
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_cook(self) -> None:
        res = self.client.get(reverse("kitchen:cook-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sandychicks",
        )
        self.client.force_login(self.user)

    def test_retrieve_dishtypes(self):
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Dessert")
        DishType.objects.create(name="Main")
        DishType.objects.create(name="Starter")
        DishType.objects.create(name="Salad")

        response = self.client.get(reverse("kitchen:dishtype-list"))
        dishtypes = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype-list"]),
            list(dishtypes)
        )
        self.assertTemplateUsed(response, "kitchen/dishtype_list.html")
        self.assertEqual(
            len(response.context["dishtype-list"]),
            DishTypeListView.paginate_by
        )


class PrivateDishTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sandychicks",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(
            name="Pizza",
        )
        Dish.objects.create(name="Ritta", dish_type=dish_type)
        Dish.objects.create(name="Havai", dish_type=dish_type)

        response = self.client.get(reverse("kitchen:dish-list"))
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class CookCarTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="sandychicks",
            password="123chicks",
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        get_user_model().objects.create_user(
            username="patrik",
            password="123patrick",
        )
        get_user_model().objects.create_user(
            username="spongebob",
            password="098sponge",
        )

        response = self.client.get(reverse("kitchen:cook-list"))
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
