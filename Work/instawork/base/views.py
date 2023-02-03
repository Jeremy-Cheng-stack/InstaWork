from django.shortcuts import render, redirect
from .models import Member
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import MemberForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_team_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            team_member = form.save()
            team_member.save()
            return redirect('team_member_list')


def addpage(request):
    return render(request, 'addpage.html')


def editpage(request):
    return render(request, 'editpage.html')


class TeamMemberListView(ListView):
    model = Member
    template_name = 'Home.html'
    context_object_name = 'team_members'


class TeamMemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'Addpage.html'

    def form_valid(self, form):
        form.save()
        return redirect('team_member_list')


class TeamMemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'Editpage.html'

    def form_valid(self, form):
        form.save()
        return redirect('team_member_list')


class TeamMemberDeleteView(DeleteView):
    model = Member
    form_class = MemberForm
    template_name = 'Deletepage.html'

    def form_valid(self, form):
        form.save()
        return redirect('team_member_list')
