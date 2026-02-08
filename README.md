Django Car Marketplace (Harwoods-Inspired UI)
----
A Django-based car marketplace web application inspired by the UX and visual design patterns of Harwoods.
This project focuses on building a realistic vehicle browsing experience with brand filtering, sorting, product detail pages, and a modern, responsive UI.

The goal of this project is to explore full-stack Django development alongside UX-driven front-end design, using real-world dealership patterns as reference.

🚗 Project Overview
---------
This application allows users to:

- Browse cars in a product grid

- Filter vehicles by brand, sale status, and price range

- Sort results by price or name

- View detailed product pages with gallery, pricing, finance placeholders, and specifications

- Navigate a Harwoods-style homepage with hero search and brand tiles

The project is still in active development and is intentionally structured to allow incremental feature additions (finance logic, authentication, checkout, etc.).

✨ Key Features
----------
Frontend / UX
-
- Harwoods-inspired layout and interaction patterns

- Responsive design (desktop & mobile)

- Custom product cards with:

  - Sale badges

  - Tags / features

  - Clear CTAs

- Sticky product detail summary panel

- Off-canvas filter panel and sort dropdown

- Brand tile navigation with logo support

Backend / Django
---
- Django models for:

   - Products

   - Brands (with slugs & logos)

   - Categories

   - Tags

   - Customers

   - Orders

- Brand-based filtering using URL query parameters

- Safe price filtering and sorting logic

- Optimized queryset usage (select_related, prefetch_related)

- Admin panel support for managing products and brands

🧱 Tech Stack
------------
- Backend: Django (Python)

- Frontend: Django Templates + Bootstrap 5

- Styling: Custom CSS (Harwoods-style components)

- Database: SQLite (development)

- Assets: Django static & media handling

📁 Project Structure (Simplified)
-----------
ecom/
├── manage.py
├── store/
│   ├── models.py        # Product, Brand, Category, Tag, Order models
│   ├── views.py         # Home, Cars, Product Detail views
│   ├── urls.py          # App routing
│   ├── admin.py         # Admin registrations
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── cars.html
│       ├── product.html
│       └── navbar.html
├── static/
│   ├── css/styles.css
│   └── assets/
└── media/
    └── uploads/

⚙️ Setup & Installation
---------
1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate   # Windows


3. Install dependencies

pip install django


4. Run migrations

python manage.py makemigrations
python manage.py migrate


5. Create a superuser

python manage.py createsuperuser


6. Start the development server

python manage.py runserver


7. Access the app

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

🧪 Current Limitations
---------
- Finance calculator values are placeholders

- Authentication is basic and not fully integrated into user flows

- No checkout or reservation logic yet

- Image gallery currently uses a single image per product

These are intentional and planned for later phases.

🔮 Planned Enhancements
------------
- Multi-image product galleries

- Real finance calculation logic

- User accounts & saved vehicles

- Reservation / checkout flow

- Improved mobile filtering UX

- Pagination & performance tuning

- Accessibility refinements

🎯 Learning Focus
--------------
This project is designed to strengthen skills in:

- Django MVC patterns

- Queryset optimization

- UX-driven frontend architecture

- Translating real-world websites into maintainable code

- Bridging design and engineering decisions

📜 License
----------
This project is for educational and portfolio purposes.
Harwoods is referenced strictly as a design inspiration, not an affiliated or reproduced product.
