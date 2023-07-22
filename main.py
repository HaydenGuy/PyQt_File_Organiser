import sys, shutil
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from UI.file_organiser_ui import Ui_file_organiser
from Widgets.add_file_type import AddFileType

class FileBrowser (QMainWindow, Ui_file_organiser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # counter used in the add_file_type method
        self.checkbox_counter = 0

        # Initialises an empty file filter variable that will be used to determine what files to show
        self.file_filter = ''

        # if the add button is clicked it will allow the user to add a file type for the filter
        self.pb_add.clicked.connect(self.add_file_type)

        # if the browse button is clicked it will run the browse file method
        self.pb_browse.clicked.connect(self.browse_file)

        # if the organise button is clicked it will run the organise file method
        self.pb_organise.clicked.connect(self.organise_file)

        # creates a list of the checkbox widgets which we can add more to
        self.checkboxes = [self.cb_mp3, self.cb_wav, self.cb_pdf, self.cb_txt, self.cb_png, self.cb_jpg, self.cb_mp4, self.cb_mov]

        # if any of the checkboxes are checked it will run the check_states method
        self.cb_mp3.stateChanged.connect(self.check_states)
        self.cb_wav.stateChanged.connect(self.check_states)
        self.cb_pdf.stateChanged.connect(self.check_states)
        self.cb_txt.stateChanged.connect(self.check_states)
        self.cb_png.stateChanged.connect(self.check_states)
        self.cb_jpg.stateChanged.connect(self.check_states)
        self.cb_mp4.stateChanged.connect(self.check_states)
        self.cb_mov.stateChanged.connect(self.check_states)

    '''
        Initialises a new AddFileType object
        executes the add_file_type code
    '''
    def add_file_type(self):
        self.user_checkbox = AddFileType()
        self.user_checkbox.exec()

        # initialise a new checkbox from the AddFileType object
        new_checkbox = self.user_checkbox.new_checkbox

        # if the checkboxes added is an even number it adds to the top row, odd adds to the bottom
        if self.checkbox_counter % 2 == 0:
            self.hl_top.addWidget(new_checkbox)
        else:
            self.hl_bottom.addWidget(new_checkbox)

        # add 1 to the checkbox counter and add the new checkbox to the checkboxes list
        self.checkbox_counter += 1
        self.checkboxes.append(new_checkbox)

        # if the state changes for the new checkbox, run the check states method
        new_checkbox.stateChanged.connect(self.check_states)

    # allows the user to browse their system files and will show the file_filter files if any boxes are checked
    def browse_file(self):
        files = QFileDialog.getOpenFileNames(
            caption='Select a file', # shows what text appears at the top of the windw
            dir='Qt_File_Organiser/File_Folder', # initialises the directory we display
            filter=self.file_filter # uses the filter list to only show files of a certain type
        )
        self.files_list = files[:-1]

    # this will copy all the files in the files_list, as selected in browse_file, and move them into the selected folder
    def organise_file(self):
        # Open a file dialog to select or create a new folder
        folder_path = QFileDialog.getExistingDirectory(
            caption='Select a folder',  # Title of the window
            dir='Qt_File_Organiser/File_Folder',  # Initial directory displayed
            options=QFileDialog.ShowDirsOnly  # Show only directories, not files
        )

        if folder_path:
            for item in self.files_list:
                for path in item:
                    try:
                        shutil.copy(path, folder_path)
                    except shutil.SameFileError:
                        # Display a QMessageBox informing the user about the same file error
                        QMessageBox.warning(self, 'Same File', 'The file already exists in the destination folder.', QMessageBox.Ok)
                        # Optionally, you can break the loop here to stop copying further files if there's an error.
                        break

        # Open the newly created folder after the copying process
        url = QUrl.fromLocalFile(folder_path)
        QDesktopServices.openUrl(url)
                    
    def check_states(self):
        # This extracts the file extension from the checkbox text, and creates a filter string with a single element
        self.file_filter = ' '.join(['*' + checkbox.text().split('.')[-1] for checkbox in self.checkboxes if checkbox.isChecked()])

#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FileBrowser()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())