from django.shortcuts import render
from .models import Product, Brand
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from decimal import Decimal, InvalidOperation
from django.db.models import Case, When, F, DecimalField
from django.db.models.functions import Coalesce

def product(request, pk):
    product_obj = get_object_or_404(Product, id=pk)
    return render(request, "product.html", {"product": product_obj})




def home(request):
    # Brand tiles
    brands = Brand.objects.all().order_by("name")

    # Products grid (optimized for template access)
    products = (
        Product.objects
        .select_related("brand", "category")
        .prefetch_related("tags")
        .all()
    )

    # Click brand tile -> filter ?brand=<slug>
    brand_slug = request.GET.get("brand")
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)

    context = {
        "brands": brands,
        "products": products,
        "active_brand": brand_slug,  # optional (useful for UI state later)
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def cars(request):
    qs = (
        Product.objects
        .select_related("brand", "category")
        .prefetch_related("tags")
        .all()
    )
     # ---------- Filters ----------
    brand_slug = request.GET.get("brand") or ""
    if brand_slug:
        qs = qs.filter(brand__slug=brand_slug)

    on_sale = request.GET.get("sale") == "1"
    if on_sale:
        qs = qs.filter(is_sale=True)

    # Price range (safe parsing)
    min_price = request.GET.get("min_price") or ""
    max_price = request.GET.get("max_price") or ""

    try:
        if min_price != "":
            qs = qs.filter(price__gte=Decimal(min_price))
    except (InvalidOperation, ValueError):
        min_price = ""

    try:
        if max_price != "":
            qs = qs.filter(price__lte=Decimal(max_price))
    except (InvalidOperation, ValueError):
        max_price = ""

    # ---------- Sorting ----------
    # Sort by "effective_price": sale_price if on sale else price
    qs = qs.annotate(
        effective_price=Case(
            When(is_sale=True, then=Coalesce(F("sale_price"), F("price"))),
            default=F("price"),
            output_field=DecimalField(max_digits=8, decimal_places=2),
        )
    )

    sort = request.GET.get("sort") or "featured"

    if sort == "price_asc":
        qs = qs.order_by("effective_price", "id")
    elif sort == "price_desc":
        qs = qs.order_by("-effective_price", "-id")
    elif sort == "name_az":
        qs = qs.order_by("name")
    else:
        # "featured" fallback (stable default)
        qs = qs.order_by("-id")

    brands = Brand.objects.all().order_by("name")

    context = {
        "products": qs,
        "brands": brands,
        "results_count": qs.count(),
        "active": {
            "brand": brand_slug,
            "sale": on_sale,
            "min_price": min_price,
            "max_price": max_price,
            "sort": sort,
        }
    }
    return render(request, "cars.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error. Please try again."))
            return redirect('login')

    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')