from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


from .models import LogBook

# Create your views here.


@login_required(login_url="/auth/login")
def home(request):
    logs = LogBook.objects.filter(student=request.user)

    paginator = Paginator(logs, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # currency = (
    #     UserPreference.objects.get(user=request.user).currency
    #     if (UserPreference.objects.get(user=request.user).currency)
    #     else "NGN"
    # )
    # print(currency, "user")

    context = {
        "logs": logs,
        "page_obj": page_obj,
        #         "currency": currency,
    }
    return render(request, "student/home.html", context)


def add_log(request):
    try:
        if request.method == "POST":
            data = request.POST
            context = {"fieldValues": data}
            desc = data.get("log_desc")
            # date = data["log_date"]
            image = data.get("log_img")

            if not desc:
                messages.error(request, "Description Is Required")
                return render(request, "student/add_log.html", context)

            LogBook.objects.create(desc=desc, image=image, student=request.user)
            messages.success(request, "Log saved successfully")
            return redirect("student_home")
        return render(request, "student/add_log.html")

    except Exception as e:
        print(e)
        messages.error(request, "Sorry An Error Occured")
        return render(request, "student/add_log.html")

    # student_logs = LogBook.objects.filter(owner=request.user)


def edit_log(request, id):
    try:
        log = LogBook.objects.get(pk=id)

        context = {
            "fieldValues": log,
            "log": log,
        }

        if request.method == "POST":
            data = request.POST
            desc = data.get("desc")
            if not desc:
                messages.error(request, "Description Is Required")
                return render(request, "student/edit_log.html", context)
            log.desc = desc
            log.student = request.user

            log.save()
            messages.success(request, "Log edited successfully")
            return redirect("student_home")

        return render(request, "student/edit_log.html", context)
    except Exception as e:
        print(e, "error occured")
        messages.error(request, "Sorry An Error Occured")
        return render(request, "student/edit_log.html")


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
