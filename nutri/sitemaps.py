try:
    from blog.sitemaps import sitemaps as blog_sitemaps
except ImportError:
    blog_sitemaps = {}

try:
    from helen.sitemaps import sitemaps as helen_sitemaps
except ImportError:
    helen_sitemaps = {}

# Объединяем все sitemaps проекта
sitemaps = {}
sitemaps.update(helen_sitemaps)
sitemaps.update(blog_sitemaps)
