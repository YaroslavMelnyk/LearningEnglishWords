from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .forms import SingUpForm, LoginForm


#class SignUpView(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'registration/signup.html'
#    context_object_name = 'user'


class SignUpView(CreateView):
    form_class = SingUpForm
    template_name = 'registration/signup.html'


    def get_success_url(self):
        return reverse_lazy('home')


class LoginVue(LoginView):
    form_class = LoginForm
    #redirect_authenticated_user = True
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

#def logout_view(request):
#    logout(request)


def profile(request):
    return render(request, 'registration/profile.html')

    def get_success_url(self):
        return reverse_lazy('home')


    def form_invalid(self, form):
        messages.error(self.request, 'Invalid  login and password')
        return self.render_to_response(self.get_context_data(form=form))





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]