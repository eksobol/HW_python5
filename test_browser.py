import os

from selene import browser, be, have


def test_add_browser():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    #заполняем параметры

    browser.element('#firstName').should(be.blank).type('Anna').press_enter()
    browser.element('#lastName').should(be.blank).type('Ivanova').press_enter()
    browser.element('#userEmail').should(be.blank).type('abc@ya.ru').press_enter()
    browser.element('label[for=gender-radio-2]').click()
    browser.element('#userNumber').should(be.blank).type('8111111111').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element("[value='7']").click()
    browser.element('.react-datepicker__year-select').click()
    browser.element("[value='2000']").click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('#subjectsInput').type('c')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="Chemistry"]').click()
    browser.element('label[for=hobbies-checkbox-1]').click()
    browser.element('label[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image.png'))
    browser.element('#currentAddress').should(be.blank).type('homeland').press_enter()
    browser.element('#state').click()
    browser.element('//*[text()="Uttar Pradesh"]').click()
    browser.element('#city').click()
    browser.element('//*[text()="Merrut"]').click()

    browser.element('#submit').click()

    # проверки

    browser.element('//table//td[contains(text(),"Student Name")]/../td[2]').should(have.text('Anna Ivanova'))
    browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text('abc@ya.ru'))
    browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.text('Female'))
    browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.text('8111111111'))
    browser.element('//table//td[contains(text(),"Date of Birth")]/../td[2]').should(have.text('08 August,2000'))
    browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text('Chemistry'))
    browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text('Sports, Music'))
    browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text('image.png'))
    browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text('homeland'))
    browser.element('//table//td[contains(text(),"State and City")]/../td[2]').should(have.text('Uttar Pradesh Merrut'))



    # browser.element('#submit').click()





