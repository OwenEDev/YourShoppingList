from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
import sqlite3

con = sqlite3.connect("recipedb.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS RECIPES
                (id INTEGER PRIMARY KEY, recipe text, ingredients text)''')

cur.execute('''CREATE TABLE IF NOT EXISTS SHOPPING_LIST
            (id INTEGER PRIMARY KEY, shopping_list text)''')
                

class custom_list_item(OneLineListItem):
    text = StringProperty()


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"


    def on_start(self):
        cur.execute('''SELECT recipe FROM RECIPES''')
        r_data = cur.fetchall() 
        r_rowcount = len(r_data) 

        for i in range(r_rowcount):

            string_data = str(r_data[i])
            print_data = string_data[2:-3]
            print(print_data)
            
            self.root.ids.recipe_list.add_widget(
                custom_list_item(text=f"{print_data}")
            ) 


    def add_to_list(self, text):

        item_text = text

        cur.execute('''SELECT ingredients FROM RECIPES WHERE recipe = ?''', 
        (item_text,))

        data_ingredients = cur.fetchone()
        
        data_ingredients_string = str(data_ingredients)

        data_ingredients_cut = data_ingredients_string[2:-3]

        data_ingredients_replace = data_ingredients_cut.replace("\\n", "\n")

        self.root.ids.shopping_list.text += f"\n{data_ingredients_replace}"

        print("added")

    def save_recipe(self, recipe_title, recipe_ingredients):
        
        data_recipe_title = recipe_title
        data_recipe_ingredients = recipe_ingredients
        
        cur.execute('''INSERT INTO RECIPES(recipe, ingredients)
        VALUES (?,?)''', (recipe_title, recipe_ingredients,))

        con.commit()

        print(recipe_title, recipe_ingredients)

    def delete_recipe(self, recipe_title):
        cur.execute('''DELETE FROM RECIPES WHERE recipe =?''', (recipe_title,))
        con.commit()

        print("deleted")

    def refresh_recipes(self):
        self.root.ids.recipe_list.clear_widgets()
        
        cur.execute('''SELECT recipe FROM RECIPES''')
        r_data = cur.fetchall() 
        r_rowcount = len(r_data) 

        for i in range(r_rowcount):

            string_data = str(r_data[i])
            print_data = string_data[2:-3]
            print(print_data)
            
            self.root.ids.recipe_list.add_widget(
                custom_list_item(text=f"{print_data}")
            ) 

    def save_shopping_list(self):
        pass


if __name__ == '__main__':
    MainApp().run()