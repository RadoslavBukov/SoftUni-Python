from django import forms

from exam_30_10_22.web.form_mixins import DisabledFormMixin
from exam_30_10_22.web.models import Profile, Car


# Profile form
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
            ),
            'email': forms.EmailInput(
            ),
            'age': forms.NumberInput(
            ),
            'password': forms.PasswordInput(
            ),
            'first_name': forms.TextInput(
            ),
            'last_name': forms.TextInput(
            ),
            'profile_picture': forms.URLInput(
            ),
        }

class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'profile_picture')


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


# Car form
class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(
            ),
            'year': forms.NumberInput(
            ),
            'image_url': forms.URLInput(
            ),
            'price': forms.NumberInput(
            ),
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(DisabledFormMixin, CarBaseForm):
    disabled_fields = ('type', 'model', 'year', 'image_url', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance