# 1-mashq
class PaymentService:
    def pay(self, user, amount):
        print(f"{user} paid {amount}")
# 2-mashq
class AppService:
    def __init__(self, repo):
        self.repo = repo

    def create(self, item):
        self.repo.add(item)
# 3-mashq
import unittest

class Test:
    def add(self, a, b):
        return a + b

class MyTest(unittest.TestCase):
    def test_add(self):
        t = Test()
        self.assertEqual(t.add(2,3), 5)
# 4-mashq
class FakeRepo:
    def add(self, x):
        print("Fake save")
# 5-mashq
class Locator:
    services = {}

    @classmethod
    def register(cls, name, obj):
        cls.services[name] = obj

    @classmethod
    def get(cls, name):
        return cls.services.get(name)
