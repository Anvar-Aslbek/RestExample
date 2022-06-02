# from rest_framework import permissions

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     #faqatgina ko'rish uchun ruxsat beriladi
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#     #o'zgartirish yozish uchun ruxsat berish
#     return obj.author == request.user