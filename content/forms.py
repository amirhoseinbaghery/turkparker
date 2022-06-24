from django import forms
from django.core import validators

choice = (
    ('پشتیبانی سایت', 'پشتیبانی سایت'),
    ('انتقادات و پیشنهادات', 'انتقادات و پیشنهادات'),
    ('پیگیری سفارش', 'پیگیری سفارش'),
    ('پشتیبانی محصول', 'پشتیبانی محصول'),
    ('مدیریت', 'مدیریت'),
    ('حسابداری و امورمالی ', 'حسابداری و امورمالی'),
    ('سایر موضوعات', 'سایر موضوعات'),
)


class ContactUsForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control form-control-solid"}),
        label='نام و نام خانوادگی',
        required=True,
        validators=[validators.MaxLengthValidator(150, 'حداکثر 150 کارکتر')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control form-control-solid"}),
        label='ایمیل',
        required=True

    )
    subject = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control form-control-solid select2-selection select2-selection--single form-select "}),
        label='موضوع',
        choices=choice,
        initial='',
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control form-control-solid"}),
        label='متن پیام',
        required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control form-control-solid"}),
        label='تلفن تماس',
        required=True,
        validators=[validators.MaxLengthValidator(11, 'حداکثر 11 کارکتر'), validators.MinLengthValidator(11, 'حداقل '
                                                                                                             '11 '
                                                                                                             'کارکتر')],
    )