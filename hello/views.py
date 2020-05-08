import os
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from hello.models import Party
from hello.serializer import PartySerializer
from rest_framework.parsers import JSONParser



@csrf_exempt
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

@csrf_exempt
@api_view(['GET', 'POST'])
def party_new(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Party.objects.all()
        serializer = PartySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
