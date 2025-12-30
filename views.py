from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserForm, MhpForm
from .models import Mhp  # import the model (important!)

# --- User Registration ---
def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'form.html', {'vv': form})


# --- Success Page ---
def success(request):
    return render(request, 'success.html')


# --- Login Page ---
def login_view(request):
    return render(request, 'login.html')


# --- Home Page ---
def home(request):
    return render(request, 'home.html')

def item(request):
    return render(request,'item.html')

def pro1(request):
    return render(request,'boat_realbeat.html')

def pro2(request):
    return render(request,'marshall.html')

def pro3(request):
    return render(request,'redmi_headband.html')

def pro4(request):
    return render(request,'y1_quadmic.html')



# --- Create Order (MHP) ---
def create_order(request):   # renamed from mhp_form to avoid confusion
    if request.method == 'POST':
        form = MhpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MhpForm()
    return render(request, 'order_form.html', {'vv': form})


# --- Order List Page ---
def order_list(request):
    orders = Mhp.objects.all().order_by('-id')  # query the Mhp model (not the form)
    return render(request, 'order_list.html', {'orders': orders})

# --- Update Order ---
def update_order(request, id):
    order = get_object_or_404(Mhp, id=id)
    form = MhpForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')  # redirect to order list after update
    return render(request, 'order_update.html', {'form': form, 'order': order})


# --- Delete Order ---
def delete_order(request, id):
    order = get_object_or_404(Mhp, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})