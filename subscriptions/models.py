from django.db import models
from django.conf import settings
from django.utils import timezone

class SubscriptionPlan(models.Model):
    DURATION_CHOICES = [
        ('DAYS', 'Days'),
        ('WEEKS', 'Weeks'),
        ('MONTHS', 'Months'),
        ('YEARS', 'Years'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration_value = models.IntegerField(default=1)
    duration_unit = models.CharField(max_length=10, choices=DURATION_CHOICES, default='MONTHS')
    is_recurring = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    features = models.JSONField(default=list)
    usage_limits = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class PromoCode(models.Model):
    PROMO_TYPES = [
        ('FREE_DAYS', 'Free Days'),
        ('PERCENTAGE', 'Percentage Discount'),
        ('FIXED', 'Fixed Amount Discount'),
    ]
    code = models.CharField(max_length=50, unique=True)
    promo_type = models.CharField(max_length=20, choices=PROMO_TYPES)
    value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Number of days or discount amount/percentage")
    start_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(null=True, blank=True)
    max_total_uses = models.IntegerField(default=0, help_text="0 for unlimited")
    max_uses_per_user = models.IntegerField(default=1)
    applicable_plans = models.ManyToManyField(SubscriptionPlan, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class UserSubscription(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('CANCELLED', 'Cancelled'),
        ('PAYMENT_FAILED', 'Payment Failed'),
        ('PAST_DUE', 'Past Due'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name if self.plan else 'Unknown Plan'}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    subscription = models.ForeignKey(UserSubscription, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    payment_method = models.CharField(max_length=50, default='PayPal')
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.user.username}"
