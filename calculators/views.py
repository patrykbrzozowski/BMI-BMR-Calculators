from os import stat
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html', context={'calc_what': 'Home'})


def BMI_calculator(request):
    context = {}
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height')) / 100

        bmi = weight / height ** 2
        

        if bmi < 16:
            state = "Wygłodzenie"
        elif 16 < bmi < 16.99:
            state = "Wychudzenie"
        elif 17 < bmi < 18.49:
            state = "Niedowaga"
        elif 18.5 < bmi < 24.99:
            state = "Waga prawidłowa"
        elif 25 < bmi < 29.99:
            state = "Nadwaga"
        elif 30 < bmi < 34.99:
            state = "Otyłość I Stopnia"
        elif 35 < bmi < 39.99:
            state = "Otyłość II stopnia (tzw. Kliniczna)"
        elif bmi > 40:
            state = "Otyłość III stopnia"


        context['bmi'] = round(bmi, 1)
        context['state'] = state

    context['calc_what'] = 'BMI'

    return render(request, 'index.html', context)

def BMR_calculator(request):
    context = {}
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        goal = request.POST.get('goal')
        activity = request.POST.get('activity')

        if gender == 'M':
            bmr = 66 + (13.7*weight) + (5*height) - (6.8*age)
            base_bmr = bmr
            correct_form = 'powinieneś'
        else:
            bmr = 655 + (9.6*weight) + (1.8*height) - (4.7*age)
            base_bmr = bmr
            correct_form = 'powinnaś'

        if activity == 'vl1':
            bmr *= 1.3
        elif activity == 'vl2':
            bmr *= 1.5
        elif activity == 'med':
            bmr *= 1.7
        elif activity == 'vh1':
            bmr *= 1.9
        else:
            bmr *= 2.3

        if goal == 'lose':
            bmrgoal = bmr - 300
            goal_form = 'schudnąć'
        elif goal == 'gain':
            bmrgoal = bmr + 300
            goal_form = 'przytyć'
        else:
            bmrgoal = bmr
            goal_form = 'utrzymać wagę'
                
        context['bmr'] = int(bmr)
        context['bmrgoal'] = int(bmrgoal)
        context['goal'] = goal
        context['correct_form'] = correct_form
        context['base_bmr'] = int(base_bmr)
        context['goal_form'] = goal_form
    
    context['calc_what'] = 'BMR'

    return render(request, 'index.html', context)
