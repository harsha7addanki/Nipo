from jinja2 import Template

def render(template,context):
    return Template(template).render(**context)