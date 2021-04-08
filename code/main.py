from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import StringProperty
import sqlite3

con = sqlite3.connect("recipedb.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS RECIPES
                (id INTEGER PRIMARY KEY, recipe text, ingredients text)''')

# cur.execute('''INSERT INTO RECIPES(recipe, ingredients)
# VALUES('toast', 'like..toasted bread?')''')
# cur.execute('''INSERT INTO RECIPES(recipe, ingredients)
# VALUES('pizza', 'sauce bread and cheese')''')
# cur.execute('''INSERT INTO RECIPES(recipe, ingredients)
# VALUES('pasta', 'just boil pasta?')''')
#cur.execute('''INSERT INTO RECIPES(recipe, ingredients) VALUES ('risotto', 'risotto rice')''')

#con.commit()

class custom_list_item(OneLineListItem):
    text = StringProperty()
    printmsg = StringProperty()


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
                custom_list_item(text=f"{print_data}", printmsg=f"{print_data} worked")
            ) 


    def add_to_list(self):
        pass



if __name__ == '__main__':
    MainApp().run()