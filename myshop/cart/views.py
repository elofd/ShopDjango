from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View


class CartListView(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(buyer=request.user)
        return render(request, 'cart/cart_list.html', {'cart': cart})


class CartAddView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(buyer=request.user)
        cart.products.add(product)
        return redirect('cart:cart_list')


class CartUpdateView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(buyer=request.user)
        quantity = int(request.POST.get('quantity', 1))
        cart.products.add(product, through_defaults={'quantity': quantity})
        return redirect('cart:cart_list')


class CartDeleteView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(buyer=request.user)
        cart.products.remove(product)
        return redirect('cart:cart_list')
