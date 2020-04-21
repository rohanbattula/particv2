import os

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from hello.forms import PartyForm
from hello.models import Party
from hello.serializer import PartySerializer

def index(request):
    party_list = Party.objects.order_by('-dateTime')
    serializer = PartySerializer(party_list, many=True)
    return JsonResponse(serializer.data, safe=False)

'''
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Party.home')
    else:
        form = UserCreationForm()
return render(request, 'accounts/signup.html'.{'form'.form})
'''

def party_new(request):
    form = PartyForm()

    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.createdBy = request.user
            party.save()
            return HttpResponse("success")
    else:
        form = PartyForm()
        return HttpResponse("success")


'''
def party_edit(request, pk):
    party = get_object_or_404(Party, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=party)
        if form.is_valid():
            party = form.save(commit=False)
            party.createdBy = request.user
            party.save()
            return redirect('party_screen', pk=party.pk)
    else:
        form = PostForm(instance=party)
    return render(request, 'blog/party_edit.html', {'form': form})


def party_detail(request, pk):
    party = get_object_or_404(Post, pk=pk)
    return render(request, 'party/party_detail.html', {'party': party})


def login(request):
    if request.method == 'POST'
    form = AuthenticationForm()
    if form.is_valid():
        string msg = email.message_from_string(data[0][1])
        string addr = email.utils.parseaddr(msg['From'])[1]
        domain = addr.split('@')[1]
        if domain == "ucla.edu" || domain == "g.ucla.edu":
            messages.success(request, f'Login successful!')
            return redirect('Party.home')
        else:
            messages.self.fail('Login unsuccessful')
        return render(request, 'Party.home', {'party': party})
'''
