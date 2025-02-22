import sys
import markdown
import os

DEFAULT_CSS = """
<style>
body { font-family: 'Inter', sans-serif; line-height: 1.7; max-width: 800px; margin: auto; padding: 20px; }
pre { background: #1e1e1e; color: #d4d4d4; padding: 1em; border-radius: 8px; overflow-x: auto; }
code { font-family: 'Fira Code', monospace; font-size: 14px; }
pre code { display: block; background: none; padding: 0; }
</style>
"""

def load_css(css_path="static/codehilite.css"):
    """Load CSS from file or use fallback."""
    if os.path.exists(css_path):
        try:
            with open(css_path, "r", encoding="utf-8") as file:
                return f"<style>{file.read()}</style>"
        except Exception as e:
            sys.stderr.write(f"Error reading CSS file: {e}\n")
    return DEFAULT_CSS

def convert_markdown():
    """Convert Markdown from stdin to HTML and print to stdout."""
    try:
        markdown_text = sys.stdin.read()
        html = markdown.markdown(markdown_text, extensions=["fenced_code", "codehilite"])
        css = load_css()
        full_html = f'<!DOCTYPE html><html><head><meta charset="UTF-8">{css}</head><body><div class="markdown-body">{html}</div></body></html>'
        sys.stdout.write(full_html)
    except Exception as e:
        sys.stderr.write(f"Error processing markdown: {e}\n")

if __name__ == "__main__":
    convert_markdown()