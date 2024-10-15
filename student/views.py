from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/auth/login")
def home(request):
    return render(request, "student/home.html")


# @login_required(login_url="/auth/login")
# def index(request):
#     categories = Category.objects.all()
#     expenses = Expenses.objects.filter(owner=request.user)

#     paginator = Paginator(expenses, 1)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     currency = (
#         UserPreference.objects.get(user=request.user).currency
#         if (UserPreference.objects.get(user=request.user).currency)
#         else "NGN"
#     )
#     print(currency, "user")

#     context = {
#         "expenses": expenses,
#         "page_obj": page_obj,
#         "currency": currency,
#     }
#     return render(request, "expenses/index.html", context)
