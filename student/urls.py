from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="student_home"),
    path("create_new_log", views.add_log, name="add_log"),
    # path("search_expenses", views.search_expenses, name="search_expenses"),
    path("edit_log/<int:id>", views.edit_log, name="edit_log"),
    # path("delete_expenses/<int:id>", views.delete_expenses, name="delete_expenses"),
    # path(
    #     "expenses_category_summary",
    #     views.expenses_category_summary,
    #     name="expenses_category_summary",
    # ),
    # path("view_stats", views.stats_view, name="stats"),
    # path("export_csv", views.export_csv, name="export_csv"),
    # path("export_excel", views.export_excel, name="export_excel"),
    # path("export_excel", views.export_pdf, name="export_pdf"),
]
