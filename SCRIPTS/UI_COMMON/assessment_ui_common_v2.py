import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# from selenium.webdriver.common.keys import Keys


# from selenium.common.exceptions import TimeoutException


class AssessmentUICommon:

    def __init__(self):
        self.delay = 120
        print("This is Latest Version of UI Code")

    def initiate_browser(self, url, path):
        # chrome option is needed in VET cases - ( its handling permissions like mic access)
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver

    def ui_login_to_test(self, user_name, password):
        # time.sleep(8)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, 'loginUsername').clear()
        self.driver.find_element(By.NAME, 'loginUsername').send_keys(user_name)
        self.driver.find_element(By.NAME, 'loginPassword').clear()
        self.driver.find_element(By.NAME, 'loginPassword').send_keys(password)
        self.driver.find_element(By.NAME, 'btnLogin').click()
        # time.sleep(5)
        login_status = "None"
        try:
            if self.driver.find_element(By.XPATH,
                                        '//div[@class="text-center login-error ng-binding ng-scope"]').is_displayed():
                print("Unable to Login ")
                # time.sleep(2)
                self.driver.implicitly_wait(2)
                error_message = self.driver.find_element(By.XPATH,
                                                         '//div[@class="text-center login-error ng-binding ng-scope"]').text
                login_status = error_message
        except Exception as e:
            print(e)
            login_status = 'SUCCESS'
        return login_status

    def select_i_agree(self):
        try:
            # time.sleep(1)
            i_agree_status = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'chk')))
            is_selected = i_agree_status.is_selected()
            if not is_selected:
                i_agree_status.click()
                is_selected = True
            return is_selected

        except Exception as e:
            print("I agree is not visible")
            print(e)

    def select_answer_for_the_question(self, answer):
        # time.sleep(1)
        value = "//input[@name='answerOptions' and @value='%s']" % answer
        answered = self.driver.find_element(By.XPATH, value)
        is_answered = answered.is_selected()
        if not is_answered:
            answered.click()

    def select_answer_for_mca_question(self, answer):
        # If user wants to select one or more options then If condition will work other wise else will pass the stmt.
        if answer:
            # user can choose n number of options, options be passed as string and comma separated
            # below split will split the string by using comma and will make a list.
            answer_choices = answer.split(',')
            for options in answer_choices:
                # strip is necessary to remove the leading and trailing space of each option.
                options = options.strip()
                # elem = self.driver.find_element_by_xpath('//*[@id="option2"]')
                value = '//*[@id="%s"]' % options
                elem = self.driver.find_element_by_xpath(value)
                self.driver.implicitly_wait(10)
                ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        else:
            # User does not want to select any option, so pass the stmt.
            pass

    def check_answered_status(self, previous_answer):
        value = "//input[@name='answerOptions' and @value='%s']" % previous_answer
        answered = self.driver.find_element(By.XPATH, value).is_enabled()
        return answered

    def next_question(self, question_index):
        # time.sleep(1)
        value = "btnQuestionIndex%s" % str(question_index)
        self.driver.find_element(By.NAME, value).click()

    def start_test_button_status(self):
        # time.sleep(1)
        is_enabled = self.driver.find_element(By.NAME, 'btnStartTest').is_enabled()
        if is_enabled:
            start_button_status = 'Enabled'
        else:
            start_button_status = 'Disabled'
        return start_button_status

    def start_test(self):
        # time.sleep(1)
        self.driver.find_element(By.NAME, 'btnStartTest').click()

    def check_security_key_model_window_availability(self):
        status = 'Success'
        try:
            if self.driver.find_element(By.NAME, 'securityKey').is_displayed():
                print("Security page is displayed")
                status = "Success"
        except Exception as e:
            print(e)
            status = 'Failed'
        return status

    def validate_security_key(self, secure_password):
        self.driver.find_element(By.NAME, 'securityKey').send_keys(secure_password)
        self.driver.find_element(By.XPATH, '//button[text()="Verify"]').click()
        time.sleep(3)

    def end_test(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger ng-scope']").click()

    def end_test_confirmation(self):
        try:
            time.sleep(5)
            self.driver.find_element(By.NAME, 'btnCloseTest').click()
            print("Test is ended Successfully")
        except Exception as e:
            print(e)

    def unanswer_question(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btnUnanswer ng-scope']").click()
        print("Un Answer Succeded")

    def find_question_string(self):
        question_string = self.driver.find_element(By.NAME, 'questionHtmlString').text
        print(question_string)
        return question_string

    def find_question_string_v2(self):
        question_string = self.driver.find_element(By.NAME, 'questionHtmlString').text
        groupname = self.driver.find_element(By.NAME, 'groupName').text
        section_name = self.driver.find_element(By.NAME, 'sectionName').text
        return question_string, groupname, section_name

    def find_question_string_for_rtc(self):
        parent_question_string = self.driver.find_element(By.NAME, 'questionParentHtmlString').text
        child_question_string = self.driver.find_element(By.NAME, 'questionHtmlString').text
        groupname = self.driver.find_element(By.NAME, 'groupName').text
        section_name = self.driver.find_element(By.NAME, 'sectionName').text
        return parent_question_string, child_question_string, groupname, section_name

    def rejection_page(self):
        print("This is Rejected Method")
        data = {}
        try:
            if self.driver.find_element(By.NAME, 'nextTestMsg').is_displayed():
                message = self.driver.find_element(By.NAME, 'nextTestMsg').text
                overall_page_message = self.driver.find_element(By.XPATH, "//*[@class='ng-scope']").text
                data = {'is_next_test_available': 'Not Available', 'is_shortlisted': 'Rejected',
                        'message': message, 'consent_yes': 'EMPTY', 'consent_no': 'EMPTY',
                        'consent_paragraph': 'EMPTY', 'next_test_page_message': overall_page_message,
                        'retest_required': False}

        except Exception as e:
            print(e)
            message = "shortlisting not available"
            data = {'is_next_test_available': 'EXCEPTION OCCURRED', 'is_shortlisted': 'EXCEPTION OCCURRED',
                    'message': message, 'consent_yes': 'EXCEPTION OCCURRED', 'consent_no': 'EXCEPTION OCCURRED',
                    'consent_paragraph': 'EXCEPTION OCCURRED', 'next_test_page_message': 'EXCEPTION OCCURRED',
                    'retest_required': False}
        return data

    def shortlisting_page(self):
        data = {}
        try:
            if self.driver.find_element(By.NAME, 'btnStartNextTest').is_displayed():
                overall_page_message = self.driver.find_element(By.XPATH, "//*[@class='ng-scope']").text
                button_message = self.driver.find_element(By.NAME, 'btnStartNextTest').text
                print("This is button message")
                print(button_message)
                if button_message == 'Yes, Request for Retest':
                    data = {'is_next_test_available': 'Not Available', 'is_shortlisted': 'Retest Case',
                            'message': 'EMPTY', 'consent_yes': 'EMPTY', 'consent_no': 'EMPTY',
                            'consent_paragraph': 'EMPTY', 'next_test_page_message': overall_page_message,
                            'retest_required': True}
                else:
                    next_test_message = self.driver.find_element(By.NAME, 'nextTestMsg').text
                    if button_message == 'Yes, Take me to the next test':
                        consent_message = self.driver.find_element(By.XPATH, "//*[@class='next-msg ng-scope']").text
                        consent_yes = self.driver.find_element(By.XPATH, "//*[@class='btn btn-success btn-yes']").text
                        consent_no = self.driver.find_element(By.XPATH, "//*[@class='btn btn-default red-button']").text
                        data = {'is_next_test_available': 'Available', 'is_shortlisted': 'Shortlisted with Consent',
                                'message': next_test_message, 'consent_yes': consent_yes, 'consent_no': consent_no,
                                'consent_paragraph': consent_message, 'next_test_page_message': overall_page_message,
                                'retest_required': False}
                    else:
                        if next_test_message == 'We have another test lined up for you.':
                            data = {'is_next_test_available': 'Available', 'is_shortlisted': 'Autotest',
                                    'message': next_test_message, 'consent_yes': 'EMPTY', 'consent_no': 'EMPTY',
                                    'consent_paragraph': 'EMPTY', 'next_test_page_message': overall_page_message,
                                    'retest_required': False}
                        elif next_test_message == 'Congratulations! You are eligible for the next test.':
                            data = {'is_next_test_available': 'Available', 'is_shortlisted': 'Shortlisted',
                                    'message': next_test_message, 'consent_yes': 'EMPTY', 'consent_no': 'EMPTY',
                                    'consent_paragraph': 'EMPTY', 'next_test_page_message': overall_page_message,
                                    'retest_required': False}
                        else:
                            data = {'is_next_test_available': 'Available', 'is_shortlisted': 'DEBUG',
                                    'message': next_test_message, 'consent_yes': 'DEBUG', 'consent_no': 'DEBUG',
                                    'consent_paragraph': 'DEBUG', 'next_test_page_message': overall_page_message,
                                    'retest_required': False}
        except Exception as e:
            print(e)
            next_test_message = "Shortlisting Not Available"
            data = {'is_next_test_available': 'EXCEPTION OCCURRED', 'is_shortlisted': 'EXCEPTION OCCURRED',
                    'message': next_test_message, 'consent_yes': 'EXCEPTION OCCURRED',
                    'consent_no': 'EXCEPTION OCCURRED', 'consent_paragraph': 'EXCEPTION OCCURRED',
                    'next_test_page_message': 'EXCEPTION OCCURRED', 'retest_required': False}
            print("This is Shortlist method")
        print(data)
        return data

    def start_next_test(self):
        self.driver.find_element(By.NAME, 'btnStartNextTest').click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[2])

    def consent_no(self):
        self.driver.find_element(By.XPATH, "//*[@class='btn btn-default red-button']").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[2])

    def vet_start_test(self):
        time.sleep(5)
        try:
            self.driver.switch_to.frame('thirdPartyIframe')
            self.driver.find_element(By.XPATH, "//*[@class='wdtContextualItem  wdtContextStart']").click()
            print("VET Test is started Successfully")
            vet_test_started = "Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("VET Start test is failed")
            is_element_successful = False
            vet_test_started = "Failed"
        return vet_test_started, is_element_successful

    def vet_welcome_page(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.ID, 'welcome_next_link').click()
            print("Welcome Page")
            vet_welcome_page = "Successful"
            is_element_successful = True
        except Exception as e:
            print(e)
            print("Failed in Welcome Page")
            is_element_successful = False
            vet_welcome_page = "Failed"

        return vet_welcome_page, is_element_successful

    def vet_quiet_please(self):
        time.sleep(10)
        try:
            self.driver.find_element(By.ID, 'distraction_next_link').click()
            print("Quiet Please Page")
            vet_quiet_please_page = "Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Welcome Page successful")
            vet_quiet_please_page = "Failed"
            is_element_successful = False

        return vet_quiet_please_page, is_element_successful

    def vet_ready_check_box(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.ID, 'ready_checkbox').click()
            print("Ready Check Box successfull")
            vet_ready_check_box = "Successful"
            is_element_successful = True
        except Exception as e:
            print(e)
            print("Ready Check Box Failed")
            vet_ready_check_box = "Failed"
            is_element_successful = False

        return vet_ready_check_box, is_element_successful

    def vet_ready_start_link(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.ID, 'ready_start_link').click()
            print("Ready Start Successful")
            vet_ready_check_box = "Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("vet_ready_start_link Failed")
            vet_ready_check_box = "Failed"
            is_element_successful = False
        return vet_ready_check_box, is_element_successful

    def vet_proceed_test(self):
        time.sleep(30)
        try:
            self.driver.find_element(By.XPATH, "//*[@class = 'proceed wizardButton greenBackground']").click()
            print("Proceed Test Successful")
            time.sleep(25)
            os.system("F:\\my_test.mp3")
            vet_proceed_test = "Successful"
            is_element_successful = True
            time.sleep(5)
        except Exception as e:
            print(e)
            print("vet_ready_start_link Failed")
            vet_proceed_test = "Failed"
            is_element_successful = False
        return vet_proceed_test, is_element_successful

    def vet_speaking_tips(self):
        try:
            time.sleep(120)
            self.driver.find_element(By.XPATH, "//*[@class='testInstructionItem testInstructionNext']").click()
            print("Speaking Tips Successful")
            vet_speaking_tips = "Successful"
            is_element_successful = False

        except Exception as e:
            print(e)
            print("vet_speaking_tips Failed")
            vet_speaking_tips = "Failed"
            is_element_successful = False

        return vet_speaking_tips, is_element_successful

    def vet_overview(self):
        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//*[@class='wdtContextualItem  wdtContextNext']").click()
            print("Overview Page Success")
            vet_overview = "Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("vet_speaking_tips Failed")
            vet_overview = "Failed"
            is_element_successful = False

        return vet_overview, is_element_successful

    def vet_instruction(self):
        time.sleep(10)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='wdtContextualItem wdtContextNext']").click()
            print("VET Instructions Page Success")
            vet_instruction = "Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("VET Instructions Failed")
            vet_instruction = "Failed"
            is_element_successful = False

        return vet_instruction, is_element_successful

    def play_audio(self):
        os.system("F:\\my_test.mp3")

    def survey_submit(self):
        time.sleep(60)
        try:
            if self.driver.find_element(By.XPATH,
                                        "//*[@class = 'wdtContextualItem  wdtContextNext']").is_displayed():
                self.driver.find_element(By.XPATH, "//*[@class = 'wdtContextualItem  wdtContextNext']").click()
                print("survey Question Success")
            survey_submit = "Successful"
            is_element_successful = True
        except Exception as e:
            print(e)
            print("survey Question  Failed")
            survey_submit = "Failed"
            is_element_successful = False
        return survey_submit, is_element_successful

    def vet_retest(self, retest_consent):
        time.sleep(60)
        try:
            if retest_consent == 'Yes, Request for Retest':
                self.driver.find_element(By.XPATH, "//*[@class='btn btn-success']").click()
            else:
                self.driver.find_element(By.XPATH, "//*[@class='btn btn-default']").click()
                print("VET Retest Success")
            vet_retest = "Retest Consent Success"
            is_element_successful = True
        except Exception as e:
            print(e)
            print("VET Retest Failed")
            vet_retest = "Retest Consent Failed"
            is_element_successful = False
        return vet_retest, is_element_successful

    def cocubes_disclaimer(self):
        time.sleep(5)
        try:
            self.driver.switch_to.frame('thirdPartyIframe')
            self.driver.find_element(By.XPATH, "//*[@class='btn-primary mid-size accept']").click()
            print("Cocubes disclaimer is Accepted")
            cocubes_disclaimer = "Disclaimer Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Cocubes Disclaimer is failed")
            is_element_successful = False
            cocubes_disclaimer = "Disclaimer Failed"
        return cocubes_disclaimer, is_element_successful

    def cocubes_start_test(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='start-test btn-primary']").click()
            print("Cocubes Test is Started")
            cocubes_start_test = "Start test Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Cocubes test is not Started")
            is_element_successful = False
            cocubes_start_test = "Start test Failed"
        return cocubes_start_test, is_element_successful

    def cocubes_group_names(self, title):
        time.sleep(5)
        title = "//*[@title='%s']" % title
        try:
            cocubes_group_names = self.driver.find_element(By.XPATH, title).text
            print("Group name is Succeded")
            # cocubes_group_names = "Agreed"
            print(cocubes_group_names)
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Group name is Failed")
            is_element_successful = False
            cocubes_group_names = "Failed"
        return cocubes_group_names, is_element_successful

    def cocubes_answer_question(self, position):
        time.sleep(1)
        try:
            element = "//*[@name='%s']" % position
            self.driver.find_element(By.XPATH, element).click()
            print("Answer is Succeded")
            cocubes_question_answer = "Answered Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Answer is Failed")
            is_element_successful = False
            cocubes_question_answer = "Answered Failed"
        return cocubes_question_answer, is_element_successful

    def cocubes_next_group(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='btn-primary next-btn btn-light-blue']").click()
            print("Next group is Succeded")
            cocubes_next_group = "Next group success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Next group is Failed")
            is_element_successful = False
            cocubes_next_group = "Next group failed"
        return cocubes_next_group, is_element_successful

    def cocubes_submit_test(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='btn-primary btn-primary-submit submit-btn']").click()
            print("Test is submitted")
            cocubes_next_group = "Submission Successful"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Test is not submitted")
            is_element_successful = False
            cocubes_next_group = "Submission Failed"
        return cocubes_next_group, is_element_successful

    def cocubes_comfirm_submit_test(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, "//*[@id='confirmsubmit']").click()
            print("Test is submitted")
            cocubes_next_group = "Submission Confirmed"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Test is not submitted")
            is_element_successful = False
            cocubes_next_group = "Submission confirmation Failed"
        return cocubes_next_group, is_element_successful

    def mettl_start_test(self):
        time.sleep(10)
        try:
            self.driver.switch_to.frame('thirdPartyIframe')
            self.driver.find_element(By.XPATH,
                                     "//*[@class='btn btn-primary py-2 px-3 btn-lineheight mobile-fixed-btn btn btn-primary']").click()
            print("Mettl Test is Started")
            mettl_start_test = "Start test1 Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl test is not Started")
            is_element_successful = False
            mettl_start_test = "Start test1 Failed"
        return mettl_start_test, is_element_successful

    def mettl_start_test2(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='py-2 px-4 mobile-btn-block btn btn-primary']").click()
            print("Mettl Test is Started2")
            mettl_start_test2 = "Start test2 Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl test is not Started2")
            is_element_successful = False
            mettl_start_test2 = "Start test2 Failed"
        return mettl_start_test2, is_element_successful

    def mettl_terms_and_conditions(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.NAME, "consentCheckbox").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@class ='px-4 mobile-btn-block btn btn-primary']").click()
            print("Terms and conditions Success")
            mettl_start_test2 = "Terms and conditions Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Terms and conditions Failed")
            is_element_successful = False
            mettl_start_test2 = "Terms and conditions Failed"
        return mettl_start_test2, is_element_successful

    def mettl_start_test3(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='px-4 text-sky-lighter mobile-fixed-btn  btn btn-primary']").click()
            print("Mettl Test is Started3")
            mettl_start_test3 = "Start test3 Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl test is not Started3")
            is_element_successful = False
            mettl_start_test2 = "Start test3 Failed"
        return mettl_start_test3, is_element_successful

    def mettl_answer_question(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='px-5 py-3 d-block form-check-label']").click()
            print("Mettl Test is Started2")
            mettl_answer_question = "answered_question"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl test is not Started2")
            is_element_successful = False
            mettl_answer_question = "answer failed"
        return mettl_answer_question, is_element_successful

    def mettl_next_section(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class='word-break border px-xl-3 px-2 btn btn-success']").click()
            print("Mettl Next section success")
            mettl_next_section = "Next group success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl next section failed")
            is_element_successful = False
            mettl_next_section = "mettl next section failed"
        return mettl_next_section, is_element_successful

    def mettl_finish_test(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@class=' last-item-btn  btn btn-ft btn-link btn-focus-outline  btn-default-ft border-white']").click()
            print("Mettl Final Submit success")
            mettl_next_section = "Mettl Final Submit success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl Final Submit failed")
            is_element_successful = False
            mettl_next_section = "Mettl Final Submit failed"
        return mettl_next_section, is_element_successful

    def mettl_finish_test_confirmation(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@class="btn btn-primary py-2 px-3 ft-btn-danger btn-danger btn btn-primary"]').click()
            print("Mettl Final Submit success")
            mettl_next_section = "Mettl Final Submit Confirmation success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl Final Submit failed")
            is_element_successful = False
            mettl_next_section = "Mettl Final Submit Confirmation failed"
        return mettl_next_section, is_element_successful

    def mettl_group_names(self):
        time.sleep(2)
        try:
            value = self.driver.find_element(By.XPATH,
                                             '//*[@class="pr-2 text-truncate"]').text
            print(value)
            print(type(value))
            print(len(value))
            print("Mettl group names success")
            group_names = value
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Mettl group names failed")
            is_element_successful = False
            mettl_next_section = "Mettl Final Submit Confirmation failed"
        return group_names, is_element_successful

    def tl_start_test(self):
        time.sleep(30)
        try:
            self.driver.switch_to.frame('thirdPartyIframe')
            # job title text
            self.driver.find_element(By.XPATH, "//*[@id='textbox_62fa715a-0dcb-498b-bf09-151fa7faad61']").send_keys(
                'QA')
            # recent position type
            self.driver.find_element(By.XPATH,
                                     '//*[@id="dropdown_d7244e75-eb2a-47a9-b23b-70f3412244d1"]/option[3]').click()
            # Recent Industry
            self.driver.find_element(By.XPATH,
                                     '//*[@id="dropdown_a7d5f8e3-1de4-4840-acf2-5a3d5ab7265e"]/option[2]').click()
            # recent occupation
            self.driver.find_element(By.XPATH,
                                     '//*[@id="dropdown_7ed143db-e43f-4759-af35-9f5eebde8a8f"]/option[4]').click()
            # next button
            self.driver.find_element(By.XPATH, '//*[@id="navigateNextBottom').click()

            print("TL Test is Started")
            tl_start_test = "Start test Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("TL test is not Started")
            is_element_successful = False
            tl_start_test = "Start test Failed"
        return tl_start_test, is_element_successful

    def tl_copyright_page(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="navigateNextBottom"]').click()

            print("TL Copywrite success")
            tl_copyright_page = "Copywrite Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("TL Copywrite Failed")
            is_element_successful = False
            tl_copyright_page = "Copywrite Failed"
        return tl_copyright_page, is_element_successful

    def tl_instructions_page1(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="navigateNextBottom"]').click()
            print("TL instructions2 success")
            tl_instructions_page1 = "instructions Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("TL instructions2 failed")
            is_element_successful = False
            tl_instructions_page = "instructions Failed"
        return tl_instructions_page1, is_element_successful

    def tl_instructions_page2(self):
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@class="btn btn-primary').click()
            print("TL instructions success")
            tl_instructions_page2 = "instructions2 Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("TL instructions failed")
            is_element_successful = False
            tl_instructions_page2 = "instructions2 Failed"
        return tl_instructions_page2, is_element_successful

    def tl_test_directions1(self):
        tl_test_directions1 = "EMPTY"
        is_element_successful = None
        for count in range(0, 9):
            time.sleep(5)
            try:
                self.driver.find_element(By.XPATH, '//*[@id="navigateNextBottom').click()
                print("TL instructions success")
                tl_test_directions1 = "test directions1 Success"
                is_element_successful = True

            except Exception as e:
                print(e)
                print("TL instructions failed")
                is_element_successful = False
                tl_test_directions1 = "test directions1 Failed"

        return tl_test_directions1, is_element_successful

    def wheebox_starttest_checkbox(self):
        time.sleep(5)
        try:
            self.driver.switch_to.frame('thirdPartyIframe')
            self.driver.find_element(By.XPATH, "//*[@class='checkbox state-success']").click()
            print("Wheebox agreement is Accepted")
            wheebox_agreement = "Agreed"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Wheebox agreement is failed")
            is_element_successful = False
            wheebox_agreement = "Not Agreed"
        return wheebox_agreement, is_element_successful

    def wheebox_proceed_test(self):
        time.sleep(30)
        try:
            self.driver.find_element(By.XPATH, "//*[@id='waitingLoungButton']").click()
            print("Wheebox proceed test  is success")
            wheebox_proceed_test = "Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Wheebox proceed test is failed")
            is_element_successful = False
            wheebox_proceed_test = "Failed"
        return wheebox_proceed_test, is_element_successful

    def wheebox_auto_next_qn(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='checkbox green-txt-clr unselectable']").click()
            print("Auto next question is success")
            wheebox_auto_next_qn = "Success"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Auto next question is failed")
            is_element_successful = False
            wheebox_auto_next_qn = "Failed"
        return wheebox_auto_next_qn, is_element_successful

    def wheebox_answer_qn(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='radio state-error']").click()
            print("Question answer is success")
            wheebox_answer_qn = "answered"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Question answer is failed")
            is_element_successful = False
            wheebox_answer_qn = "Not answered"
        return wheebox_answer_qn, is_element_successful

    def wheebox_submit_test(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='pull-right unselectable']").click()
            print("Test is submitted successfully")
            wheebox_submit_test = "submitted"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Test is not submitted successfully")
            is_element_successful = False
            wheebox_submit_test = "Not submitted"
        return wheebox_submit_test, is_element_successful

    def wheebox_confirm_submit(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//*[@class='confirm']").click()
            print("Test is submitted successfully")
            wheebox_confirm_submit = "submitted"
            is_element_successful = True

        except Exception as e:
            print(e)
            print("Test is not submitted successfully")
            is_element_successful = False
            wheebox_confirm_submit = "Not submitted"
        return wheebox_confirm_submit, is_element_successful

    def coding_editor(self, code):
        self.driver.find_element(By.CLASS_NAME, 'ace_content').click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.active_element.send_keys(code)
        self.driver.find_element(By.XPATH, '//button[text()=" Compile & Execute"]').click()
        time.sleep(7)
        action = self.driver.find_element(By.CLASS_NAME, 'ace_content')
        action.click()
        self.driver.switch_to.parent_frame()
        action.send_keys(Keys.CONTROL + 'A')

    # def coding_editor(self, code):
    #     self.driver.find_element(By.CLASS_NAME, 'ace_content').click()
    #     self.driver.switch_to.parent_frame()
    #     self.driver.switch_to.active_element.clear()
    #     self.driver.switch_to.active_element.send_keys(code)
    #     self.driver.find_element(By.XPATH, '//button[text()=" Compile & Execute"]').click()
    #

    # self.driver.find_element(By.XPATH, '//button[text()=" Compile & Execute"]').click()


assess_ui_common_obj = AssessmentUICommon()
# status = assess_ui_common_obj.ui_login_to_test()
# print(status)
# url = "https://pearsonstg.hirepro.in/assessment/#/assess/login/eyJhbGlhcyI6ImF1dG9tYXRpb24ifQ%3D%3D"
# path = r"F:\qa_automation\chromedriver.exe"
# assess_ui_common_obj.initiate_browser_for_proctoring( url, path)
