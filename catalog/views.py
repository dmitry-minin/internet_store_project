from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        return render(request, 'confirm.html', {'name': name})
    return render(request, 'contacts.html')
