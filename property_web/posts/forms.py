from django import forms
from .models import Post
from images.models import Image
from category.models import Category
from property_web.constants.enum import Type


class PostForm(forms.ModelForm):
    type = forms.ChoiceField(
        label="Loại Bài Đăng",
        choices=[(type.value, type.value) for type in Type],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        label="Loại Bất Động Sản",
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['title', 'price', 'area', 'address', 'type', 'category', 'description']
        labels = {
            'title': 'Tiêu Đề',
            'price': 'Giá (VND)',
            'area': 'Diện Tích',
            'address': 'Địa Chỉ',
            'description': 'Mô tả',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': 'Select an Image',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
