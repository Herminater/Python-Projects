from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("employees/", views.EmployeeView.as_view(), name="employees"),
    path("employees/create", views.EmployeeCreate.as_view(), name="employeecreate"),
    path("employees/<int:pk>/update", views.EmployeeUpdate.as_view(), name="employeeupdate"),
    path("employees/<int:pk>/delete", views.EmployeeDelete.as_view(), name="employeedelete"),
    path("calendars/", views.CalendarView.as_view(), name="calendars"),
    path("calendars/create", views.CalendarCreate.as_view(), name="calendarcreate"),
    path("calendars/<int:pk>/update", views.CalendarUpdate.as_view(), name="calendarupdate"),
    path("calendars/<int:pk>/delete", views.CalendarDelete.as_view(), name="calendardelete"),
    path("shifts/", views.ShiftView.as_view(), name="shifts"),
    path("shifts/create/<str:date>/", views.shift_create, name="shiftcreate"),
    path("shifts/create/", views.shift_create, name="shiftcreatewithoutdate"),
    path("shifts/<int:pk>/<str:date>/update", views.ShiftUpdate.as_view(), name="shiftupdate"),
    path("shifts/<int:pk>/delete", views.ShiftDelete.as_view(), name="shiftdelete"),
    path("fill/create/<str:calendar_id>", views.process_selection, name="fill"),
]   