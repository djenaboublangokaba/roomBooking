from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, BookingForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from locationblango.models import Booking, Room
from django.contrib import messages
from datetime import datetime
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator


# Create your views here.
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created successfully'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html',{'form':form, 'msg':msg})



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')

            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')

            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')

            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validation form'


    return render(request, 'accounts/login_view.html', {'form':form, 'msg':msg})


@login_required
def booking(request):
    user = request.user
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            duplicate_booking = Booking.objects.filter(check_in=booking.check_in, check_out=booking.check_out, room=booking.room)
            if duplicate_booking.exists():
                messages.success(request, 'This room is already booked try another or change date')

            else:

                booking.user = user
                booking.save()

                messages.success(request, 'Successfuly booked')
                return render(request, 'accounts/success_page.html', {'booking':booking})

    else:
        form=BookingForm()

    context={'form':form}

    return render(request, 'accounts/new_booking.html',context)


@login_required
def booking_update(request, pk):
    user=request.user
    booking = Booking.objects.get(pk=pk)

    if booking.user == request.user:
        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                booking=form.save(commit=False)
                booking.user = user
                booking.save()

                messages.success(request, 'Success')
                return redirect('booking-list')

        else:
            form=BookingForm(instance=booking)

    else:
        raise Http404

    context={'form':form}

    return render(request, 'accounts/booking-update.html',context)




@login_required
def delete_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.delete()
    messages.success(request, 'The booking is successfuly delete')

    return redirect('booking-list')


    return render(request, 'accounts/delete-booking.html',context={'booking':booking})




def booking_list(request):

    if 'search' in request.GET:
        search = request.GET.get('search')
        booking_list = Booking.objects.all()
    else:
        
        booking_list = Booking.objects.all()


    paginator = Paginator(booking_list, 10)
    page = request.GET.get('page')
    try:
        bookings = paginator.get_page(page)
    except Exception:
        bookings = paginator.page(1)
    

    context={'bookings':bookings}
    return render(request, 'accounts/booking-list.html',context)




def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    context={'booking':booking}
    return render(request, 'accounts/booking-detail.html', context)


def admin_page(request):
    return render(request, 'accounts/admin.html')


def employee_page(request):
    return render(request, 'accounts/employee.html')


def customer_page(request):
    return render(request, 'accounts/customer.html')
