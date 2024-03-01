from django import forms
from django.contrib.auth import get_user_model
from . import models


# class ArticleMenuForm(forms.Form):
#     description = forms.CharField(max_length=100)
#     hide = forms.BooleanField(required=False)


class ArticleMenuForm(forms.ModelForm):
    class Meta:
        model = models.ArticleMenu
        fields = ("description", "hide", "parent")


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ("header", "perex", "body", "menu", "published")


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "username", "is_active", "is_staff", "is_superuser")
