from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    
    # Renamed dictionary to avoid conflict
    priority_mapping = {
        'home': 1.00,
        'about': 0.80,
        'register': 0.80,
        'blog': 0.80,
        'faq': 0.80,
        'services': 0.80,
        'contact': 0.80,
        'blog_page_2': 0.64,
        'blog_page_3': 0.64,
        'blog_page_1': 0.51,
    }

    def items(self):
        return [
            'home',
            'about',
            'register',
            'blog',
            'faq',
            'services',
            'contact',
            'blog_page_1',
            'blog_page_2',
            'blog_page_3',
        ]

    def location(self, item):
        if "blog_page" in item:
            page_number = item.split("_")[-1]
            return f"/blog?page={page_number}"
        return reverse(item)

    def priority(self, item):
        return self.priority_mapping.get(item, 0.5)  # Now using priority_mapping
