from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Contact, User, profile
from .forms import UserRegistrationForm, ProfileForm
from .serializers import BookSerializer

class HomeView(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_books'] = Book.objects.filter(is_visible=True)[:10]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('books:home')
        return self.get_context_data()

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(is_visible=True)

class MyProfileView(ListView):
    model = profile
    template_name = 'books/my_profile.html'
    context_object_name = 'profiles'
    def get_queryset(self):
        return profile.objects.all()

class profileView(TemplateView):
    template_name = 'books/add_profile.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form directly
            return redirect('books:home')  # Redirect to the home page
        else:
            # If the form is invalid, re-render the page with the form errors
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_visible=True)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserRegisterView(TemplateView):
    template_name = 'books/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserRegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('books:home')
        return self.render_to_response(self.get_context_data(form=form))