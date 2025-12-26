from django import template
import re

register = template.Library()

@register.filter
def highlight(text, word):
    if word:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        return pattern.sub(
            r'<mark>\g<0></mark>',
            text
        
        )
    return text