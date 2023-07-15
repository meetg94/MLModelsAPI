from django import forms

class CancerPredictForm(forms.Form):
    # Genetic Information
    age = forms.IntegerField(min_value=1, max_value=100)
    genetic_risk = forms.IntegerField(min_value=0, max_value=9)
    chronic_lung_disease = forms.IntegerField(min_value=0, max_value=9)

    # Gender
    GENDER_CHOICES = [(1, "Male"), (2, "Female")]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    # Environmental Data
    coughing_of_blood = forms.IntegerField(min_value=0, max_value=9)
    alcohol_use = forms.IntegerField(min_value=0, max_value=9)
    fatigue = forms.IntegerField(min_value=0, max_value=9)
    wheezing = forms.IntegerField(min_value=0, max_value=9)
    smoking = forms.IntegerField(min_value=0, max_value=9)
    passive_smoker = forms.IntegerField(min_value=0, max_value=9)
    obesity = forms.IntegerField(min_value=0, max_value=9)
    dust_allergy = forms.IntegerField(min_value=0, max_value=9)
    frequent_cold = forms.IntegerField(min_value=0, max_value=9)
    clubbing_of_finger_nails = forms.IntegerField(min_value=0, max_value=9)
    shortness_of_breath = forms.IntegerField(min_value=0, max_value=9)
    air_pollution = forms.IntegerField(min_value=0, max_value=9)
    snoring = forms.IntegerField(min_value=0, max_value=9)
    balanced_diet = forms.IntegerField(min_value=0, max_value=9)
    occupational_hazards = forms.IntegerField(min_value=0, max_value=9)

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)
        for field_name, field_value in initial.items():
            self.fields[field_name].initial = field_value
            