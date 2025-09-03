from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegistrationForm, AppointmentForm
from .models import Appointment

def home(request):
	"""Home page view."""
	return render(request, 'medicare/home.html')

def about(request):
	"""About page view."""
	return render(request, 'medicare/about.html')

def services(request):
	"""Services page view."""
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			appointment = form.save(commit=False)
			if request.user.is_authenticated:
				appointment.user = request.user
			appointment.save()
			messages.success(request, 'Appointment booked successfully! We will contact you soon.')
			return redirect('medicare:services')
	else:
		form = AppointmentForm()
	
	return render(request, 'medicare/services.html', {'form': form})

def contact(request):
	"""Contact page view."""
	return render(request, 'medicare/contact.html')

def signup(request):
	"""User registration view."""
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Account created successfully! Please log in.')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	
	return render(request, 'medicare/signup.html', {'form': form})

@login_required
def dashboard(request):
	"""User dashboard view."""
	user_appointments = Appointment.objects.filter(user=request.user)
	return render(request, 'medicare/dashboard.html', {
		'appointments': user_appointments
	})

def book_appointment(request):
	"""Book appointment view."""
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			appointment = form.save(commit=False)
			if request.user.is_authenticated:
				appointment.user = request.user
			appointment.save()
			messages.success(request, 'Appointment booked successfully! We will contact you soon.')
			return redirect('medicare:services')
	else:
		form = AppointmentForm()
	
	return render(request, 'medicare/appointment.html', {'form': form})
