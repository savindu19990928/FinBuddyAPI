from django.contrib import admin
from .models import SubscriptionPlan, PromoCode, UserSubscription, Payment

admin.site.register(SubscriptionPlan)
admin.site.register(PromoCode)
admin.site.register(UserSubscription)
admin.site.register(Payment)
