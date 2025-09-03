# Sanjivini Medicare - Healthcare Website

A full-stack healthcare website built with Django, featuring user authentication, appointment booking, and Google Maps integration.

## 🏥 Features

- **Responsive Design**: Modern, mobile-friendly interface using Bootstrap 5
- **User Authentication**: Login, signup, and user dashboard
- **Appointment Booking**: Online appointment scheduling system
- **Google Maps Integration**: Interactive map showing hospital location
- **Admin Panel**: Django admin interface for managing appointments
- **Contact Forms**: Multiple contact options for patients
- **Healthcare Services**: Comprehensive service listings
- **Responsive Navigation**: Mobile-optimized navigation menu

## 🛠️ Tech Stack

- **Backend**: Django 4.2.7 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (default) / PostgreSQL (optional)
- **Maps**: Google Maps JavaScript API
- **Forms**: Django Crispy Forms with Bootstrap styling
- **Authentication**: Django built-in user authentication

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google Maps API key

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Annirudha1/medicare.git
cd medicare
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
```

**Note**: Replace `your-secret-key-here` with a secure Django secret key and `your-google-maps-api-key` with your actual Google Maps API key.

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

## 🌐 Google Maps API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Maps JavaScript API
4. Create credentials (API key)
5. Add the API key to your `.env` file
6. Restrict the API key to your domain for security

## 📁 Project Structure

```
medicare/
├── config/                 # Django project settings
│   ├── settings.py        # Main settings file
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── medicare/              # Main Django app
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── forms.py          # Form classes
│   ├── admin.py          # Admin configuration
│   ├── urls.py           # App URL patterns
│   └── context_processors.py # Context processors
├── templates/             # HTML templates
│   └── medicare/         # App-specific templates
│       ├── base.html     # Base template
│       ├── home.html     # Home page
│       ├── about.html    # About page
│       ├── services.html # Services page
│       ├── contact.html  # Contact page
│       ├── signup.html   # User registration
│       └── dashboard.html # User dashboard
├── static/                # Static files
│   ├── css/              # Stylesheets
│   │   └── style.css     # Custom CSS
│   ├── js/               # JavaScript files
│   │   └── main.js       # Main JavaScript
│   └── images/           # Image files
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔧 Configuration

### Database Configuration

The project uses SQLite by default. To use PostgreSQL:

1. Install PostgreSQL and psycopg2:
```bash
pip install psycopg2-binary
```

2. Update `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files

Static files are automatically collected to the `staticfiles/` directory. In production:

```bash
python manage.py collectstatic
```

## 🚀 Deployment

### Production Settings

1. Set `DEBUG=False` in your `.env` file
2. Update `ALLOWED_HOSTS` in `settings.py`
3. Use a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up HTTPS

### Environment Variables

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 📱 Pages

- **Home**: Landing page with hero section and service overview
- **About**: Information about the healthcare facility and team
- **Services**: Detailed service listings with appointment booking
- **Contact**: Contact information and Google Maps integration
- **Sign Up**: User registration form
- **Dashboard**: User dashboard with appointments and profile

## 🔐 Authentication

- User registration with email verification
- Login/logout functionality
- Password reset capabilities
- User dashboard with appointment management

## 📅 Appointment System

- Online appointment booking
- Date and time selection
- Service type specification
- User appointment history
- Admin appointment management

## 🗺️ Google Maps Features

- Interactive map showing hospital location
- Custom marker with hospital information
- Responsive map design
- Location-based services

## 🎨 Customization

### Styling

- Modify `static/css/style.css` for custom styles
- Update Bootstrap theme colors in CSS variables
- Customize component styles as needed

### Content

- Update hospital information in templates
- Modify service descriptions
- Change contact details and location

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 📊 Admin Interface

Access the admin interface at `/admin/` to:

- Manage user accounts
- View and edit appointments
- Monitor system usage
- Manage content

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

- Create an issue on GitHub
- Contact: info@sanjivinimedicare.com
- Emergency: +91-98765-43210

## 🔄 Updates

Keep your project updated:

```bash
git pull origin main
pip install -r requirements.txt
python manage.py migrate
```

## 📈 Performance Tips

- Use Django Debug Toolbar in development
- Optimize database queries
- Implement caching for static content
- Use CDN for external resources
- Optimize images and media files

## 🔒 Security Considerations

- Keep Django and dependencies updated
- Use HTTPS in production
- Implement proper user authentication
- Validate all form inputs
- Use environment variables for sensitive data
- Regular security audits

---

**Built with ❤️ for better healthcare**
