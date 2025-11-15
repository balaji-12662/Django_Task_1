import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieapi.settings')  
django.setup()

from django.contrib.auth import get_user_model
from movie.models import Movie  

User = get_user_model()

def seed():
    print("Starting seeding...")

    alice, created = User.objects.get_or_create(username='alice')
    if created:
        alice.set_password('alice123')
        alice.save()
        print("Created: alice")

    bob, created = User.objects.get_or_create(username='bob')
    if created:
        bob.set_password('bob123')
        bob.save()
        print("Created: bob")

    Movie.objects.get_or_create(
        title="The Matrix", owner=alice,
        defaults={'description': 'A computer hacker learns about reality.'}
    )
    Movie.objects.get_or_create(
        title="Inception", owner=alice,
        defaults={'description': 'A thief who steals secrets through dreams.'}
    )

    Movie.objects.get_or_create(
        title="Pulp Fiction", owner=bob,
        defaults={'description': 'Intertwined stories of crime.'}
    )
    Movie.objects.get_or_create(
        title="The Dark Knight", owner=bob,
        defaults={'description': 'Batman vs Joker.'}
    )

    print("Seeding completed!")

if __name__ == "__main__":
    seed()
