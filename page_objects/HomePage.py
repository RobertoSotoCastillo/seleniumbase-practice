from seleniumbase import BaseCase
class HomePage(BaseCase):
    #General
    welcome_message = ".wp-block-heading"
    practice_buttons = ".wp-block-button__link"
    copyright_message = "//*[@class='copyright-text text-center']"
    expected_copyright = "© 2020-2024 - automateNow, LLC. All rights reserved."
    expected_links = ["JavaScript Delays", "Sliders", "Tables", "Ads", "Click Events", "Iframes", "Broken Images", "Form Fields", "Calendars", "Window Operations", "Gestures", "Spinners", "Carousels", "Accordions", "Popups", "Modals", "Hover", "File Download", "File Upload", "Broken Links"]
    url = "https://practice-automation.com/"

    #About Page
    about_button = "//*[contains(text(),'About')]"
    about_url = "https://automatenow.io/about/"

    #Learn More Page
    learn_more_button = "//*[contains(text(),'Learn More')]"
    learn_more_url = "https://linktr.ee/automateNow"


    def open_page_max(self):
        self.open(self.url)
        self.maximize_window()

    def get_button_list(self):
        self.wait_for_element_visible(self.practice_buttons)
        element_list = self.find_elements(self.practice_buttons)
        return element_list

