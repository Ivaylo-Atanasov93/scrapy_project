The project is made to collect data from two of the main categories on https://gplay.bg/.

The script is collecting the following information *If the price is bellow 200.00lv. and the product is in stock*:

1. Category
2. Subcategory
3. Title
4. Subtitle
5. Product number
6. Price


How the script works.

The scripts has two start links, each of them for differenet category.
Collects all the links for subcategories, after that collects all the products
following the pages ahead.

After that it runs every single collected link and if the verification passes it
collects the required information.

All the information is stored in SQLite database, and every time when we run the
script it drops the old table, then creating a new one.

*How to use the project*
Innitial requirements:

You'll need preinstalled Python on you device.

If you don't have Python on your computer you can check this tutorial: https://www.youtube.com/watch?v=UvcQlPZ8ecA&t=8s (Download the latest version of Python available)

Since you have Python installed on your computer, you will have to clone this repository to a local repository on your machine. If you don't know how to do that you can follow this tutorial here: https://www.youtube.com/watch?v=CKcqniGu3tA

After you have Python installed and the project is on your computer you need to open your Command Prompt (Windows) or Linux Terminal.
Navigate to the main folder of the project (the one with the requirements.txt in it).
Run "pip install requirements.txt" command - This will install everything that you need to run the project on your computer.

To run the project run "scrapy crawl spider_gplay".

To see the collected information the easiest way is to go to: https://sqliteonline.com/
Select "File" (top left corner), then "Open DB", navigate to your project folder where the requirements.txt file is and select the gplay_items file.
Upload the file, double click the table with the name gplay_items and you can see your information.
