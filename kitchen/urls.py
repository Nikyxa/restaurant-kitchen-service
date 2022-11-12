from django.urls import path
from .views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dishtype-list",
    ),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create",
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path(
        "cooks/<int:pk>/add_delete",
        toggle_assign_to_dish,
        name="add_delete_cook"
    )
]

app_name = "kitchen"
