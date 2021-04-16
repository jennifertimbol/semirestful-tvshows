from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages


def new(request):
    return render(request, "newshow.html")


def create(request):
    if request.method == "POST":
        errors = Show.objects.createnewshow_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release'],
                description=request.POST['desc']
            )

    return redirect(f"/shows/{show.id}")


def showinfo(request, tvshow_id):
    context = {
        'tvshow': Show.objects.get(id=tvshow_id)
    }

    return render(request, "id.html", context)


def display(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, "allshows.html", context)


def edit(request, tvshow_id):
    context = {
        'edit_show': Show.objects.get(id=tvshow_id)
    }

    return render(request, 'editshow.html', context)


def update(request, tvshow_id):
    errors = Show.objects.createnewshow_validator(request.POST)

    show_to_update = Show.objects.get(id=tvshow_id)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release']
    show_to_update.description = request.POST['desc']
    show_to_update.save()

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_to_update.id}/edit")
    else:
        return redirect(f"/shows/{show_to_update.id}")


def destroy(request, tvshow_id):
    show_to_delete = Show.objects.get(id=tvshow_id)
    show_to_delete.delete()

    return redirect('/shows')


def index(request):
    return redirect('/shows')
