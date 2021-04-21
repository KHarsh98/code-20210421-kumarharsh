from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Person
import json

# vamstar request handler

def total_overweight():
    count = 0
    for p in Person.objects.all():
        if p.bmi > 25.0:
            count+=1
    return count


def handle(request):
    if request.method == "POST":
        json_data = request.read() # read json data
        data = json.loads(json_data) # convert it into list
        

        for d in data:
            p = Person()
            for key, value in d.items():
                if key == "Gender":
                    p.gender = value
                elif key == "HeightCm":
                    height = float(value)
                elif key == "WeightKg":
                    weight = float(value)

            try:
                bmi = weight/(height / 100.0)
            except ZeroDivisionError:
                print("Cannot divide by zero")
                return HttpResponseBadRequest('This view can not handle method {0}'.\
                                      format(request.method), status=405)
            else:
                   print(bmi)
            p.bmi = bmi
            if bmi <= 18.4:
                p.bmi_cat = "Underweight"
                p.health_risk = "Malnutrition risk"

            elif bmi > 18.5 and bmi <= 24.9:
                p.bmi_cat = "Normal weight"
                p.health_risk = "Low risk"

            elif bmi > 25.0 and bmi <= 29.9:
                p.bmi_cat = "Overweight"
                p.health_risk = "Enhanced risk"
        
            elif bmi > 30.0 and bmi <= 34.9:
                p.bmi_cat = "Moderately obese"
                p.health_risk = "Medium risk"

            elif bmi > 35.0 and bmi <= 39.9:
                p.bmi_cat = "Severely obese"
                p.health_risk = "High risk"
            
            elif bmi > 40.0:
                p.bmi_cat = "Very severely obese"
                p.health_risk = "Very high risk"

            p.save()        

            total_count = total_overweight()
            context = {'total_overweight':total_count} # ignore, just for testing

        return render(request, 'pages/result.html', context)



