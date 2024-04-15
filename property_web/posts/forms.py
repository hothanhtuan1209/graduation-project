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
            'price':  forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            if len(data) > 12:
                raise forms.ValidationError("Bạn chỉ được phép tải lên tối đa 12 ảnh.")
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ImageForm(forms.ModelForm):
    image = MultipleFileField(label='Chọn tối đa 12 ảnh:', required=True)

    class Meta:
        model = Image
        fields = ['image', ]
