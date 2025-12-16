from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import CustomUser

from phonenumber_field.formfields import SplitPhoneNumberField, PrefixChoiceField
from  phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.safestring import mark_safe
from phonenumber_field.formfields import REGION_CODE_TO_COUNTRY_CODE

def get_flag_country_choices():
    """
    Generate choices with flag emoji + country code (e.g., 🇳🇬 NG)
    instead of full country names.
    
    The choice key must be the region_code (NG, GB, US, etc.) because
    SplitPhoneNumberField.prefix_field() uses PrefixChoiceField which
    validates against region codes, not country codes.
    """
    choices = [("", "---------")]
    for region_code, country_code in REGION_CODE_TO_COUNTRY_CODE.items():
        # Generate flag emoji from region code (A=🇦, B=🇧, etc.)
        flag = ''.join(chr(0x1F1E6 + ord(c) - ord('A')) for c in region_code)
        label = f"{flag} {region_code}"
        choices.append((region_code, label))
    # Sort by region code for easier lookup
    choices.sort(key=lambda x: x[0] if x[0] else "")
    return choices

class InlinePhoneWidget(PhoneNumberPrefixWidget):
    """Wrap the rendered MultiWidget output in a div so we can style it as one line."""
    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        return mark_safe(f'<div class="phone-inline">{rendered}</div>')
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"John"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"mt-1 w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"Doe"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"w-full pl-10 pr-10 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"johndoe@gmail.com"
            }
        )
    )
    phone_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class":"w-full pl-10 pr-10 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"2347000000000"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"w-full pl-10 pr-10 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"************"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"w-full pl-10 pr-10 py-2 border border-gray-300 rounded-md focus:ring-green-500 focus:border-green-500",
                "placeholder":"************"
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2',
                  'first_name', 'last_name', 'phone_number']
