from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "cookingtime",
            "ingredients",
            "instructions",
            "notes",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_types",
            "calories",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        notes = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "cookingtime": "Cooking Time",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "notes": "Recipe Notes",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
