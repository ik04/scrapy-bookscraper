# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        field_names = adapter.field_names()  # very imp updated syntax
        # print(field_names)
        # removes whitespace
        for field_name in field_names:
            # print(field_name)
            if field_name != "description":
                value = adapter.get(field_name)
                print(value)
                adapter[field_name] = value.strip()  # !this bs
                # value = adapter.get(field_name)

        # to lower for some keys
        sanitize_to_lowercase = ["category", "product_type"]
        for lowercase_key in sanitize_to_lowercase:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        # typecast to float
        price_keys = ["price", "price_excl_tax", "price_incl_tax", "tax"]
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace("£", "")  # replaces pound with nothing
            adapter[price_key] = float(value)

        # sanitize availability to a number
        availability_string = adapter.get("availability")
        split_string_array = availability_string.split("(")
        if len(split_string_array) < 2:
            adapter["availability"] = 0
        else:
            availability_array = split_string_array[1].split(" ")
            adapter["availability"] = int(availability_array[0])

        num_reviews_string = adapter.get("num_reviews")
        adapter["num_reviews"] = int(num_reviews_string)

        stars_string = adapter.get("stars")
        split_stars_array = stars_string.split(" ")
        stars_text_value = split_stars_array[1].lower()

        if stars_text_value == "zero":
            adapter["stars"] = 0
        elif stars_text_value == "one":
            adapter["stars"] = 0
        elif stars_text_value == "two":
            adapter["stars"] = 0
        elif stars_text_value == "three":
            adapter["stars"] = 0
        elif stars_text_value == "four":
            adapter["stars"] = 0
        elif stars_text_value == "five":
            adapter["stars"] = 0

        return item


class CategoryScraperPipeline:
    pass
