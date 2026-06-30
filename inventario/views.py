from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Producto, Categoria, MovimientoStock
from .forms import ProductoForm, CategoriaForm, MovimientoStockForm, BusquedaForm


class EsAdminMixin(UserPassesTestMixin):
    """Restringe una vista a usuarios staff (administradores)."""
    def test_func(self):
        return self.request.user.is_staff


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        productos = Producto.objects.filter(activo=True)
        ctx['total_productos'] = productos.count()
        ctx['stock_total'] = productos.aggregate(t=Sum('stock'))['t'] or 0
        ctx['valor_inventario'] = sum(p.valor_total for p in productos)
        ctx['stock_bajo'] = [p for p in productos if p.stock_bajo]
        ctx['sin_stock'] = [p for p in productos if p.stock == 0]
        ctx['ultimos_movimientos'] = MovimientoStock.objects.select_related('producto', 'usuario')[:8]
        return ctx


# ---------- Productos ----------

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'inventario/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        qs = Producto.objects.filter(activo=True).select_related('categoria')
        self.form = BusquedaForm(self.request.GET)
        if self.form.is_valid():
            if q := self.form.cleaned_data.get('q'):
                qs = qs.filter(nombre__icontains=q)
            if categoria := self.form.cleaned_data.get('categoria'):
                qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form
        return ctx


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'inventario/producto_detail.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['movimientos'] = self.object.movimientos.select_related('usuario')[:10]
        ctx['movimiento_form'] = MovimientoStockForm()
        return ctx


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, f'Producto "{form.instance.nombre}" creado.')
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, f'Producto "{form.instance.nombre}" actualizado.')
        return super().form_valid(form)


class ProductoDeleteView(LoginRequiredMixin, EsAdminMixin, DeleteView):
    model = Producto
    template_name = 'inventario/confirmar_eliminar.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        # Baja lógica en vez de borrar de verdad
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        messages.success(self.request, f'Producto "{self.object.nombre}" eliminado.')
        return redirect(self.success_url)


@login_required
def registrar_movimiento(request, pk):
    """Registra una entrada/salida de stock y actualiza el producto."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = MovimientoStockForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            tipo = form.cleaned_data['tipo']
            nuevo_stock = producto.stock + cantidad if tipo == 'entrada' else producto.stock - cantidad
            if nuevo_stock < 0:
                messages.error(request, 'El movimiento dejaría el stock en negativo.')
            else:
                with transaction.atomic():
                    producto.stock = nuevo_stock
                    producto.save()
                    movimiento = form.save(commit=False)
                    movimiento.producto = producto
                    movimiento.usuario = request.user
                    movimiento.save()
                messages.success(request, 'Movimiento de stock registrado.')
    return redirect('producto_detail', pk=pk)


# ---------- Categorías (solo administradores) ----------

class CategoriaListView(LoginRequiredMixin, EsAdminMixin, ListView):
    model = Categoria
    template_name = 'inventario/categoria_list.html'
    context_object_name = 'categorias'


class CategoriaCreateView(LoginRequiredMixin, EsAdminMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoria_form.html'
    success_url = reverse_lazy('categoria_list')


class CategoriaUpdateView(LoginRequiredMixin, EsAdminMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoria_form.html'
    success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(LoginRequiredMixin, EsAdminMixin, DeleteView):
    model = Categoria
    template_name = 'inventario/confirmar_eliminar.html'
    success_url = reverse_lazy('categoria_list')