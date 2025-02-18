from pygeai.core.managers import Geai

client = Geai()


response = client.get_assistant_data(assistant_name="Test-Profile-WelcomeData-2")
print(f"response: {response}")
