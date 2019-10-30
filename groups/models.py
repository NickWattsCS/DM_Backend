from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
"""
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
"""

class AdminGroup(models.Model):
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    id = models.CharField(max_length=100, default='')
    firstName = models.CharField(max_length=100, default='')
    lastName = models.CharField(max_length=100, default='')
    permissions = models.CharField(max_length=100, default='Admin')
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        abstract = True
        ordering = ['created']

class UserGroup(AdminGroup):
    permissions = models.CharField(max_length=20, default='User')

class StaffGroup(AdminGroup):
    permissions = models.CharField(max_length=20, default='Staff')

""""
def save(self, *args, **kwargs):
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)
""""
