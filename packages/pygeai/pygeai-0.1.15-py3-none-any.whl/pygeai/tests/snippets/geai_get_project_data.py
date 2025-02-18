from pygeai.core.managers import Geai

client = Geai()


response = client.get_project_data("1956c032-3c66-4435-acb8-6a06e52f819f")
print(f"response: {response}")
