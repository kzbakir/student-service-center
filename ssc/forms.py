from django.forms import ModelForm, NumberInput, FileInput, TextInput
from ssc.models import *
from captcha.fields import ReCaptchaField, ReCaptchaV3


class ReferenceForm(ModelForm):
    """
    Форма для заявление услуги - "Выдача справки лицам, не завершившим высшее и послевузовское образование"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    class Meta:
        model = Reference
        fields = "__all__"
        widgets = {
            'course': NumberInput(attrs={'min': 1, 'max': 5}),
            'receipt_year': NumberInput(attrs={'min': 1953, 'max': year_}),
            'exclude_year': NumberInput(attrs={'min': 1953, 'max': year_})
        }

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.fields['specialty'].label = 'Специальность'
        self.fields['status'].required = False


class AcademicLeaveForm(ModelForm):
    """
    Форма для заявление услуги - "Предоставление академических отпусков обучающимся в организациях образования"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    class Meta:
        model = AcademicLeave
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AcademicLeaveForm, self).__init__(*args, **kwargs)
        self.fields['reason'].label = 'Причина (в связи)'
        self.fields['specialty'].label = 'Специальность'
        self.fields['attachment'].label = 'Прикрепление файла копии заключения/решения/свидетельства/повестки'
        self.fields['status'].required = False


class AbroadForm(ModelForm):
    """
    Форма для заявление услуги - "Прием документов для участия в конкурсе на обучение за рубежом, в том числе академической мобильности"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    class Meta:
        model = Abroad
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AbroadForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False


class HostelForm(ModelForm):
    """
    Форма для заявление услуги - "Предоставление общежития в высших учебных заведениях"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    class Meta:
        model = Hostel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HostelForm, self).__init__(*args, **kwargs)
        self.fields['specialty'].label = 'Специальность'
        self.fields['status'].required = False


# class DuplicateForm(ModelForm):
#     """
#     Форма для заявление услуги - "Выдача справки лицам, не завершившим высшее и послевузовское образование"
#     """
#     captcha = ReCaptchaField(
#         widget=ReCaptchaV3(
#             attrs={
#                 'required_score': 0.85
#             }
#         )
#     )
#
#     class Meta:
#         model = Duplicate
#         fields = "__all__"
#
#     def __init__(self, *args, **kwargs):
#         super(DuplicateForm, self).__init__(*args, **kwargs)
#         self.fields['reason'].label = 'Причина (в связи)'
#         self.fields['specialty'].label = 'Специальность'
#         self.fields['status'].required = False


class TransferForm(ModelForm):
    """
    Форма для заявление услуги - "Перевод в другой ВУЗ"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    widgets = {
        'course': NumberInput(attrs={'min': 1, 'max': 5})
    }

    class Meta:
        model = Transfer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['university'].label = 'ВУЗ перевода'
        self.fields['status'].required = False


class TransferKSTUForm(ModelForm):
    """
    Форма для заявление услуги - "Перевод в КарГТУ"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    widgets = {
        'course': NumberInput(attrs={'min': 1, 'max': 5})
    }

    class Meta:
        model = TransferKSTU
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TransferKSTUForm, self).__init__(*args, **kwargs)
        self.fields['university'].label = 'Предыдущий ВУЗ'
        self.fields['grant'].label = 'Свидетельство о образовательном гранте(если грант)'
        self.fields['status'].required = False


class RecoveryForm(ModelForm):
    """
    Форма для заявление услуги - "Восстановление в число обучающихся"
    """
    captcha = ReCaptchaField(
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.85
            }
        )
    )

    widgets = {
        'course': NumberInput(attrs={'min': 1, 'max': 5})
    }

    class Meta:
        model = Recovery
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RecoveryForm, self).__init__(*args, **kwargs)
        self.fields['specialty'].label = 'Специальность'
        self.fields['university'].label = 'Предыдущий ВУЗ'
        self.fields['status'].required = False
