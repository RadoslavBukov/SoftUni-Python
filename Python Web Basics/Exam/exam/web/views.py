from django.shortcuts import render, redirect

from exam_30_10_22.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from exam_30_10_22.web.models import Profile, Car


# Create your views here.
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    nav_without_user = False
    if profile is None:
        nav_without_user = True

    context = {
        'nav_without_user': nav_without_user,
    }
    return render(request, 'core/../../../../../servicebook/templates/core/index.html', context)


def catalogue(request):
    profile = get_profile()
    # if profile is None:
    #     return add_profile(request)
    cars_count = Car.objects.count()

    context = {
        'cars': Car.objects.all(),
        'cars_count': cars_count,
    }
    return render(request, 'catalogue/catalogue.html', context)



# Profile:
def create_profile(request):

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'nav_without_user': True,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = 0
    for car in cars:
        total_price += car.price
    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)


# Car:


def create_car(request):

    if request.method == "GET":
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'cars/car-create.html', context)


def detail_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'cars/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'cars/car-delete.html', context)
