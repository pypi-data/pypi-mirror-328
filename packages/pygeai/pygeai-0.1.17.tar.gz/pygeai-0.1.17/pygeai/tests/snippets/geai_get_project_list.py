from pygeai.core.managers import Geai

client = Geai()


response = client.get_project_list("full")
print(f"response: {response}")
