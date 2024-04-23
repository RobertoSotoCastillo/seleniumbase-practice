from builtins import enumerate

from page_objects.HomePage import HomePage

class MyTestClass(HomePage):

    def setUp(self):
        super().setUp()
        HomePage.open_page_max(self)

    def tearDown(self):
        super().tearDown()


    def test_aexplore_to_bottom(self):
        #scroleamos al bottom y comprobamos el texto del copy
       self.scroll_to_bottom()
       self.assert_text(self.expected_copyright,self.copyright_message)

    def test_botones_existentes(self):
        #contamos el total de botones y revisamos si estan todos los esperados
        buttons = HomePage.get_button_list(self)
        for x, button in enumerate(buttons):
            self.assertEqual(self.expected_links[x], button.text)

    def test_go_to_learn_more_page(self):
        #scrolear hasta elememento learn y esperar que sea visible
        self.scroll_to_element(self.learn_more_button)
        self.sleep(1)
        self.wait_for_element_clickable(self.learn_more_button, timeout=10)
        #dar clic en elemento
        self.click(self.learn_more_button)
        #cambbiar a la nueva pestaña
        self.switch_to_newest_window()
        #comprobar si la URL es la correcta
        self.assert_url(self.learn_more_url)

    def test_go_to_about_page(self):
        # scrolear hasta elememento learn y esperar que sea visible
        self.scroll_to_element(self.about_button)
        self.sleep(1)
        self.wait_for_element_clickable(self.about_button, timeout=10)
        # dar clic en elemento
        self.click(self.about_button)
        # cambbiar a la nueva pestaña
        self.switch_to_newest_window()
        # comprobar si la URL es la correcta
        self.assert_url(self.about_url)




if __name__ == "__main__":
    MyTestClass().test_basic()