import factory

from users.models import User

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)
    
    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
