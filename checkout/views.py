from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from project.models import Projects
import stripe

# Create your views here.

stripe.api_key = setting.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=='POST':
        oreder_form = MakePaymentForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quality in cart.items():
                project = get_object_or_404(Projects, pk=id)
                total += quantity * project.price
                order_line_item = OrderLineItem(
                    order = order,
                    project = project,
                    quantity = quality
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except strope.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('projects'))
            else:
                messages.error(request, "Unable to make pyment")
        else:
            print(payment_form.error)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        oreder_form = OrderForm()

    return render(request, "checkout.html", {'order_form': oreder_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})