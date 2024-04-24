from page_objects.FileUpload import FileUpload

class MyTestClass(FileUpload):

    def setUp(self):
        super().setUp()
        FileUpload.open_page_max(self)

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

#upload expected files
    def test_upload_small_jpg(self):
        self.upload_small_file(self.path_jpg)

    def test_upload_small_doc(self):
        self.upload_small_file(self.path_docx)

    def test_upload_small_gif(self):
        self.upload_small_file(self.path_gif)

    def test_upload_small_pdf(self):
        self.upload_small_file(self.path_pdf)

    def test_upload_small_png(self):
        self.upload_small_file(self.path_png)

    def test_upload_small_txt(self):
        self.upload_small_file(self.path_txt)

#negative
    def test_negative_upload_wrong_ext(self):
        #se intenta subir archivo .rar
        self.choose_file(self.file_element, self.path_rar)
        #se indica que es un archivo incorrecto
        self.assert_text(self.expected_not_allowed_message, self.not_allowed_message)

    def test_negative_upload_big_jpg(self):
        self.upload_big_file(self.path_jpg_BIG)

    def test_negative_upload_without_file(self):
        #se hace clic sin cargar nada
        self.click(self.upload_button)
        # se muestra mensaje solicitando se adjunte archivo
        self.assert_text(self.expected_fill_message, self.fill_message)
        # se muestra mensaje de error
        self.assert_text(self.expected_error_message, self.error_message)

#Otras Funcionalidades
    def test_navigate_to_home(self):
        #click en href que redirecciona a home
        self.click(self.ref_return_to_home)
        #validar estamos en la URL de home
        self.assert_url(self.home_url)

    def test_navigate_to_copyright(self):
        #scroll a bottom
        self.scroll_to_bottom()
        #revisamos que copyright se encuentre presente
        self.assert_text(self.expected_copy,self.copyright)