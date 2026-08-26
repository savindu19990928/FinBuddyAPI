# FinBuddy - Personal Finance Management System

## 1. System Overview
FinBuddy is a comprehensive personal finance application designed to help users manage their income, expenses, accounts, budgets, savings, and bills. 

The front-end application interacts directly with the FinBuddy API. All features listed below are available to the end-user through these API endpoints. Administrative and management functions are strictly handled outside of this scope.

---

## 2. User Authentication & Profile Management

Users can securely manage their access and personal details:
- **Registration**: Create a new account with email and password.
- **Login/Logout**: Secure JWT-based authentication.
- **Password Recovery**: Reset forgotten passwords securely.
- **Profile Management**: Update personal information including full name, phone number, and profile picture (uploaded to cloud storage).
- **Preferences**: Set a preferred currency and time zone for accurate financial reporting.
- **Notifications**: Manage personal notification preferences.
- **Account Deletion**: Request permanent account deletion.

---

## 3. Subscription Management & Payments

FinBuddy operates on a flexible subscription model. Users can seamlessly manage their plans and payments directly from the front-end:

### Subscriptions
- **View Available Plans**: Browse all active subscription plans, their included features, duration, and prices (including zero-price/free access plans).
- **Current Subscription Status**: View the active subscription, start date, expiration date, and auto-renewal/next billing date.
- **Purchase Subscription**: Select a plan and proceed to checkout.
- **Cancel Subscription**: Turn off auto-renewal for recurring subscriptions.

### Payments & Promos
- **Promo Codes**: Apply valid promotional codes (for free days or price discounts) during the checkout process and instantly see the discounted price.
- **PayPal Integration**: Complete subscription purchases securely via the PayPal Checkout integration.
- **Payment History**: View a complete history of past transactions, including the original price, discounts applied, promo codes used, payment status, and final amount paid.

---

## 4. Personal Finance Management

Users have complete control over their daily finances across multiple dimensions.

### Financial Accounts
- **Manage Accounts**: Create, edit, and delete multiple financial accounts (e.g., Cash, Bank Account, Credit Card, Digital Wallet).
- **Track Balances**: Set opening balances and view real-time current balances for each account.
- **Money Transfers**: Record money transfers between internal accounts (e.g., Bank to Cash). These transfers dynamically update account balances without artificially inflating income or expense totals.

### Income & Expenses
- **Record Income**: Log incoming funds (Salary, Freelance, etc.) specifying the amount, date, receiving account, and source description.
- **Record Expenses**: Log outgoing transactions (Food, Rent, etc.) specifying the amount, date, originating account, and merchant.
- **Categories**: Categorize transactions using system-default categories or by creating personalized custom categories tailored to the user's lifestyle.
- **Search & Filter**: Find specific transactions by filtering through dates, categories, accounts, merchants, or exact amounts.

### Budgets
- **Create Budgets**: Set spending limits for specific categories over a defined period (e.g., Rs. 20,000 for Food this month).
- **Track Progress**: View real-time progress showing total spent vs. remaining budget amount to prevent overspending.

### Savings Goals
- **Set Goals**: Create targeted savings goals (e.g., "Buy a Laptop").
- **Track Savings**: Set target amounts and dates, manually log saved amounts, and visualize the progress towards the goal.
- **Completion**: Mark goals as completed once the target is reached.

### Bills & Recurring Transactions
- **Manage Bills**: Track upcoming bills (e.g., Electricity, Rent), set due dates, and mark them as paid to keep track of liabilities.
- **Recurring Transactions**: Automate the logging of regular income (e.g., monthly salary) or expenses (e.g., internet bill). The system can generate these automatically on a daily, weekly, monthly, or yearly schedule.

---

## 5. Dashboard & Analytics

The front-end can provide rich, visual insights based on the user's financial data returned by the API.

- **Main Dashboard**: A high-level overview displaying current total balance, monthly income/expenses, total savings, remaining budgets, and upcoming bills.
- **Financial Reports**: Generate detailed reports such as cash-flow statements, income vs. expense comparisons, and category-wise spending breakdowns.
- **Custom Timeframes**: Filter analytics and reports by specific time ranges (Today, This Week, This Month, This Year, or Custom Ranges).

---

## 6. User Support

Users can interact with the support team directly from the application:
- **Submit Tickets**: Create new support requests detailing issues, questions, or bugs.
- **Track Status**: View the current status of their requests (Open, In Progress, Resolved, Closed).
- **Communication**: Read replies from support agents and send follow-up messages within the support ticket thread.
