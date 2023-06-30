from django.shortcuts import render
from .forms import CancerPredictForm
import pandas as pd
import joblib

# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        form = CancerPredictForm(request.POST)
        if form.is_valid():
            #Prepare data for model
            data = pd.DataFrame(form.cleaned_data, index=[0])

            #Use model to make a prediction
            prediction = model.predict(data)

            print(preidction)
            #Load your model
            
            return render(request, 'results.html', {'prediction': prediction})

    else:
        form = CancerPredictForm()

    return render(request, 'predict.html', {'form': form})