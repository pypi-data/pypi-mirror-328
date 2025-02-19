from pygeai.core.managers import Geai

manager = Geai()

response = manager.get_document_list(name="Test-Profile-WelcomeData-4")
print(response)