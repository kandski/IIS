
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


class IndexView(generic.ListView):
    template_name = 'zlodeji/index.html'

    def get_queryset(self):
        return Zlocin.objects.all()

    def list_of_korist(self, request):
        username = request.user.username
        return username

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['urobil'] = Urobil.objects.all()
        context['all_zlocin'] = Zlocin.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['eviduje'] = Eviduje.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        context['all_vydriduch'] = Vydriduch.objects.all()
        context['all_lupeznik'] = Lupeznik.objects.all()
        return context


class DetailView(generic.ListView):
    model = Zlocin
    template_name = 'zlodeji/detail.html'
    queryset = Zlocin.objects.all()

    # @login_required(login_url='zlodeji/login.html')
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['dostal_unique'] = Dostal.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['typ_vybavenia'] = TypVybavenia.objects.all()
        return context


class ZlodejCreate(LoginRequiredMixin, CreateView):
    template_name = 'zlodeji/registration_form.html'
    model = Zlodej
    fields = ['username','email', 'prezivka','meno', 'password', 'odmena',
                  'rc', 'fotka', 'zivy']


class ZlodejUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'zlodeji/zlodej_form.html'
    model = Zlodej
    fields = ['email','meno', 'odmena', 'rc', 'fotka', 'zivy']
    success_message = u"Uživateľ bol úspešne upravený."


class ZlodejDelete(LoginRequiredMixin, DeleteView):
    model = Zlodej
    success_url = reverse_lazy('zlodej:index')


class ZlocinCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Zlocin
    fields = ['hodnota_korist', 'uspech', 'id_typu_zlocinu']
    success_message = u"Záznam zločinu bol úspešne vytvorený."


class SkolenieCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Skolenie
    fields = ['level_skoleni', 'schvalene', 'poznamky']
    success_message = u"Záznam školenia bol úspešne vytvorený."


class SkolenieUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Skolenie
    fields = ['level_skoleni', 'schvalene', 'poznamky']
    success_message = u"Záznam školenia bol úspešne vytvorený."


class VybavenieCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Vybavenie
    fields = ['meno', 'id_typu_vybavenia']
    success_message = u"Záznam bol úspešne vytvorený."


class VybavenieUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Vybavenie
    fields = ['meno', 'id_typu_vybavenia']
    success_message = u"Záznam bol úspešne vytvorený."


class ZlocinUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Zlocin
    fields = ['hodnota_korist', 'uspech', 'id_typu_zlocinu']
    success_message = u"Záznam bol úspešne vytvorený."


class ZlocinDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Zlocin
    success_message = u"Záznam bol úspešne odstránený."
    success_url = reverse_lazy('zlodej:index')

class UrobilDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Urobil
    success_message = u"Záznam bol úspešne odstránený."
    success_url = reverse_lazy('zlodej:index')


class BolnaCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = BolNa
    fields = ['id_skolenia', 'prezivka']
    success_message = u"Záznam bol úspešne vytvorený."



class BolnaUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = BolNa
    fields = ['id_skolenia', 'prezivka']
    success_message = u"Záznam bol úspešne upravený."


class UrobilCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Urobil
    fields = ['id_zlocinu', 'prezivka']
    success_message = u"Záznam bol úspešne vytvorený."



class UrobilUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Urobil
    fields = ['id_zlocinu', 'prezivka']
    success_message = u"Záznam bol úspešne upravený."


class VlastnilCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = VlastnilForm
    template_name = 'zlodeji/vlastnil_form.html'
    success_message = u"Záznam bol úspešne vytvorený."


class VlastnilUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = VlastnilForm
    template_name = 'zlodeji/vlastnil_form.html'
    success_message = u"Záznam bol úspešne upravený."



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
        form = self.form_class(initial={'odmena': '0',})
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
                    messages.success(request, u"Vitaj " + username + "!")
                    return redirect('zlodej:index')

        return render(request, self.template_name, {'form': form})


class LogInView(SuccessMessageMixin, View):
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
                messages.success(request, u"Vitaj späť " + username + "!")
                return redirect('zlodej:index')
        return render(request, self.template_name, {'form': form})


class LogOutView(LoginRequiredMixin, View):

    # process form data
    def get(self, request):
        logout(request)
        messages.success(request, u"Odhlásenie prebehlo úspešne!")
        return redirect('zlodej:index')


class SkolenieApprove(LoginRequiredMixin, UpdateView):
    model = Skolenie
    fields = ['schvalene']
    success_url = reverse_lazy('zlodej:skolenia')


class User_Super(LoginRequiredMixin, UpdateView):
    model = Zlodej
    fields = ['is_superuser', 'is_staff']
    success_url = reverse_lazy('zlodej:index')


class User_Staff(LoginRequiredMixin, UpdateView):
    model = Zlodej
    fields = ['is_staff']
    success_url = reverse_lazy('zlodej:index')


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
        context['povolenia_count'] = Dostal.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['dostal_unique'] = Dostal.objects.values('prezivka').distinct()
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


class Povolenia(generic.ListView):
    template_name = 'zlodeji/povolenia.html'

    def get_queryset(self):
        return Dostal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Povolenia, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['dostal_unique'] = Dostal.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['typ_vybavenia'] = TypVybavenia.objects.all()
        return context


class RajonCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Rajon
    fields = ['nazov_rajonu', 'sirka', 'dlzka', 'pocet_obyvatelov', 'kapacita_zlodejov', 'bohatstvo', 'level_rajonu']
    success_message = u"Záznam bol úspešne vytvorený."



class RajonDetail(LoginRequiredMixin, generic.ListView):
    template_name = 'zlodeji/detail.html'
    model = Eviduje

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kwargs = None

    def get_queryset(self):
        return Eviduje.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RajonDetail, self).get_context_data(**kwargs)
        context['all_zlodejs'] = Zlodej.objects.all()
        context['zlodej_count'] = Zlodej.objects.count()
        context['zlocin_count'] = Urobil.objects.count()
        context['skolenie_count'] = BolNa.objects.count()
        context['vybavenie_count'] = Vlastnil.objects.count()
        context['urobil'] = Urobil.objects.all()
        context['eviduje'] = Eviduje.objects.all()
        context['urobil_unique'] = Urobil.objects.values('prezivka').distinct()
        context['bolna_unique'] = BolNa.objects.values('prezivka').distinct()
        context['vlastnil_unique'] = Vlastnil.objects.values('prezivka').distinct()
        context['dostal_unique'] = Dostal.objects.values('prezivka').distinct()
        context['all_zlocin'] = Zlocin.objects.all()
        context['vlastnil'] = Vlastnil.objects.all()
        context['bolna'] = BolNa.objects.all()
        context['dostal'] = Dostal.objects.all()
        context['typ_vybavenia'] = TypVybavenia.objects.all()
        context['stranka'] = self.kwargs['pk']
        context['uziv'] = Eviduje.objects.get(pk=context['stranka'])
        return context


class EvidujeCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'zlodeji/rajon_form.html'
    model = Eviduje
    fields = ['prezivka', 'nazov_rajonu']
    success_message = u"Záznam bol úspešne vytvorený."
    #success_url = reverse_lazy('zlodej:eviduje-add')


class EvidujeAssign(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = EvidujeForm
    template_name = 'zlodeji/rajon_assign.html'
    success_message = u"Záznam bol úspešne vytvorený."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def get_initial(self):
        self.initial.update({'prezivka': self.request.user})
        return self.initial
    # success_url = reverse_lazy('zlodej:eviduje-assign')


class BolNaCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = BolNa
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."


class BolNaUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = BolNa
    fields = '__all__'
    success_message = u"Záznam bol úspešne upravený."


class BolNaDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = BolNa
    fields = '__all__'
    success_message = u"Záznam bol úspešne vymazaný."
    success_url = reverse_lazy('zlodej:skolenia')


class SkolenieZlocinuCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = SkolenieZlocinu
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."


class SkolenieVybaveniaCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = SkolenieVybavenia
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."

class DostalCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Dostal
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."

class PovolenieCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Povolenie
    fields = ['doba_platnosti', 'nazov_rajonu', 'id_zlocinu']
    success_message = u"Záznam bol úspešne vytvorený."

class VydriduchCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Vydriduch
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."


class LupeznikCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lupeznik
    fields = '__all__'
    success_message = u"Záznam bol úspešne vytvorený."


class DostalDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Dostal
    fields = '__all__'
    success_message = u"Záznam bol úspešne vymazaný."
    success_url = reverse_lazy('zlodej:povolenia')

class EvidujeDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Eviduje
    fields = '__all__'
    success_message = u"Záznam bol úspešne vymazaný."
    success_url = reverse_lazy('zlodej:index')


class VlastnilDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Vlastnil
    fields = '__all__'
    success_message = u"Záznam bol úspešne vymazaný."
    success_url = reverse_lazy('zlodej:index')


class VlastnilCreatezlodej(SuccessMessageMixin, CreateView):
    form_class = VlastnilFormzlodej
    template_name = 'zlodeji/vlastnil_form.html'
    success_message = u"Záznam bol úspešne vytvorený."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None

    def get_initial(self):
        self.initial.update({'prezivka': self.request.user})
        return self.initial
    # success_url = reverse_lazy('zlodej:eviduje-assign')