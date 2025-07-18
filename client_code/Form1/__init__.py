from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.current_row = None  # Tracks the row being edited
        self.refresh_clients()   # Load initial data

    def save_button_click(self, **event_args):
        """Handle add or update"""
        if self.current_row:
            # Update existing row
            self.current_row['name'] = self.text_name.text
            self.current_row['email'] = self.text_email.text
            self.current_row['mobile'] = self.text_mobile.text
            self.current_row = None
            self.save_button.text = "Add Client"
        else:
            # Add new row
            app_tables.clients.add_row(
                name=self.text_name.text,
                email=self.text_email.text,
                mobile=self.text_mobile.text
            )
        self.clear_inputs()
        self.refresh_clients()

    def clear_inputs(self):
        self.text_name.text = ""
        self.text_email.text = ""
        self.text_mobile.text = ""

    def refresh_clients(self):
        self.repeating_panel_1.items = app_tables.clients.search()
