from django.contrib import admin
from .models import Budget, SavingsGoal, Bill, RecurringTransaction

admin.site.register(Budget)
admin.site.register(SavingsGoal)
admin.site.register(Bill)
admin.site.register(RecurringTransaction)
