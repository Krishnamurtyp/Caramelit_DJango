from django.shortcuts import render
from django.core.mail import send_mail

# Defining ticket numbers for contact forms
service_ticket = 1
consortium_ticket = 1
academy_ticket = 1

# Static Home pages
def index(request):
    return render(request, 'staticHome/index.html')

def aboutus(request):
    return render(request, 'staticHome/aboutus.html')

def consortium(request):
    return render(request, 'staticHome/consortium.html')

def academy(request):
    return render(request, 'staticHome/academy.html')

def products(request):
    return render(request, 'staticHome/products.html')

# Industries related pages
def automotive(request):
    return render(request, 'staticHome/industries/automotive.html')
def program(request):
    return render(request, 'staticHome/program.html')

def communication(request):
    return render(request, 'staticHome/industries/communication.html')

def lifescience(request):
    return render(request, 'staticHome/industries/lifescience.html')

def banking(request):
    return render(request, 'staticHome/industries/banking.html')

def consumer(request):
    return render(request, 'staticHome/industries/consumer.html')

def travel(request):
    return render(request, 'staticHome/industries/travel.html')

# Insights related pages
def artificial(request):
    return render(request, 'staticHome/insights/artificial.html')

def blockchain(request):
    return render(request, 'staticHome/insights/blockchain.html')

def iot(request):
    return render(request, 'staticHome/insights/iot.html')

def futureworkforce(request):
    return render(request, 'staticHome/insights/futureworkforce.html')

def cloudcomputing(request):
    return render(request, 'staticHome/insights/cloudcomputing.html')

def datascience(request):
    return render(request, 'staticHome/insights/datascience.html')

# Business related pages
def strategy(request):
    return render(request, 'staticHome/business/strategy.html')

def consulting(request):
    return render(request, 'staticHome/business/consulting.html')

def digital(request):
    return render(request, 'staticHome/business/digital.html')

def technology(request):
    return render(request, 'staticHome/business/technology.html')

def operations(request):
    return render(request, 'staticHome/business/operations.html')

def Application(request):
    return render(request, 'staticHome/business/Application.html')

def program(request):
    return render(request, 'staticHome/program.html')

# Contact forms
def contactform(request):
    global service_ticket
    if request.method == 'POST':
        try:
            full_name = request.POST.get('fname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pincode = request.POST.get('pincode')
            budget = request.POST.get('budget')
            service = request.POST.get('service')
            country = request.POST.get('country')
            msg = "Name: " + full_name + '\n' + "Email: " + email + '\n' + "Phone: " + phone + '\n' + "Budget: " + budget + '\n' + "Service: " + service + '\n' + "Country: " + country + '\n'
            send_mail('IT Services Ticket #' + str(service_ticket), msg, 'Madarauchiha3524@gmail.com', ['Vinesh.katewa@gmail.com'], fail_silently=False,)
            service_ticket += 1
            return render(request, 'staticHome/contactform.html', {'error': 0})
        except Exception as e:
            return render(request, 'staticHome/contactform.html', {'error': 1})        
    return render(request, 'staticHome/contactform.html')

def academycontact(request):
    global academy_ticket
    if request.method == 'POST':
        try:
            full_name = request.POST.get('fname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pincode = request.POST.get('pincode')
            subcategory = request.POST.get('subcategory')
            category = request.POST.get('category')
            country = request.POST.get('country')
            msg = "Name: " + full_name + '\n' + "Email: " + email + '\n' + "Phone: " + phone + '\n' + "Subcategory: " + subcategory + '\n' + "Category: " + category + '\n' + "Country: " + country + '\n'
            send_mail('IT Academy Ticket #' + str(academy_ticket), msg, 'Madarauchiha3524@gmail.com', ['Vinesh.katewa@gmail.com'], fail_silently=False,)
            academy_ticket += 1
            return render(request, 'staticHome/academycontact.html', {'error': 0})
        except Exception as e:
            return render(request, 'staticHome/academycontact.html', {'error': 1})
    return render(request, 'staticHome/academycontact.html')

def consortiumcontact(request):
    global consortium_ticket
    if request.method == 'POST':
        try:
            full_name = request.POST.get('fname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pincode = request.POST.get('pincode')
            subcategory = request.POST.get('subcategory')
            category = request.POST.get('category')
            country = request.POST.get('country')
            msg = "Name: " + full_name + '\n' + "Email: " + email + '\n' + "Phone: " + phone + '\n' + "Subcategory: " + subcategory + '\n' + "Category: " + category + '\n' + "Country: " + country + '\n'
            send_mail('IT Consortium Ticket #' + str(consortium_ticket), msg, 'Madarauchiha3524@gmail.com', ['Vinesh.katewa@gmail.com'], fail_silently=False,)
            consortium_ticket += 1
            return render(request, 'staticHome/consortiumcontact.html', {'error': 0})
        except Exception as e:
            return render(request, 'staticHome/consortiumcontact.html', {'error': 1})
    return render(request, 'staticHome/consortiumcontact.html')