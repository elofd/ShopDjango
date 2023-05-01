from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Category, Product, Order


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shop/order_list.html'
    context_object_name = 'orders'


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'shop/order_detail.html'
    context_object_name = 'order'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'shop/order_form.html'

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'shop/order_form.html'


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'shop/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
