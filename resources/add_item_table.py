import sqlite3
import sys
import re

in_file = sys.argv[1]
out_file = sys.argv[2]

#Read from the mined database
con_read = sqlite3.connect(in_file)
cur_read = con_read.cursor()
cur_read.execute("select idx, refund, en_us, filename from items, localized_texts, icons where items.id == localized_texts.idx and localized_texts.tbl_name == 'items' and localized_texts.tbl_column_name == 'name' and items.icon_id == icons.id and not en_us == '' order by idx")
out_rows = cur_read.fetchall()

con_out = sqlite3.connect(out_file)
cur_out = con_out.cursor()

#Check if the items table exists, if it does, remove it
cur_out.execute("drop table if exists items")
cur_out.execute("create table items(item_id Int, price Int, name Text, description Text, filename Text);")

#Fill our DB with items from an extracted ArcheAge DB
for row in out_rows:
    cur_out.execute("insert into items (item_id, price, name, description, filename) values (?,?,?,?,?)", (row[0], row[1], row[2], '', row[3].replace('.dds', '.png')))
con_out.commit()

#Fill the item DB with the item descriptions
cur_read.execute("select idx, refund, en_us from items, localized_texts where items.id == localized_texts.idx and localized_texts.tbl_name == 'items' and localized_texts.tbl_column_name == 'description' and not en_us == '' order by idx")
out_rows = cur_read.fetchall()
for row in out_rows:
    description = row[2]
    clean_description = re.sub(r'\|c(.{8})(.*?)\|r', r'\2', description)
    clean_description = re.sub(r'\|nc;(.*?)\|r', r'\1', clean_description)
    clean_description = re.sub(r'\|nd;(.*?)\|r', r'\1', clean_description)
    clean_description = re.sub(r'\|ni;(.*?)\|r', r'\1', clean_description)
    clean_description = re.sub(r'\|nn;(.*?)\|r', r'\1', clean_description)
    clean_description = re.sub(r'\|nr;(.*?)\|r', r'\1', clean_description)
    clean_description = re.sub(r'\|ng;(.*?)\|r', r'\1', clean_description)
    cur_out.execute("update items set description=? where item_id=?", (clean_description, row[0]))

    con_out.commit()
