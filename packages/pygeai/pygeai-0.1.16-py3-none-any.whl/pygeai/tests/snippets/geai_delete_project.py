from pygeai.core.managers import Geai

client = Geai()


response = client.delete_project("b91a21f1-0e5f-4aaf-bef5-e3cefd029d87")
print(f"response: {response}")
