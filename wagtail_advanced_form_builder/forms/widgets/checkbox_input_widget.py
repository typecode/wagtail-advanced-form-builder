from django.forms import CheckboxInput as DjangoCheckboxInput


class CheckboxInput(DjangoCheckboxInput):

    def __init__(self, display_checkbox_label=True, default_value="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display_checkbox_label = display_checkbox_label
        # self.default_value = default_value
        # print("default_value", default_value)

    def get_context(self, *args, **kwargs):

        context = super().get_context(*args, **kwargs)

        print("context", context)

        context['widget'].update({
            'display_checkbox_label': self.display_checkbox_label,
            # 'checked': bool(self.default_value)
        })

        return context
