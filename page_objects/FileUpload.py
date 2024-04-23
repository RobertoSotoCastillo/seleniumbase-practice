from seleniumbase import BaseCase
#--html=report.html
#--dashboard
#-n3
#--headless
#--browser=firefox
class FileUpload(BaseCase):

    #URL
    url = "https://practice-automation.com/file-upload/"
    home_url = "https://practice-automation.com/"

    #selectors
    page_header = "//h1[contains(text(),'File Upload')]"
    file_element = "//*[@type='file']"
    upload_button = "//*[@id='upload-btn']"
    fill_message = "//span[contains(text(),'Please fill out this field.')]"
    copyright = "//*[@id='copyright']//div//div"
    ref_return_to_home = "//a[contains(text(),'Home')]"
    error_message = "//div[contains(text(),'One or more fields have an error. Please check and try again.')]"
    to_big_message = "//span[contains(text(),'Uploaded file is too big.')]"
    successful_message = "//div[contains(text(),'There was an error trying to send your message. Please try again later.')]"
    not_allowed_message = "//span[contains(text(),'You are not allowed to upload files of this type.')]"

    #messages
    expected_copy = "© 2020-2024 - automateNow, LLC. All rights reserved."
    expected_fill_message = "Please fill out this field."
    expected_error_message ="One or more fields have an error. Please check and try again."
    expected_to_big_message = "Uploaded file is too big."
    expected_successful_message = "There was an error trying to send your message. Please try again later."
    expected_not_allowed_message = "You are not allowed to upload files of this type."

    #documents paths
    path_txt='./page_objects/files/FileUpload/txt auto.txt'
    path_rar='./page_objects/files/FileUpload/rar auto.rar'
    path_png='./page_objects/files/FileUpload/png auto.png'
    path_jpg='./page_objects/files/FileUpload/jpeg auto.jpg'
    path_jpg_BIG='./page_objects/files/FileUpload/big jpg auto.jpg'
    path_gif='./page_objects/files/FileUpload/gif auto.gif'
    path_docx='./page_objects/files/FileUpload/docx auto.docx'
    path_pdf='./page_objects/files/FileUpload/pdf auto.pdf'

    def open_page_max(self):
        self.open(self.url)
        self.maximize_window()

    def upload_small_file(self, path):
        #se selecciona el archivo del path
        self.choose_file(self.file_element, path)
        #se presiona upload
        self.click(self.upload_button)
        #se muestra mensaje de exito
        self.assert_text(self.expected_successful_message, self.successful_message)

    def upload_big_file(self, path):
        #se selecciona el archivo del path
        self.choose_file(self.file_element, path)
        #se indica que es demasiado grande el archivo.
        self.assert_text(self.expected_to_big_message, self.to_big_message)
        #Se presiona upload y error al intentar subir.
        self.click(self.upload_button)
        self.assert_text(self.expected_error_message, self.error_message)

