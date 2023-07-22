from PySide6.QtWidgets import QDialog, QCheckBox

from UI.add_file_type_ui import Ui_add_file_type

'''
    A QDialog that appears when the user clicks add in the main file
    It gives the user the ability to enter text which can be used to add a file type to the filter
'''
class AddFileType (QDialog, Ui_add_file_type):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_text = ''

        self.pb_ok.clicked.connect(self.ok_button)
        self.pb_cancel.clicked.connect(self.cancel_button)

    '''
        Takes the users entered text and assigns it to a variable
        Creates a new checkbox
        Sets the checkbox name to the user input text for use in the filter
        Sets the checkbox text visual to the input text without the *
    '''
    def ok_button(self):
        self.user_text = self.le_user_input.text()
        self.new_checkbox = QCheckBox()
        self.new_checkbox.setObjectName(f'cb_{self.user_text[2:]}')
        self.new_checkbox.setText(f'{self.user_text[1:]}')
        self.accept()

    def cancel_button(self):
        self.reject()