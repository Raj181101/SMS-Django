from django.shortcuts import render,redirect
from django.http import HttpResponse
from Birthday.forms import UserRegisterForm
from Birthday.models import Birth
from django.contrib import messages
import datetime
import requests
import json
# Create your views here.

def birth(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user')
            birthday = form.cleaned_data.get('birthday')
            mobile = form.cleaned_data.get('phone_number')
        #     print("====",username,birthday,mobile)
            x=Birth.objects.all().values('user','birthday','phone_number')
            for y in x:
                # print("++++",y['user'],y['birthday'],y['phone_number'])
                if(y['user'] == username and y['birthday'] == birthday and y['phone_number'] == mobile):
                    messages.warning(request, f'Already User Details Exist! Change Details')
                    break
            else:
                form.save()
                return render(request,'thanq.html',{'form':username})
    return render(request,'birthday.html',{'form':form})


def date():
        dates = Birth.objects.all().values('user','birthday','phone_number') 
        today = datetime.datetime.now()
        today_month = today.month
        today_day = today.day
        # print(today_day,today_month)
        details = {}
        for date in dates:
                if date['birthday'] is not None:
                        month=date['birthday'].month
                        day=date['birthday'].day
                        if(today_day == day and today_month == month):
                                # print("---Both Dates and Month are Matched---",date['user'],date['phone_number'])
                                details[date['user']]=date['phone_number']
                        
                                ##### SMS Sending Starts Here #####
                                URL = 'https://www.way2sms.com/api/v1/sendCampaign'
                                def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
                                        req_params = {
                                                'apikey':apiKey,
                                                'secret':secretKey,
                                                'usetype':useType,
                                                'phone': phoneNo,
                                                'message':textMessage,
                                                'senderid':senderId
                                        }
                                        return requests.post(reqUrl, req_params)

                                name = date['user']
                                msg = "Hello Dear Friend {} \n \tWish You Many More Happy Returns Of The Day\n \tIam Wishing All Your Dreams Comes True \n\n Regards \n Raja".format(name)
                                mobile = date['phone_number']
                                response = sendPostRequest(URL, 'api_key', 'api_secure', 'stage',mobile, '', msg )
                                #print(response.text) 
        
        name = 'ur name'
        mobile = 'ur number' 
        msg1 = "Hi Raja Today Birthday Guys are \n\t Names : {0}  \n\t Mobile Numbers : {1}".format(list(details.keys()),list(details.values()))
        response = sendPostRequest(URL, 'api_key', 'api_secure', 'stage',mobile, '', msg1 )

# date()
