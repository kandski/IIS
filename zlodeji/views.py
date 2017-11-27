from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count

from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    template_name = 'zlodeji/index2.html'

    def get_queryset(self):
        return Zlocin.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['urobil'] = Urobil.objects.all()
        context['all_zlocin'] = Zlocin.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['eviduje'] = Eviduje.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        return context


class ZlodejsView(generic.ListView):
    template_name = 'zlodeji/zlodejs.html'
    context_object_name = 'all_zlodejs'

    def get_queryset(self):
        return Zlodej.objects.all()


class DetailView(generic.DetailView):
    model = Zlocin
    template_name = 'zlodeji/detail.html'
    queryset = Zlocin.objects.all()

    # @login_required(login_url='zlodeji/login.html')
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['urobil'] = Urobil.objects.all()
        context['test'] = Zlocin.objects.all()
        return context


class ZlodejCreate(LoginRequiredMixin, CreateView):
    model = Zlodej
    fields = ['prezivka', 'meno', 'rc', 'zivy', 'odmena', 'fotka']


class ZlodejUpdate(LoginRequiredMixin, UpdateView):
    model = Zlodej
    fields = ['prezivka', 'meno', 'rc', 'zivy', 'odmena', 'fotka']


class ZlodejDelete(LoginRequiredMixin, DeleteView):
    model = Zlodej
    success_url = reverse_lazy('zlodej:index')


class ZlocinCreate(LoginRequiredMixin, CreateView):
    model = Zlocin
    fields = ['hodnota_korist', 'uspech', 'id_typu_zlocinu']


class SkolenieCreate(LoginRequiredMixin, CreateView):
    model = Skolenie
    fields = ['level_skoleni', 'schvalene', 'poznamky']


class SkolenieUpdate(LoginRequiredMixin, UpdateView):
    model = Skolenie
    fields = ['level_skoleni', 'schvalene', 'poznamky']

class VybavenieCreate(LoginRequiredMixin, CreateView):
    model = Vybavenie
    fields = ['meno', 'id_typu_vybavenia']


class VybavenieUpdate(LoginRequiredMixin, UpdateView):
    model = Vybavenie
    fields = ['meno', 'id_typu_vybavenia']


class ZlocinUpdate(LoginRequiredMixin, UpdateView):
    model = Zlocin
    fields = ['hodnota_korist', 'uspech', 'id_typu_zlocinu']


class ZlocinDelete(LoginRequiredMixin, DeleteView):
    model = Zlocin
    success_url = reverse_lazy('zlodej:index')


class BolnaCreate(LoginRequiredMixin, CreateView):
    model = BolNa
    fields = ['id_skolenia', 'prezivka']


class BolnaUpdate(LoginRequiredMixin, UpdateView):
    model = BolNa
    fields = ['id_skolenia', 'prezivka']


class UrobilCreate(LoginRequiredMixin, CreateView):
    model = Urobil
    fields = ['id_zlocinu', 'prezivka']


class UrobilUpdate(LoginRequiredMixin, UpdateView):
    model = Urobil
    fields = ['id_zlocinu', 'prezivka']

class Skolenia(generic.ListView):
    template_name = 'zlodeji/skolenia.html'

    def get_queryset(self):
        return BolNa.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Skolenia, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['sk_zlocinu_count'] = SkolenieZlocinu.objects.count()
        context['sk_zlocinu'] = SkolenieZlocinu.objects.all()
        context['sk_vybavenia_count'] = SkolenieVybavenia.objects.count()
        context['sk_vybavenia'] = SkolenieVybavenia.objects.all()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['eviduje'] = Eviduje.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        return context


class RegisterView(View):
    form_class = UserForm
    template_name = 'zlodeji/registration_form.html'

    # display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('zlodej:index')

        return render(request, self.template_name, {'form': form})


class LogInView(View):
    form_class = LoginForm
    template_name = 'zlodeji/login_form.html'

    # display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(None)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('zlodej:index')

        return render(request, self.template_name, {'form': form})


class LogOutView(LoginRequiredMixin, View):

    # process form data
    def get(self, request):
        logout(request)
        return redirect('zlodej:index')


class SkolenieApprove(LoginRequiredMixin, UpdateView):
    model = Skolenie
    fields = ['schvalene']
    success_url = reverse_lazy('zlodej:skolenia')



class Statistics(generic.ListView):
    template_name = 'zlodeji/stat.html'

    def get_queryset(self):
        return Urobil.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Statistics, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['eviduje'] = Eviduje.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        return context


class VybavenieView(generic.ListView):
    template_name = 'zlodeji/vybavenie.html'

    def get_queryset(self):
        return Vlastnil.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VybavenieView, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        context['typ_vybavenia'] = TypVybavenia.objects.all()
        return context