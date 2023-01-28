from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Note
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from .forms import MyUserCreationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    page_id = 'home'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if (q.lower() == 'all'):
        notes = Note.objects.all()
    else:
        notes = Note.objects.filter(
            Q(name__icontains=q) |
            Q(note__icontains=q) |
            Q(tag1__icontains=q) |
            Q(tag2__icontains=q) |
            Q(tag3__icontains=q)
        )
    if request.method == "POST":
        user_update = User.objects.get(
            email=request.user.email
        )
        if request.FILES.get('image') == None:
            username =request.POST['modal_username']
            if username == '':
                username = 'user'
                user_update.username = username
            else:
                user_update.username = username
            user_update.save()
            print(username)
            return redirect('home')
            
        elif request.FILES.get('image') != None:
            username =request.POST['modal_username']
            if username == '':
                username = 'user'
                user_update.username = username
                
            else:
                user_update.username = username
            avatar = request.FILES['image']
            user_update.avatar = avatar
            user_update.save()
            return redirect('home')
            
    return render(request, 'index.html', {
        'notes':notes,
        'pg_id':page_id,
    })

@login_required(login_url='login')
def createNote(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST['note_name']
        tag1 = request.POST['tag_1']
        tag2 = request.POST['tag_2']
        tag3 = request.POST['tag_3']
        note_content = request.POST['note_content']
        print(current_user)
        if name != '':
            note = Note.objects.create(
                owner=current_user,
                name=name,
                tag1=tag1,
                tag2=tag2,
                tag3=tag3,
                note=note_content
            )
            return redirect('home')
        else:
            messages.info(
                request, "Add a name to note"
            )
    return render(request, 'create.html', {
            
        })
    
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=email)
        except:
            messages.error(
                request, "User doesn't exist!"
            )
        user = authenticate(
            request,
            username=email,
            password=password,
        )
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request,
                'invalid username or password'
            )
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
  
def userEmailCheck_error(user_mail):
    for i in User.objects.all():
        if str(i.email) == user_mail:
            return True
        else:
            return False
  
def registerUser(request):
    if request.user.is_authenticated:
        logout(request)

    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(
                "something is wrong with me and i don't know what haha that's coding for you!"
            )
    # TODO: CATCH USER ERRORS DURING REGISTERATION!
    return render(request, 'register.html', {
        'form':form
    })
    
def detailed(request, pk):
    notes = Note.objects.get(unique_note_identity=pk)
    return render(request, 'detailed.html', {
        'notes':notes
    })
    
def deleteNote(request, pk):
    notes = Note.objects.get(unique_note_identity=pk).delete()
    return redirect('home')
    
def updateNote(request, pk):
    note_obj = Note.objects.get(unique_note_identity=pk)
    if request.method == "POST":
        note_name = request.POST['note_name']
        tag_1 = request.POST['tag_1']
        tag_2 = request.POST['tag_2']
        tag_3 = request.POST['tag_3']
        note_content = request.POST['note_content']
        # updating data
        if note_name != '':
            note_obj.name = note_name
            note_obj.tag1 = tag_1
            note_obj.tag2 = tag_2
            note_obj.tag3 = tag_3
            note_obj.note = note_content
            note_obj.save()
            return redirect('home')
        else:
            messages.error(
                request,
                'Note Name can\'t be empty'
            )
        
    return render(request, 'update.html', {
        'note':note_obj
    })