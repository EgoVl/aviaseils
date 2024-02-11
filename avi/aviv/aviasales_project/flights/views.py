from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Ticket


def index(request):
    registration_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'flights/index.html', {'registration_form': registration_form, 'login_form': login_form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'flights/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'flights/login.html', {'login_form': login_form})

def home(request):
    tickets = Ticket.objects.all()
    return render(request, 'flights/home.html', {'tickets': tickets})

def buy_ticket(request, ticket_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        ticket = Ticket.objects.get(id=ticket_id)
        total_price = ticket.price * quantity
        return redirect('home')

def hotel_search(request):
    return render(request, 'flights/hotel_search.html')

def search_tickets(request):
    if request.method == 'GET':
        origin = request.GET.get('origin', '')
        destination = request.GET.get('destination', '')
        departure_date = request.GET.get('departure_date', '')
        return_date = request.GET.get('return_date', '')

        tickets = Ticket.objects.filter(origin=origin, destination=destination, departure_date=departure_date, return_date=return_date)

        context = {
            'tickets': tickets,
            'origin': origin,
            'destination': destination,
            'departure_date': departure_date,
            'return_date': return_date
        }

        return render(request, 'tickets.html', context)

