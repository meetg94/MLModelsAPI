from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=[(1, 'Male'), (2, 'Female')], label="Gender")

    genetic_risk = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Genetic Risk")
    chronic_lung_disease = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Chronic Lung Disease")

    coughing_of_blood = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Coughing of Blood")
    alcohol_use = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Alcohol Use")
    fatigue = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Fatigue")
    wheezing = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Wheezing")
    smoking = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Smoking")
    passive_smoker = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Passive Smoker")
    obesity = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Obesity")
    dust_allergy = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Dust Allergy")
    frequent_cold = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Frequent Cold")
    clubbing_of_finger_nails = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Clubbing of Finger Nails")
    shortness_of_breath = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Shortness of Breath")
    air_pollution = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Air Pollution")
    snoring = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Snoring")
    balanced_diet = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Balanced Diet")
    occupational_hazards = forms.ChoiceField(choices=[(x, x) for x in range(0, 10)], label="Occupational Hazards")
