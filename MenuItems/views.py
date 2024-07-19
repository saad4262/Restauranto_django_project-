from django.shortcuts import render
from django.http import JsonResponse
from MenuItems.models import *
import json
from .models import dineIn

from django.shortcuts import render
from .models import Product, Order, Customer

def home_page(request):
    cartTotal = 0
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    product_messages = Product.objects.all()
    category = request.GET.get('category')
    search_query = request.GET.get('search')  # New: Get the search query from the request

    if category:
        product_messages = product_messages.filter(category=category)

    if search_query:  # New: Filter products by name if search query exists
        product_messages = product_messages.filter(product_name__icontains=search_query)

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'products': Product.objects.all(),
        'product_messages': product_messages,
        'category': category,
        'cartTotal': cartTotal,
    }
    
    return render(request, 'base1.html', context)

def cart_page(request):
    cartTotal = 0

    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
        # Using the corrected method
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'cartTotal': cartTotal}
    return render(request, 'cart.html', context)


from django.shortcuts import render
from django.http import JsonResponse
from MenuItems.models import *
import json
from django.db import transaction

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer, created = Customer.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    with transaction.atomic():
        # Fetch all order items with the same order and product
        order_items = OrderItem.objects.filter(order=order, product=product)

        if action == 'add':
            if order_items.exists():
                order_item = order_items.select_for_update().first()  # Lock the selected row for update
                order_item.quantity += 1
                order_item.save()
            else:
                order_item = OrderItem.objects.create(order=order, product=product, quantity=1)
        elif action == 'remove':
            if order_items.exists():
                order_item = order_items.select_for_update().first()  # Lock the selected row for update
                order_item.quantity -= 1
                order_item.save()
                if order_item.quantity <= 0:
                    order_item.delete()
        elif action == 'delete':
            order_items.delete()

    return JsonResponse("Item was updated", safe=False)

from django.shortcuts import render, redirect
from .models import Customer, Order, OrderItem, shipping_address
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from weasyprint import HTML


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from weasyprint import HTML

def send_checkout_receipt_email(information, order, items):
    context = {
        'information': information,
        'order': order,
        'items': items,
    }
    html_content = render_to_string('d-receipt.html', context)
    pdf_content = HTML(string=html_content).write_pdf()

    email = EmailMessage(
        'Order Receipt',
        'Thank you for your order. Please find attached your receipt.',
        'from@example.com',
        [information.email],
    )
    email.attach('receipt.pdf', pdf_content, 'application/pdf')
    email.send()


def checkout(request):
    information = None  # Initialize the variable to ensure it's always defined

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        province = request.POST.get('province')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        instruction = request.POST.get('instruction')

        information = shipping_address(name=name, email=email, number=number, address=address, city=city, zipcode=zipcode, province=province, instruction=instruction)
        information.save()

        if request.user.is_authenticated:
            customer, created = Customer.objects.get_or_create(user=request.user)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items

            # Send receipt email
            send_checkout_receipt_email(information, order, items)

            # Redirect to a success page
            return redirect('checkout_success')
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']
            # Send receipt email
            send_checkout_receipt_email(information, order, items)

            request.session['information_id'] = information.id

            # Redirect to a success page
            return redirect('success')

    else:
        if request.user.is_authenticated:
            customer, created = Customer.objects.get_or_create(user=request.user)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'information': information}
    return render(request, 'checkout.html', context)


from django.shortcuts import render
from .models import Customer, Order, OrderItem, shipping_address

def checkout_success(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']


    information_id = request.session.get('information_id')
    information = shipping_address.objects.get(id=information_id) if information_id else None

    context = {
        'information': information,

        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'd-success.html', context)


from django.shortcuts import render, redirect
from .models import dineIn, Customer, Order
from .forms import DineInForm



from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import dineIn, Customer, Order
from .forms import DineInForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import BookingForm
# from .models import Booking
from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from weasyprint import HTML  # type: ignore



from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import dineIn, Customer, Order
from .forms import DineInForm
from weasyprint import HTML

def dine_in(request):
    if request.method == 'POST':
        form = DineInForm(request.POST)
        if form.is_valid():
            dine_in_instance = form.save()
            # Get total price
            # total_price = dine_in_instance.total_price
            # Send receipt email
            send_receipt_email(dine_in_instance)
            # Redirect to a success page
            return redirect('success')  # Redirect to a success page after saving
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = DineInForm()

    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'form': form, 'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'tableForm.html', context)

def send_receipt_email(dine_in_instance):
    
    
    context = {
        'dine_in_instance': dine_in_instance,
        # 'total_price': total_price
    }
    html_content = render_to_string('receipt.html', context)
    pdf_content = HTML(string=html_content).write_pdf()

    email = EmailMessage(
        'Booking Receipt',
        'Thank you for your booking. Please find attached your receipt.',
        'from@example.com',
        [dine_in_instance.email],
    )
    email.attach('receipt.pdf', pdf_content, 'application/pdf')
    email.send()


def success(request):

    # Retrieve dine_in_instance_id from session
    dine_in_instance_id = request.session.get('dine_in_instance_id')
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    try:
        # Get dineIn instance using the dine_in_instance_id
        dine_in_instance = dineIn.objects.get(id=dine_in_instance_id)
    except dineIn.DoesNotExist:
        # Handle case where dineIn instance does not exist
        dine_in_instance = None

    context = {'dine_in_instance': dine_in_instance, 'items': items, 'order': order, 'cartItems': cartItems}
    return render(request,'success.html', context)
