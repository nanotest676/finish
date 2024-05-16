from rest_framework import serializers
from .models import Tag, Ingredient, Recipe, RecipeIngredient

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'measurement_unit']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredient', 'amount']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'author',
            'ingredients',
            'tags',
            'image',
            'text',
            'cooking_time',
            'is_favorited',
            'is_in_shopping_cart'
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(**ingredient_data['ingredient'])
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, amount=ingredient_data['amount'])
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooking_time = validated_data.get('cooking_time', instance.cooking_time)
        instance.tags.set(validated_data.get('tags', instance.tags))
        instance.save()

        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(**ingredient_data['ingredient'])
            RecipeIngredient.objects.update_or_create(recipe=instance, ingredient=ingredient, defaults={'amount': ingredient_data['amount']})
        return instance
