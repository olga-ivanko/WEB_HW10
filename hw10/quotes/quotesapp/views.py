from django.shortcuts import render, redirect
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote


# Create your views here.
def main(request):
    return render(request, "quotesapp/index.html")


def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/tag.html", {"form": form})

    return render(request, "quotesapp/tag.html", {"form": TagForm()})


def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotesapp:main")
        else:
            return render(request, "quotesapp/author.html", {"form": form})

    return render(request, "quotesapp/author.html", {"form": AuthorForm()})


def quote(request):
    tags = Tag.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

                return redirect(to="quotesapp.main")
        else:
            return render(
                request, "quotesapp/quote.html", {"tags": tags, "form": form}
            )

    return render(request, "quotesapp/quote.html", {"tags": tags, "form": QuoteForm()})
