from django.http import HttpResponse
from django.shortcuts import render
from .models import servicelist
from .models import serviceform
from django.shortcuts import redirect



# Create your views here.
def customer(request):
    return HttpResponse("this is customer page")



def servicerequest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_request_type=request.POST.get('dropdown')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        serviceformdata = serviceform(name=name, email=email, subject=subject,service_request_type=service_request_type, message=message)
        serviceformdata.save()

    servicelistdata = servicelist.objects.all()
    if servicelistdata.exists():
        first_servicelist = servicelistdata[0]
    else:
        first_servicelist = None
    context = {
        'servicelist': first_servicelist

    }
    return render(request, 'customer_portal/Service_Request.html', context)


def trackrequest(request):
    service_requests = serviceform.objects.all()
    print("service_requests :",service_requests)
    print("request.user :",str(request.user))
    if str(request.user) == 'admin':
        return render(request, 'customer_portal/Track_Request.html', {'service_requests': service_requests,"user": 'admin'})
    curr_user_service = []

    for service_request in service_requests:
        print("-------------")
        print("service_request :",service_request)
        print("curr_user_service :",curr_user_service)
        print("str(request.user) :",str(request.user))
        print("str(service_request.name) :",str(service_request.name))
        if str(request.user) == str(service_request.name):
            curr_user_service.append(service_request)
    print("curr_user_service last :",curr_user_service)
    return render(request, 'customer_portal/Track_Request.html', {'service_requests': curr_user_service })

def chooseoption(request):
    return render(request,'customer_portal/button.html')

def editservicerequest(request,entry_id):

    return redirect('ServiceRequest',entry_id=entry_id)