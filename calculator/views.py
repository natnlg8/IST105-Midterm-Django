from django.db.models.expressions import result
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .form import MathForm


# Create your views here.


class CalculateView(TemplateView):
    template_name = 'math_form.html'
    form_class = MathForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            n1 = form.cleaned_data['number1']
            n2 = form.cleaned_data['number2']
            operator = form.cleaned_data['operator']

            respond = {}
            result_math = 0
            if operator == '+':
                result_math = n1 + n2
            elif operator == '-':
                result_math = n1 - n2
            elif operator == '*':
                result_math = n1 * n2
            elif operator == '/':
                if n2 > 0:
                    result_math = n1 / n2
                else:
                    error = "Error: Division by zero"
                    respond['error'] = error

            if result_math > 100:
                result_math *= 2
            elif result_math < 0:
                result_math += 50

            respond['result'] = result_math


            return render(request, 'resut.html', {'respond': respond})