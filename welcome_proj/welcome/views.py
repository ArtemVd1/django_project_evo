from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User


def welcome_form(request):
    if request.method == "POST":
        if request.POST.get('hello_button') is not None:
            errors = {}
            data = {}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            if not errors:
                if User.objects.all().filter(first_name=data['first_name'], last_name=data['last_name']):
                    message = f'Вже бачились, {data["first_name"]}!'
                else:
                    user = User(**data)
                    user.save()
                    message = f'Привіт, {data["first_name"]} {data["last_name"]}!'

                return HttpResponseRedirect(f"{reverse('welcome_form')}?status_message={message}")

            else:
                return render(request, 'form.html', {'errors': errors})

        elif request.POST.get('quests_button') is not None:
            return HttpResponseRedirect(reverse('welcome_list'))

    else:
        return render(request, 'form.html', {})


def welcome_list(request):
    users = User.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by == '':
        users = users.order_by('first_name')
    if order_by in ('last_name', 'first_name'):
        users = users.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            users = users.reverse()

    # paginate students
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'welcome_list.html', {'users': users})
