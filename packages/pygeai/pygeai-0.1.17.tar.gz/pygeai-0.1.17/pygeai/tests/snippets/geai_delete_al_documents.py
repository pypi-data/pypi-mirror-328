from pygeai.core.managers import Geai

manager = Geai()

response = manager.delete_all_documents(name="Test-Profile-WelcomeData-3")
print(response)