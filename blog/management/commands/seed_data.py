from django.core.management.base import BaseCommand
from authentication.models import User
from blog.models import Blog, Category


CATEGORIES = ['Python', 'Django', 'Web Development', 'Database', 'HTML/CSS', 'API']

BLOG_POSTS = [
    {
        'title': 'Getting Started with Django: A Comprehensive Guide',
        'short_description': 'Learn how to build your first Django web application from scratch with this step-by-step tutorial for beginners.',
        'slug': 'getting-started-with-django',
        'category': 'Django',
        'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

In this comprehensive guide, we will walk through the process of setting up a Django project from scratch. We will cover installation, project structure, views, URLs, templates, models, and the admin interface.

First, make sure you have Python installed on your system. Django requires Python 3.10 or higher. You can check your Python version by running python --version in your terminal.

Next, install Django using pip: pip install django. Once installed, you can create a new project by running: django-admin startproject myproject.

This will create a new directory with the project structure. Let us explore each file and understand their purpose.''',
        'status': 'Published',
    },
    {
        'title': 'Python Tips & Tricks Every Developer Should Know',
        'short_description': 'Boost your productivity with these essential Python techniques and best practices.',
        'slug': 'python-tips-tricks',
        'category': 'Python',
        'content': '''Python is one of the most versatile and powerful programming languages available today. Whether you are a beginner or an experienced developer, there is always something new to learn.

Here are some essential Python tips and tricks that will help you write cleaner, more efficient code.

1. Use list comprehensions instead of for loops for simple transformations. They are more readable and faster.

2. Leverage the power of f-strings for string formatting. They are more readable and performant than older methods.

3. Use enumerate() when you need both the index and value from a sequence.

4. Take advantage of Python's built-in functions like map(), filter(), and reduce().

5. Use context managers (with statements) for resource management.

6. Master the standard library - it is full of useful modules.

These tips will help you become a more effective Python developer.''',
        'status': 'Published',
    },
    {
        'title': 'Building Responsive Websites with Bootstrap 5',
        'short_description': 'Master the art of creating beautiful, responsive web layouts using Bootstrap 5 framework.',
        'slug': 'bootstrap-5-crash-course',
        'category': 'Web Development',
        'content': '''Bootstrap 5 is the latest version of the world's most popular CSS framework. It makes front-end web development faster and easier by providing a comprehensive set of pre-built components and utilities.

In this crash course, we will cover the essential features of Bootstrap 5 that you need to know to build responsive websites.

The grid system is the foundation of Bootstrap. It uses a 12-column layout that automatically adapts to different screen sizes. You can use classes like container, row, col-md-6, and col-lg-4 to create responsive layouts.

Bootstrap 5 also includes a wide range of components such as navbars, cards, buttons, forms, modals, and carousels. These components are designed to be accessible and customizable.

One of the biggest changes in Bootstrap 5 is the removal of jQuery dependency. All components are now built with vanilla JavaScript, making them lighter and faster.''',
        'status': 'Published',
    },
    {
        'title': 'Understanding HTML5 Semantic Elements',
        'short_description': 'Learn how to use HTML5 semantic elements to create well-structured and accessible web pages.',
        'slug': 'html5-semantic-elements',
        'category': 'HTML/CSS',
        'content': '''HTML5 introduced a set of semantic elements that help define the structure of a web page more meaningfully. These elements not only make your code more readable but also improve accessibility and SEO.

Semantic elements clearly describe their meaning to both the browser and the developer. For example, header, nav, main, article, section, aside, and footer are all semantic elements.

Using semantic HTML has several benefits:

1. Better accessibility: Screen readers use semantic elements to help visually impaired users navigate content.

2. Improved SEO: Search engines use semantic markup to understand the structure and relevance of content.

3. Cleaner code: Semantic elements make your HTML more readable and maintainable.

4. Future-proof: Following web standards ensures your site works across different browsers and devices.''',
        'status': 'Published',
    },
    {
        'title': 'Database Design Best Practices',
        'short_description': 'Learn the fundamentals of database design and how to structure your data efficiently.',
        'slug': 'database-design-best-practices',
        'category': 'Database',
        'content': '''Database design is a crucial aspect of software development. A well-designed database ensures data integrity, improves performance, and makes your application easier to maintain.

Here are some best practices to follow when designing your database:

1. Normalize your data: Break down your data into logical tables to reduce redundancy and improve data integrity.

2. Use appropriate data types: Choose the right data type for each column to optimize storage and performance.

3. Define primary and foreign keys: Establish relationships between tables using keys to maintain referential integrity.

4. Index strategically: Create indexes on columns that are frequently used in WHERE clauses and JOIN operations.

5. Plan for scalability: Design your schema with future growth in mind.

By following these practices, you will create databases that are efficient, maintainable, and scalable.''',
        'status': 'Published',
    },
    {
        'title': 'Introduction to REST APIs with Django REST Framework',
        'short_description': 'Build powerful and scalable REST APIs using Django REST Framework.',
        'slug': 'rest-apis-django-rest-framework',
        'category': 'API',
        'content': '''Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. It provides a set of tools and conventions that make it easy to build RESTful APIs.

Why use Django REST Framework?

1. Serialization: DRF makes it easy to convert complex data types like querysets and model instances into JSON.

2. Authentication: Built-in support for various authentication methods including token auth and session auth.

3. Viewsets and Routers: DRF provides high-level abstractions that reduce boilerplate code.

4. Browsable API: DRF generates a human-friendly HTML interface for your APIs.

5. Documentation: DRF integrates well with tools like Swagger and ReDoc for API documentation.

Getting started with DRF is straightforward. Install it with pip, add it to your INSTALLED_APPS, and start building your API endpoints.''',
        'status': 'Published',
    },
]


class Command(BaseCommand):
    help = 'Seed the database with sample blog posts and a superuser'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Seeding database...'))

        # ── Create superuser ──
        SUPERUSER_EMAIL = 'admin@deepverselab.com'
        SUPERUSER_PASSWORD = 'admin123'

        user, created = User.objects.get_or_create(
            email=SUPERUSER_EMAIL,
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
        )
        if created:
            user.set_password(SUPERUSER_PASSWORD)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser created: {SUPERUSER_EMAIL} / {SUPERUSER_PASSWORD}'))
        else:
            self.stdout.write(f'Superuser already exists: {SUPERUSER_EMAIL}')

        # ── Create categories ──
        category_map = {}
        for cat_name in CATEGORIES:
            cat, created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': cat_name.lower().replace('/', '').replace(' ', '-')},
            )
            category_map[cat_name] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category created: {cat_name}'))

        # ── Create blog posts ──
        for data in BLOG_POSTS:
            cat_name = data.pop('category', None)
            obj, created = Blog.objects.get_or_create(
                slug=data['slug'],
                defaults=data,
            )
            if cat_name and obj.category != category_map.get(cat_name):
                obj.category = category_map.get(cat_name)
                obj.save()
            if created:
                self.stdout.write(self.style.SUCCESS(f'Blog created: {data["title"]}'))
            else:
                self.stdout.write(f'Blog already exists: {data["title"]}')

        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
