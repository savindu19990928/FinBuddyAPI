# Personal Finance Management System
## Functional Requirements Specification

---

# 1. System Overview

The Personal Finance Management System is a personal finance application that allows users to manage their income, expenses, accounts, budgets, savings, bills, and financial reports.

The application uses a subscription-based access system.

Users can:

- Create an account
- Receive free access where available
- Purchase subscription plans
- Pay for subscriptions using PayPal
- Apply promotional codes
- Manage personal finances
- View financial reports
- Manage budgets and savings goals

The system also provides an administration dashboard for managing users, subscriptions, payments, promotional codes, and other system functions.

---

# 2. User Roles

The system shall have two levels of administrative access:

## 2.1 User

A normal user can:

- Register and log in
- Manage their profile
- Manage their personal finances
- Manage their subscription
- Purchase subscriptions
- Apply promotional codes
- View payment history
- Manage financial accounts
- Manage income and expenses
- Create budgets
- Create savings goals
- Manage bills and recurring transactions
- View financial reports

Users must only be able to access their own financial information.

---

## 2.2 Super Admin

The Super Admin has full administrative access.

The Super Admin can:

- Manage users
- Create and manage Admin accounts
- Assign permissions to Admins
- Manage subscription plans
- Manage user subscriptions
- Manage promotional codes
- Manage payments
- Manage categories
- View revenue reports
- Manage notifications
- Manage support requests
- Manage system settings
- View audit records

---

## 2.3 Admin

Admins are created by the Super Admin.

An Admin does not automatically have access to every administrative function.

The Super Admin can assign individual permissions to each Admin.

For example:

**Admin A**

- Manage users
- View subscriptions
- View payments

**Admin B**

- Manage subscription plans
- Manage promo codes
- View revenue reports

The permissions of each Admin can be different.

Admins cannot give themselves additional permissions.

Only the Super Admin can manage Admin accounts and their permissions.

---

# 3. User Registration & Account Management

The system shall allow users to:

- Register for an account
- Log in
- Log out
- Verify their email address
- Recover a forgotten password
- Change their password
- Update their personal information
- Change their profile information
- Manage notification preferences
- Delete their account

---

# 4. User Profile

Users can manage:

- Full name
- Email address
- Phone number
- Profile picture
- Preferred currency
- Time zone
- Password
- Notification preferences

---

# 5. Subscription System

The system shall use a flexible subscription system.

There is **no separate subscription type called "Trial"**.

Every subscription plan can have:

- A price
- A duration
- A recurring or non-recurring behavior
- Features
- Usage limits

A subscription can have a price of zero.

For example:

> Free Access — Rs. 0 — 14 Days — Non-Recurring

This can be used as a free trial.

---

# 6. Subscription Plans

The system shall allow the Super Admin and authorized Admins to create and manage subscription plans.

Each plan can have:

- Plan name
- Description
- Price
- Duration
- Billing behavior
- Available features
- Usage limits
- Active/inactive status

---

# 7. Subscription Duration

The administrator shall be able to configure different subscription durations.

Supported durations can include:

- Days
- Weeks
- Months
- Years

Examples:

- 7 Days
- 14 Days
- 1 Week
- 30 Days
- 45 Days
- 1 Month
- 2 Months
- 6 Months
- 1 Year

The system should not restrict subscription plans to only monthly or yearly periods.

---

# 8. Subscription Price

Each subscription plan can have its own price.

Examples:

- Rs. 0
- Rs. 300
- Rs. 999
- Rs. 1,500
- Rs. 2,000
- Rs. 9,999

A subscription plan with a price of zero is allowed.

---

# 9. Subscription Billing Behavior

Each subscription plan can be either:

### Recurring

The subscription automatically renews after the configured period.

Example:

> Rs. 999 — 1 Month — Recurring

The subscription continues by charging the user for each renewal period.

### Non-Recurring

The subscription remains active for the configured period and then expires.

Example:

> Rs. 2,000 — 45 Days — Non-Recurring

The user must purchase another subscription after it expires.

---

# 10. Free Access

The system shall not have a separate "Trial Subscription".

Instead, the administrator can create a normal subscription plan with:

- Price = Rs. 0
- Non-recurring duration

Example:

> Free Access  
> Rs. 0  
> 14 Days  
> Non-Recurring

This subscription can be automatically provided to newly registered users.

---

# 11. Free Access Configuration

The administrator can configure:

- Whether free access is enabled
- Which subscription plan is used for free access
- Free access duration
- Whether new users automatically receive free access
- Whether a user can receive free access only once

Example:

> Free Access: Enabled  
> Default Plan: 14 Days Free  
> One Free Access Per User: Yes

---

# 12. Subscription Management – User

Users can:

- View available plans
- Compare plans
- Select a subscription
- View subscription price
- View subscription duration
- View included features
- Purchase a subscription
- Apply a promo code
- View current subscription
- View subscription start date
- View expiration date
- View next renewal date
- Cancel recurring subscriptions where applicable
- View subscription history

---

# 13. Subscription Status

A user's subscription can have statuses such as:

- Active
- Expired
- Cancelled
- Payment Failed
- Past Due

The system shall clearly display the current subscription status to the user.

---

# 14. Subscription Expiration

For non-recurring subscriptions:

- The subscription becomes active after successful activation.
- The subscription remains active until its expiration date.
- The subscription automatically becomes expired after the configured period.
- The user can purchase another subscription after expiration.

User financial information must not be deleted when a subscription expires.

---

# 15. Subscription Renewal

For recurring subscriptions:

- The system shall attempt to renew the subscription.
- The user shall be charged according to the subscription plan.
- The subscription shall continue after successful renewal.
- The user should be notified about successful renewal.
- The user should be notified if renewal fails.

---

# 16. Subscription Plan Management – Admin

Authorized administrators can:

- Create subscription plans
- Edit subscription plans
- Activate plans
- Deactivate plans
- Change plan prices
- Change plan durations
- Change recurring/non-recurring behavior
- Configure plan features
- Configure usage limits
- View subscribers
- View subscription statistics

Changes to a plan should not alter historical subscription information.

---

# 17. PayPal Subscription Payments

The system shall support **PayPal Checkout** for paid subscription purchases.

Users can pay for their selected subscription using PayPal.

The payment process should allow the user to:

1. Select a subscription plan.
2. Apply a promotional code if available.
3. View the original price.
4. View the discount.
5. View the final price.
6. Continue to PayPal Checkout.
7. Complete the payment.
8. Return to the application.
9. Receive the subscription after successful payment confirmation.

---

# 18. Payment Verification

The system must verify the payment before activating a paid subscription.

The system shall:

- Confirm whether the payment was successful.
- Confirm the amount paid.
- Associate the payment with the correct user.
- Associate the payment with the correct subscription.
- Prevent duplicate subscription activation.
- Handle failed payments.
- Handle cancelled payments.
- Handle refunds where applicable.

A user must not receive paid subscription access based only on a client-side payment response.

---

# 19. Payment History – User

Users can view:

- Payment date
- Subscription purchased
- Amount
- Discount
- Promo code used
- Final amount
- Payment status
- Payment method

Users should be able to view their previous subscription purchases.

---

# 20. Payment Management – Admin

Authorized administrators can:

- View payments
- Search payments
- Filter payments
- View successful payments
- View failed payments
- View cancelled payments
- View refunded payments
- View payment details
- View payment history
- Export payment information

---

# 21. Promo Code System

The system shall support two types of promotional codes:

1. **Free Days Promo**
2. **Discount Promo**

---

# 22. Free Days Promo

A Free Days Promo gives the user additional free subscription days.

Example:

> Promo Code: FREE15  
> Type: Free Days  
> Free Days: 15

If a user purchases a 30-day subscription, the promotion can provide:

> 30 Days + 15 Free Days

The administrator can configure:

- Promo code
- Number of free days
- Start date
- Expiration date
- Maximum total uses
- Maximum uses per user
- Applicable subscription plans
- Active/inactive status

---

# 23. Discount Promo

A Discount Promo reduces the price of a subscription.

The system shall support:

## Percentage Discount

Example:

> 20% discount

If the subscription costs Rs. 1,000:

> Original Price: Rs. 1,000  
> Discount: Rs. 200  
> Final Price: Rs. 800

## Fixed Amount Discount

Example:

> Rs. 500 discount

If the subscription costs Rs. 2,000:

> Original Price: Rs. 2,000  
> Discount: Rs. 500  
> Final Price: Rs. 1,500

---

# 24. Promo Code Configuration – Admin

Authorized administrators can:

- Create promo codes
- Edit promo codes
- Activate promo codes
- Deactivate promo codes
- Delete promo codes
- Set promo type
- Set free days
- Set percentage discounts
- Set fixed discounts
- Set start date
- Set expiration date
- Set maximum total usage
- Set maximum usage per user
- Select applicable subscription plans
- View promo usage

---

# 25. Promo Code Validation

When a user enters a promo code, the system shall check:

- Whether the promo code exists
- Whether it is active
- Whether it has expired
- Whether it has reached its maximum usage
- Whether the user has already exceeded their allowed usage
- Whether it applies to the selected subscription
- Whether the promotion is still valid

The user should see the discount or additional free days before completing the purchase.

---

# 26. Income Management

Users can record their income.

Income can include:

- Salary
- Freelance income
- Business income
- Investment income
- Gifts
- Other income

Users can:

- Add income
- Edit income
- Delete income
- View income
- Search income
- Filter income
- Categorize income

Income information can include:

- Amount
- Category
- Date
- Account
- Description
- Source

---

# 27. Expense Management

Users can record their expenses.

Examples:

- Food
- Transport
- Shopping
- Rent
- Utilities
- Education
- Entertainment
- Healthcare

Users can:

- Add expenses
- Edit expenses
- Delete expenses
- View expenses
- Search expenses
- Filter expenses
- Categorize expenses

Expense information can include:

- Amount
- Category
- Date
- Account
- Description
- Merchant

---

# 28. Financial Accounts

Users can create financial accounts such as:

- Cash
- Bank accounts
- Savings accounts
- Credit cards
- Digital wallets

Users can:

- Add accounts
- Edit accounts
- Delete accounts
- Set opening balance
- View current balance
- View account transactions

---

# 29. Money Transfers

Users can transfer money between their own financial accounts.

Example:

> Bank Account → Cash  
> Rs. 20,000

The system should update both account balances.

Transfers between a user's own accounts should not be counted as income or expenses.

---

# 30. Categories

The system shall provide default income and expense categories.

Users can also create their own categories where permitted.

### Income Categories

- Salary
- Freelance
- Business
- Investment
- Gift
- Other

### Expense Categories

- Food
- Transport
- Shopping
- Housing
- Bills
- Education
- Entertainment
- Healthcare
- Other

Authorized administrators can manage default/system categories.

---

# 31. Budget Management

Users can create budgets for their spending.

Example:

> Food Budget: Rs. 20,000  
> Spent: Rs. 14,500  
> Remaining: Rs. 5,500

Users can:

- Create budgets
- Select categories
- Set budget amounts
- Set budget periods
- Edit budgets
- Delete budgets
- View budget progress

The system can notify users when they approach or exceed a budget.

---

# 32. Savings Goals

Users can create savings goals.

Example:

> Goal: Buy Laptop  
> Target: Rs. 250,000  
> Saved: Rs. 100,000  
> Remaining: Rs. 150,000

Users can:

- Create goals
- Set target amounts
- Set target dates
- Add savings
- View progress
- Edit goals
- Delete goals
- Mark goals as completed

---

# 33. Recurring Transactions

Users can create recurring income and expense transactions.

Examples:

- Monthly salary
- Monthly rent
- Monthly internet bill
- Monthly subscriptions
- Weekly expenses

Users can configure:

- Amount
- Category
- Account
- Frequency
- Start date
- End date

The system shall create the relevant transactions according to the configured schedule.

---

# 34. Bills & Reminders

Users can create bills and payment reminders.

Examples:

- Electricity bill
- Water bill
- Internet bill
- Rent
- Credit card payment

Users can:

- Add bills
- Set due dates
- Set amounts
- Assign categories
- Set recurring bills
- Mark bills as paid
- Edit bills
- Delete bills

The system can remind users before the due date.

---

# 35. User Dashboard

The main dashboard should provide an overview of the user's finances.

It can display:

- Current balance
- Total income
- Total expenses
- Total savings
- Monthly income
- Monthly expenses
- Remaining budget
- Recent transactions
- Upcoming bills
- Savings goals
- Current subscription
- Subscription expiration/renewal information

---

# 36. Financial Charts

The application can display visual financial information such as:

- Income vs expenses
- Expenses by category
- Monthly spending
- Savings progress
- Budget usage
- Account balances

---

# 37. Transaction Search & Filtering

Users should be able to search and filter transactions.

Filtering options can include:

- Date
- Category
- Income/expense
- Account
- Amount
- Merchant
- Recurring transactions

---

# 38. Financial Reports

Users can view:

- Income reports
- Expense reports
- Monthly summaries
- Category-wise expense reports
- Account reports
- Budget reports
- Savings reports
- Cash-flow reports
- Income vs expense reports
- Recurring expense reports

Users can select:

- Today
- This week
- This month
- Last month
- This year
- Custom date range

---

# 39. Notifications

The system can notify users about:

- Subscription expiration
- Subscription renewal
- Successful payments
- Failed payments
- Upcoming bills
- Budget limits
- Recurring transactions
- Savings progress
- Promotional offers

---

# 40. Admin Dashboard

The Admin Dashboard should provide an overview of the entire application.

It can display:

### Users

- Total users
- New users today
- New users this week
- New users this month
- Active users
- Inactive users
- Suspended users

### Subscriptions

- Active subscriptions
- Expired subscriptions
- Cancelled subscriptions
- Recurring subscriptions
- Non-recurring subscriptions
- Free subscriptions
- Subscriptions by plan

### Payments

- Today's revenue
- Weekly revenue
- Monthly revenue
- Yearly revenue
- Total revenue
- Successful payments
- Failed payments
- Refunds

### Promo Codes

- Active promo codes
- Expired promo codes
- Total promo redemptions
- Free-days promo usage
- Discount promo usage
- Most-used promo codes

---

# 41. Admin Dashboard Charts

The dashboard can provide charts for:

### User Growth

- Daily registrations
- Weekly registrations
- Monthly registrations

### Revenue

- Daily revenue
- Monthly revenue
- Yearly revenue

### Subscriptions

- Active subscriptions
- Expired subscriptions
- Cancelled subscriptions
- Subscriptions by plan

### Promo Usage

- Promo usage over time
- Usage by promo code
- Free-days vs discount promotions

---

# 42. User Management – Admin

Authorized administrators can:

- View users
- Search users
- Filter users
- View user information
- Edit user information
- Activate users
- Deactivate users
- Suspend users
- Delete users
- View subscription information
- View subscription history
- View payment history
- View promo usage

Access to sensitive personal financial information should only be provided to administrators when specifically required and permitted.

---

# 43. Subscription Management – Admin

Authorized administrators can:

- View subscription plans
- Create plans
- Edit plans
- Activate/deactivate plans
- Change prices
- Change durations
- Change billing behavior
- Configure features
- Configure limits
- View subscribers
- Search subscriptions
- Filter subscriptions
- View expired subscriptions
- View cancelled subscriptions
- Extend user subscriptions where authorized
- Cancel user subscriptions where authorized

---

# 44. Revenue Reports – Admin

Authorized administrators can view application revenue reports.

Reports can include:

- Gross subscription revenue
- Discounts
- Refunds
- Net revenue
- Revenue by subscription plan
- Revenue by date
- Revenue by recurring/non-recurring subscriptions

---

# 45. Category Management – Admin

Authorized administrators can:

- Create default categories
- Edit categories
- Activate/deactivate categories
- Delete categories where appropriate
- Manage income categories
- Manage expense categories

---

# 46. Support Management

Users can submit support requests.

Users can:

- Create support requests
- View their requests
- Reply to requests
- View request status

Administrators with the appropriate permissions can:

- View support requests
- Search requests
- Filter requests
- Reply to users
- Change request status
- Close requests

Possible statuses:

- Open
- In Progress
- Resolved
- Closed

---

# 47. Admin Management

Only the Super Admin can manage Admin accounts.

The Super Admin can:

- Create Admin accounts
- Edit Admin accounts
- Activate Admin accounts
- Deactivate Admin accounts
- Delete Admin accounts
- Assign permissions
- Remove permissions
- View Admin activity

There are no fixed Admin categories.

Each Admin receives permissions according to their responsibilities.

---

# 48. Admin Permissions

The Super Admin can assign permissions for areas such as:

### User Management

- View users
- Create users
- Edit users
- Delete users
- Suspend users

### Subscription Management

- View plans
- Create plans
- Edit plans
- Delete plans
- View user subscriptions
- Manage user subscriptions

### Promo Management

- View promo codes
- Create promo codes
- Edit promo codes
- Delete promo codes

### Payment Management

- View payments
- View payment details
- View refunds
- Export payment records

### Reports

- View revenue reports
- Export reports

### Categories

- View categories
- Create categories
- Edit categories
- Delete categories

### Support

- View support requests
- Reply to support requests
- Manage support requests

### Notifications

- Create notifications
- Send notifications
- Manage notifications

### Settings

- View settings
- Change settings

### Audit Records

- View administrative activity

---

# 49. Audit Records

The system shall record important administrative activities.

Examples:

- Super Admin creates an Admin
- Super Admin assigns permissions
- Admin creates a subscription plan
- Admin changes a subscription price
- Admin creates a promo code
- Admin disables a promo code
- Admin suspends a user
- Admin extends a subscription
- Admin processes a refund
- Admin changes free-access settings

The records should allow authorized administrators to identify:

- Who performed the action
- What action was performed
- What was affected
- When the action occurred

---

# 50. System Settings

Authorized administrators can manage system settings such as:

### General

- Application name
- Logo
- Default currency
- Time zone
- Date format

### Subscriptions

- Free-access settings
- Default free-access plan
- Subscription settings
- Renewal settings

### Payments

- PayPal payment settings
- Payment currency
- Payment environment

### Notifications

- Email notifications
- Subscription reminders
- Payment notifications
- Promotional notifications

---

# 51. Admin Notifications

Authorized administrators can send system notifications to users.

Target groups can include:

- All users
- Free-access users
- Active subscribers
- Users with expiring subscriptions
- Specific users

Notifications can be used for:

- System announcements
- Maintenance announcements
- New features
- Promotions
- Subscription reminders

---

# 52. Data Export

Authorized administrators can export system information such as:

- Users
- Subscriptions
- Payments
- Promo usage
- Revenue reports
- Support requests
- Administrative activity

Supported formats can include:

- CSV
- Excel
- PDF

---

# 53. Important Business Rules

1. There is only one Subscription concept.
2. There is no separate Trial Subscription.
3. A subscription plan can have a price of zero.
4. A zero-price, non-recurring subscription can be used as free access/trial.
5. Subscription durations can be configured flexibly.
6. Subscription durations can be days, weeks, months, or years.
7. A subscription can be recurring or non-recurring.
8. Non-recurring subscriptions expire after their configured duration.
9. Recurring subscriptions can automatically renew.
10. Paid subscription payments are processed through PayPal Checkout.
11. Payments must be verified before paid access is granted.
12. Promo codes can provide either free days or discounts.
13. Promo codes can have usage limits.
14. Promo codes can be restricted to specific subscription plans.
15. Historical subscription purchases should retain the price and discount that were applied at the time of purchase.
16. Subscription expiration must not delete the user's financial information.
17. Users can retain their account and financial data after subscription expiration.
18. Users can only access their own financial information.
19. Administrative access is permission-based.
20. Only the Super Admin can create and manage Admin accounts.
21. Only the Super Admin can assign permissions to Admins.
22. Admins cannot assign permissions to themselves.
23. Important administrative actions should be recorded.
24. PayPal payment credentials must remain secure.
25. The system must prevent duplicate payment processing.
26. Promo discounts must be validated before payment.
27. The final subscription price must be confirmed before payment.
28. Changing a subscription plan should not change previous purchases.
29. Free-access settings should apply to new users unless an administrator explicitly changes an existing user's subscription.
30. Deactivating a subscription plan should not automatically cancel existing active subscriptions unless explicitly configured to do so.

---

# 54. MVP Functional Requirements

## Account Management

- Registration
- Login
- Logout
- Email verification
- Password recovery
- Profile management

## Personal Finance

- Dashboard
- Income management
- Expense management
- Categories
- Financial accounts
- Account transfers
- Budgets
- Savings goals
- Recurring transactions
- Bills
- Basic financial reports
- Transaction search and filtering

## Subscription

- Subscription plans
- Flexible subscription durations
- Zero-price subscriptions
- Recurring subscriptions
- Non-recurring subscriptions
- Free-access configuration
- Subscription purchase
- Subscription expiration
- Subscription renewal
- Subscription history

## Payments

- PayPal Checkout
- Payment confirmation
- Payment verification
- Payment history
- Failed payment handling
- Payment cancellation handling
- Refund handling where applicable

## Promo Codes

- Free-days promotions
- Percentage discounts
- Fixed-amount discounts
- Promo validation
- Usage limits
- Plan restrictions

## Administration

- Super Admin
- Admin accounts
- Individual Admin permissions
- Admin dashboard
- User management
- Subscription management
- Promo management
- Payment management
- Revenue reports
- Category management
- Support management
- Notifications
- Audit records
- System settings

---

# 55. Future Functional Features

The system can later support:

- Bank account integration
- Automatic transaction importing
- Receipt scanning
- AI expense categorization
- AI financial insights
- Investment tracking
- Debt management
- Multiple currencies
- Currency conversion
- Shared/family finances
- Financial forecasting
- Tax management
- Mobile applications
- Push notifications
- Advanced analytics
- Financial recommendations

---

# 56. Overall User Flow

```text
User Registration
       ↓
Free Access Available?
       ↓
      Yes
       ↓
Receive Zero-Price Subscription
       ↓
Use Application
       ↓
Subscription Expires
       ↓
Select Paid Subscription
       ↓
Apply Promo Code
       ↓
Pay with PayPal
       ↓
Payment Verified
       ↓
Subscription Activated
       ↓
Use Application
       ↓
Subscription Renewal / Expiration
```

---

# 57. Overall Administration Flow

```text
Super Admin
     │
     ├── Manage Admins
     │      └── Assign Permissions
     │
     ├── Manage Users
     │
     ├── Manage Subscription Plans
     │
     ├── Manage Promo Codes
     │
     ├── Manage Payments
     │
     ├── View Revenue
     │
     ├── Manage Categories
     │
     ├── Manage Support
     │
     ├── Manage Notifications
     │
     ├── View Audit Records
     │
     └── Manage Settings
```

Admins can only access the sections for which the Super Admin has granted them permission.