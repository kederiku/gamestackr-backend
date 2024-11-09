import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker


@pytest.fixture
def faker_account(db):
    return baker.make(
        get_user_model(),
        username='Faker',
        email='faker@example.com',
        # The hash stands for: pass1234
        # Using hash makes tests much faster
        password='pbkdf2_sha256$600000$xtoVMXq0IfPVEH9OUp5zsL$QCNMq3hD+3vRP641TsIilSmOf4agkjOx/VHTbH6nU0o=',
    )


@pytest.fixture
def ia_account(db):
    return baker.make(get_user_model(), email='ia@example.com', username='IA')
