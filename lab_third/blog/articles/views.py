from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
    return render(request, 'archive.html', {'posts': Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):
    # Проверяем, авторизован ли пользователь
    if request.user.is_anonymous:
        raise Http404("Вы должны быть авторизованы, чтобы создавать статьи.")

    # Если пользователь отправил форму
    if request.method == "POST":
        form = {
            'title': request.POST.get("title", "").strip(),
            'text': request.POST.get("text", "").strip()
        }

        # Проверка: заполнены ли поля
        if not form["title"] or not form["text"]:
            form['errors'] = "Пожалуйста, заполните все поля."
            return render(request, 'create_post.html', {'form': form})

        # Проверка: уникальность названия
        if Article.objects.filter(title=form["title"]).exists():
            form['errors'] = "Статья с таким названием уже существует."
            return render(request, 'create_post.html', {'form': form})

        # Создаём статью
        article = Article.objects.create(
            title=form["title"],
            text=form["text"],
            author=request.user
        )

        # Перенаправляем на страницу созданной статьи
        return redirect('get_article', article_id=article.id)

    # Если метод GET — просто показать пустую форму
    return render(request, 'create_post.html', {})

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            return render(request, "register.html", {"error": "Все поля обязательны!"})

        try:
            User.objects.get(username=username)
            return render(request, "register.html", {"error": "Такой пользователь уже существует"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect("archive")
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("archive")
        else:
            return render(request, "login.html", {"error": "Неверный логин или пароль"})
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("archive")