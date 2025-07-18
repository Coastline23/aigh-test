from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def edit_button_click(self, **event_args):
        """Populate Form1 inputs for editing"""
        main_form = get_open_form()
        main_form.text_name.text = self.item['name']
        main_form.text_email.text = self.item['email']
        main_form.text_mobile.text = self.item['mobile']
        main_form.current_row = self.item
        main_form.save_button.text = "Update Client"

    def delete_button_click(self, **event_args):
        """Delete the row"""
        if confirm("Are you sure you want to delete this client?"):
            self.item.delete()
            get_open_form().refresh_clients()

    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""
        pass
