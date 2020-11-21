import json

from mainapp.models import DealsOfTheWeek


img_path_template = r"related_products_images/{}"
related_products = []

with open(r"data/mainapp/related_products.json", encoding="utf-8") as f:
    data = f.read()
    json_data = json.loads(data)

for prod in json_data.get("related_products"):
    url = prod.get("page_link")
    image_name = prod.get("image_path").split(r"/")[-1]
    image_path = img_path_template.format(image_name)
    price = prod.get("price")
    name = prod.get("description")
    new_deal = DealsOfTheWeek(name=name, image=image_path, price=price, url=url)
    related_products.append(new_deal)

for i in related_products:
    i.save()
