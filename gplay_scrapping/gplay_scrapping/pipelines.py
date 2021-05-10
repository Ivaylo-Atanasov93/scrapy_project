# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class GplayScrappingPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("gplay_items.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS gplay_items""")
        self.cursor.execute('''create table gplay_items(
                        cateogory text,
                        subcategory text,
                        title text,
                        subtitle text,
                        product_number text,
                        price REAL
                        )''')

    def process_item(self, item, spider):
        # TODO Json schema
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("""insert into gplay_items values (?, ?, ?, ?, ?, ?)""", (
            item['category'],
            item['subcategory'],
            item['title'],
            item['subtitle'],
            item['product_number'],
            item['price']
        ))
        self.connection.commit()
