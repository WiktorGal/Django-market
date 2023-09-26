from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemFrom(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'}),
            'name': forms.TextInput(attrs={'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'}),
            'price': forms.TextInput(attrs={'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'}),
            'image': forms.FileInput(attrs={'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'}),
        }


class EditItemFrom(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-2 px-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-400'  # Corrected class here
            })
        }
