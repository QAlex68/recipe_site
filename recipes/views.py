from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category, Profile
from .forms import RecipeForm, CategoryForm, UserRegistrationForm, ProfileEditForm


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Проверяем, что текущий пользователь — автор рецепта
    if recipe.author != request.user:
        return redirect('recipe_detail', pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    return render(request, 'recipes/add_category.html', {'form': form, 'categories': categories})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'recipes/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'recipes/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Предполагается, что есть URL с именем 'profile'
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'recipes/edit_profile.html', {'form': form})

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Проверяем, является ли автором текущий пользователь
    if recipe.author != request.user:
        raise Http404("Вы не можете удалить этот рецепт.")

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')  # Перенаправляем на главную страницу

    return render(request, 'recipes/confirm_delete_recipe.html', {'recipe': recipe})
