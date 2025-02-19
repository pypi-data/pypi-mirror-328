import random
import string


def random_string(length=6):
    """Generate a random string of fixed length"""
    return ''.join(random.choices(string.ascii_letters, k=length))


def _wrap_in_html_doc(config_html, display_html):
    """Wrap the HTML content in a basic HTML document"""
    return f"""
<html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
            }}
        </style>
        {config_html}
    </head>
    <body>
        {display_html}
    </body>
</html>
"""
