# Movie API (Django + JWT)

A secure REST API to manage personal movie collections.

---

## Features
- User registration & login (JWT)
- Create, read, update, delete **your own** movies
- Filter movies: `?ids=1,2,3`
- Sample data with 2 users + 4 movies

---

## Endpoints

| Method | URL | Auth |
|--------|-----|------|
| POST | `/api/auth/register/` | No 
| POST | `/api/auth/login/` | No |
| POST | `/api/movies/` | Yes |
| GET  | `/api/movies/` | Yes |
| GET  | `/api/movies/?ids=1,2` | Yes |
| PUT  | `/api/movies_put/<int:id>/ ` | Yes |
| DELETE | `/api/movies_delete/<int:id>/` | Yes |

---

## Setup

```bash
# 1. Activate env
env\Scripts\activate

# 2. Install
pip install -r requirements.txt

# 3. Migrate
python manage.py migrate

# 4. Seed data
python seed_data.py