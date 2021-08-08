from django import template
from ..models import Category, Post

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     """Вывод категорий"""
#     return Category.objects.all()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    """Вывод списка категорий"""
    category = Category.objects.all()  # .order_by('name')
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    """Вывод последних 5 постов в меню"""
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {'list_last_post': posts}
