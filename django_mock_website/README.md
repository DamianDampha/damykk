# Django Mock Website

A complete Django project demonstrating a blog and portfolio website with a professional structure.

## Project Structure

```
django_mock_website/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── mysite/                   # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI application
└── blog/                    # Blog application
    ├── models.py            # Database models (Post, Category, Project)
    ├── views.py             # View logic
    ├── urls.py              # App URL routing
    ├── admin.py             # Django admin configuration
    ├── templates/           # HTML templates
    │   ├── base.html
    │   ├── blog/
    │   │   ├── home.html
    │   │   ├── post_list.html
    │   │   ├── post_detail.html
    │   │   ├── project_list.html
    │   │   ├── about.html
    │   │   └── contact.html
    └── static/              # Static files (CSS, JS, images)
```

## Features

- **Blog System**: Create and manage blog posts with categories
- **Portfolio**: Showcase your projects with descriptions and links
- **Categories**: Organize blog posts by category with filtering
- **Admin Interface**: Manage content through Django's built-in admin panel
- **Responsive Design**: Beautiful, modern UI that works on all devices
- **Related Posts**: Show related posts on individual post pages

## Models

### Category
- `name`: Category name (unique)
- `description`: Category description

### Post
- `title`: Post title
- `content`: Post content
- `author`: Author name
- `category`: Foreign key to Category
- `created_at`: Timestamp (auto-set)
- `updated_at`: Timestamp (auto-update)
- `published`: Boolean flag for publishing

### Project
- `title`: Project title
- `description`: Project description
- `technologies`: Technologies used (comma-separated)
- `link`: Project link
- `created_at`: Timestamp (auto-set)

## Views

- **home**: Homepage with featured posts and projects
- **post_list**: List all blog posts with category filtering
- **post_detail**: Display individual post with related posts
- **project_list**: Display all portfolio projects
- **about**: About page
- **contact**: Contact page with form

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Apply Migrations
```bash
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create a superuser account.

### 4. Run Development Server
```bash
python manage.py runserver
```

### 5. Access the Site
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Adding Sample Data

1. Log into the admin panel at `/admin/`
2. Create a Category (e.g., "Web Development", "Python")
3. Create Posts and Projects using the admin interface

## URLs

- `/` - Homepage
- `/posts/` - Blog posts list
- `/posts/<id>/` - Individual blog post
- `/projects/` - Portfolio projects
- `/about/` - About page
- `/contact/` - Contact page
- `/admin/` - Admin panel

## Customization

### Change Site Name
Edit the `<div class="logo">` in [base.html](blog/templates/base.html) or update site name in Django admin settings.

### Modify Colors
Edit the CSS in [base.html](blog/templates/base.html) - look for the gradient colors (e.g., `#667eea`, `#764ba2`)

### Add More Fields to Posts
Edit [models.py](blog/models.py), add new fields to the Post model, create a migration, and update templates.

## Example Data

Here's how to add sample data via the admin panel or shell:

```python
# Via Django shell: python manage.py shell
from blog.models import Category, Post, Project
from django.utils import timezone

# Create category
cat = Category.objects.create(name='Web Development', description='Web development tutorials')

# Create post
Post.objects.create(
    title='Getting Started with Django',
    content='Django is a powerful web framework...',
    author='John Doe',
    category=cat,
    published=True
)

# Create project
Project.objects.create(
    title='Personal Blog',
    description='A feature-rich blog built with Django',
    technologies='Django, PostgreSQL, HTML, CSS',
    link='https://example.com'
)
```

## Technologies Used

- **Django 4.2**: Web framework
- **SQLite**: Default database
- **HTML5 & CSS3**: Frontend
- **Python 3.8+**: Backend language

## License

Free to use for learning and development purposes.
