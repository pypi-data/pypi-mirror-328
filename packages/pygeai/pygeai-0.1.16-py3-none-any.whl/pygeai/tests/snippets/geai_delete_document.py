from pygeai.core.managers import Geai

manager = Geai()

response = manager.delete_document(
    name="Test-Profile-WelcomeData-4",
    document_id="ce6f779e-329d-4e39-b84f-07a77265ff02"
)
print(response)
