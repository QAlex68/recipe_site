from django import forms
from .models import Recipe, Category, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Форма для создания/редактирования рецептов
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cook_time', 'image', 'category']
        labels = {
            'title': 'Название блюда',
            'description': 'Описание',
            'steps': 'Шаги приготовления',
            'cook_time': 'Время приготовления',
            'image': 'Изображение',
            'category': 'Категория',
        }
        # help_texts = {
        #     'title': 'Введите уникальное название для блюда.',
        #     'description': 'Опишите ваше блюдо кратко.',
        #     'steps': 'Опишите шаги приготовления подробно.',
        #     'cook_time': 'Укажите время в минутах.',
        #     'image': 'Загрузите изображение блюда.',
        #     'category': 'Выберите категорию блюда.',
        # }


# Форма для создания категорий
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название категории',
        }
        help_texts = {
            'name': 'Введите название категории, например, "Супы" или "Десерты".',
        }


# Форма для регистрации пользователя
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',

        }
        help_texts = {
            'username': 'Введите уникальный логин для входа в систему.',
            'password': 'Придумайте надёжный пароль.',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }