from django.db import models
import markdown
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_content_as_html(self):
        html = markdown.markdown(self.content, extensions=["fenced_code", "codehilite", "tables"])
        return mark_safe(html)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'