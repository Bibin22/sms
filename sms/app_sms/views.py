from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import SMS
from .forms import CreateForm
from django.conf import settings
import requests

class Send_SMS(TemplateView):
    model = SMS
    template_name = 'app_sms/sms.html'
    form_class = CreateForm
    def get(self, request, *args, **kwargs):
        self.context = {
            'form':self.form_class
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = self.model.objects.last()

            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization": settings.AUTH_KEY,
                           "message": "Hi " + str(user.name) + " you have purchased " + str(user.item) + " on an amount of "  + str(user.price) + " Have a nice day",
                           "language": "english",
                           "route": "q",
                           "numbers": str(user.phone)}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            #print(response.text)


            return HttpResponse('SMS sent Successfully')
        else:
            return HttpResponse('Invalid Form')


