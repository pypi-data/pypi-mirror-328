from pygeai.core.managers import Geai

client = Geai()


response = client.delete_assistant(assistant_name="Test-Profile-WelcomeData-9")
print(f"response: {response}")
