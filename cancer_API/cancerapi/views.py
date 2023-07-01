from django.shortcuts import render
from .forms import CancerPredictForm
import pandas as pd
from joblib import load

#Model
model = load('model.pkl')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        form = CancerPredictForm(request.POST)
        if form.is_valid():
            features = form.cleaned_data

            # The order of features as used in model training
            ordered_features = ['coughing_of_blood', 'alcohol_use', 'fatigue', 'wheezing', 'smoking',
                                'passive_smoker', 'obesity', 'dust_allergy', 'frequent_cold',
                                'clubbing_of_finger_nails', 'shortness_of_breath', 'air_pollution',
                                'snoring', 'balanced_diet', 'occupational_hazards', 'gender', 'age',
                                'genetic_risk', 'chronic_lung_disease']
            #Prepare data for model
            df = pd.DataFrame(features, index=[0])

            #Decoding to get the level of prediction
            decode_map = { 0: 'Low', 1: 'Medium', 2: 'High' }

            df = df[ordered_features]
            #Use model to make a prediction
            prediction = model.predict(df)

            decoded_prediction = decode_map[prediction[0]]
            
            return render(request, 'result.html', {'prediction': decoded_prediction })

    else:
        form = CancerPredictForm()

    return render(request, 'predict.html', {'form': form})