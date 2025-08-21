# Restrict_Access_Based
Restrict Access Based on User Roles

Role-Based Access Control (RBAC) in Django REST Framework

This project demonstrates Role-Based Access Control (RBAC) using Django and Django REST Framework (DRF).
It restricts access to certain API endpoints based on the user's role (Admin, Manager, Cashier, Waiter).

Features:
Custom User model with a role field.
Role choices: Admin, Manager, Cashier, Waiter.
Custom DRF permissions to control access.

Example use case:
• Admin/Manager → Can add or edit menu items.
• Waiter → Can place customer orders.
• Cashier → Can process payments.
• Admin → Has full access.

Tech Stack:
Python 3.10+
Django 5+
Django REST Framework
SQLite (default) – can be switched to PostgreSQL/MySQL

Project Structure:
restaurant/
│── restaurant/ (Project settings)
│── menu/ (App for dishes)
│── orders/ (App for orders)
│── users/ (Custom user with roles)
│── manage.py

Usage:
Create Users with Roles
Go to /admin/ → Create new users → Assign role (Admin, Manager, Cashier, Waiter).
Role-Based Permissions

Menu endpoints:
Admin & Manager → Add/Edit/Delete dishes
Others → Read only

Order endpoints:
Waiter → Can place new orders
Admin & Manager → Can view all orders

Payments endpoints:
Cashier → Can process payments
Admin → Full access

Example Permission Class (permissions.py):

from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
def has_permission(self, request, view):
return request.user.role in ["Admin", "Manager"]

class IsWaiter(BasePermission):
def has_permission(self, request, view):
return request.user.role == "Waiter"

class IsCashier(BasePermission):
def has_permission(self, request, view):
return request.user.role == "Cashier"

Testing:
Create users with different roles.
Try accessing different endpoints with their credentials.
Verify access restrictions work as expected.
Future Enhancements:
JWT Authentication for API users.
Role + Permission mapping in database (more flexible).
API documentation with Swagger/OpenAPI.

Author:
Sandhya Rani Panda
Email: panda.sandhyarani2001@gmil.com
