from SCRIPTS.UI_COMMON.assessment_ui_common_v2 import *
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.write_excel_new import *
from SCRIPTS.COMMON.io_path import *
from SCRIPTS.CRPO_COMMON.crpo_common import *
from SCRIPTS.CRPO_COMMON.credentials import *


class QPVerification:

    def __init__(self):
        self.row = 1
        write_excel_object.save_result(output_path_ui_mcq_client_test_random)
        header = ['QP_Verification']
        write_excel_object.write_headers_for_scripts(0, 0, header, write_excel_object.black_color_bold)
        header = ['Test Cases', 'Status', 'Test Id', 'Candidate Id', 'Testuser ID', 'User Name', 'Password',
                  'mismatched questions(in QP) - question out of the QP', "Mismatched Group1 if any",
                  "Mismatched Group2 if any", "Expected Overall Randomization",
                  "Actual Overall Randomization", "Expected Test level Randomization ( group position swap)",
                  "Actual test level Randomization ( group position swap )",
                  "Expected Group Randomization ( section position swap )",
                  "Actual Group Randomization ( section position swap )",
                  "Expected Group1 Randomization", "Actual Group1 Randomization",
                  "Expected Group2 Randomization", "Actual Group2 Randomization",
                  '1st login Q1', '2nd login Q1', '1st login Q2', '2nd login Q2', '1st login Q3', '2nd login Q3',
                  '1st login Q4', '2nd login Q4', '1st login Q5', '2nd login Q5', '1st login Q6', '2nd login Q6',
                  '1st login Q7', '2nd login Q7', '1st login Q8', '2nd login Q8', '1st login Q9', '2nd login Q9',
                  '1st login Q10', '2nd login Q10', '1st login Q11', '2nd login Q11', '1st login Q12', '2nd login Q12',
                  '1st login Q13', '2nd login Q13', '1st login Q14', '2nd login Q14', '1st login Q15', '2nd login Q15',
                  '1st login Q16', '2nd login Q16', '1st login Q17', '2nd login Q17', '1st login Q18', '2nd login Q18',
                  '1st login Q19', '2nd login Q19', '1st login Q20', '2nd login Q20', '1st login Q21', '2nd login Q21',
                  '1st login Q22', '2nd login Q22', '1st login Q23', '2nd login Q23', '1st login Q24', '2nd login Q24',
                  '1st login Q25', '2nd login Q25', '1st login Q26', '2nd login Q26', '1st login Q26', '2nd login Q26',
                  '1st login Q28', '2nd login Q28', '1st login Q29', '2nd login Q29', '1st login Q30', '2nd login Q30',
                  '1st login Q31', '2nd login Q31', '1st login Q32', '2nd login Q32', '1st login Q33', '2nd login Q33',
                  '1st login Q34', '2nd login Q34', '1st login Q35', '2nd login Q35', '1st login Q36', '2nd login Q36',
                  '1st login Q37', '2nd login Q37', '1st login Q38', '2nd login Q38', '1st login Q39', '2nd login Q39',
                  '1st login Q40', '2nd login Q40']
        write_excel_object.write_headers_for_scripts(1, 0, header, write_excel_object.black_color_bold)

        self.qp_qn_index = [{"qn": "MS Client side question randomization group1section1 question1", "index": 1},
                            {"qn": "MS Client side question randomization group1section1 question2", "index": 2},
                            {"qn": "MS Client side question randomization group1section1 question3", "index": 3},
                            {"qn": "MS Client side question randomization group1section1 question4", "index": 4},
                            {"qn": "MS Client side question randomization group1section1 question5", "index": 5},
                            {"qn": "MS Client side question randomization group1section1 question6", "index": 6},
                            {"qn": "MS Client side question randomization group1section1 question7", "index": 7},
                            {"qn": "MS Client side question randomization group1section1 question8", "index": 8},
                            {"qn": "MS Client side question randomization group1section1 question9", "index": 9},
                            {"qn": "MS Client side question randomization group1section1 question10", "index": 10},
                            {"qn": "MS Client side question randomization group1section2 question11", "index": 11},
                            {"qn": "MS Client side question randomization group1section2 question12", "index": 12},
                            {"qn": "MS Client side question randomization group1section2 question13", "index": 13},
                            {"qn": "MS Client side question randomization group1section2 question14", "index": 14},
                            {"qn": "MS Client side question randomization group1section2 question15", "index": 15},
                            {"qn": "MS Client side question randomization group1section2 question16", "index": 16},
                            {"qn": "MS Client side question randomization group1section2 question17", "index": 17},
                            {"qn": "MS Client side question randomization group1section2 question18", "index": 18},
                            {"qn": "MS Client side question randomization group1section2 question19", "index": 19},
                            {"qn": "MS Client side question randomization group1section2 question20", "index": 20},
                            {"qn": "MS Client side question randomization group2section1 question21", "index": 21},
                            {"qn": "MS Client side question randomization group2section1 question22", "index": 22},
                            {"qn": "MS Client side question randomization group2section1 question23", "index": 23},
                            {"qn": "MS Client side question randomization group2section1 question24", "index": 24},
                            {"qn": "MS Client side question randomization group2section1 question25", "index": 25},
                            {"qn": "MS Client side question randomization group2section1 question26", "index": 26},
                            {"qn": "MS Client side question randomization group2section1 question27", "index": 27},
                            {"qn": "MS Client side question randomization group2section1 question28", "index": 28},
                            {"qn": "MS Client side question randomization group2section1 question29", "index": 29},
                            {"qn": "MS Client side question randomization group2section1 question30", "index": 30},
                            {"qn": "MS Client side question randomization group2section2 question31", "index": 31},
                            {"qn": "MS Client side question randomization group2section2 question32", "index": 32},
                            {"qn": "MS Client side question randomization group2section2 question33", "index": 33},
                            {"qn": "MS Client side question randomization group2section2 question34", "index": 34},
                            {"qn": "MS Client side question randomization group2section2 question35", "index": 35},
                            {"qn": "MS Client side question randomization group2section2 question36", "index": 36},
                            {"qn": "MS Client side question randomization group2section2 question37", "index": 37},
                            {"qn": "MS Client side question randomization group2section2 question38", "index": 38},
                            {"qn": "MS Client side question randomization group2section2 question39", "index": 39},
                            {"qn": "MS Client side question randomization group2section2 question40", "index": 40}]

        self.section1_group1_questions = ["MS Client side question randomization group1section1 question1",
                                          "MS Client side question randomization group1section1 question2",
                                          "MS Client side question randomization group1section1 question3",
                                          "MS Client side question randomization group1section1 question4",
                                          "MS Client side question randomization group1section1 question5",
                                          "MS Client side question randomization group1section1 question6",
                                          "MS Client side question randomization group1section1 question7",
                                          "MS Client side question randomization group1section1 question8",
                                          "MS Client side question randomization group1section1 question9",
                                          "MS Client side question randomization group1section1 question10"]

        self.section2_group1_questions = ["MS Client side question randomization group1section2 question11",
                                          "MS Client side question randomization group1section2 question12",
                                          "MS Client side question randomization group1section2 question13",
                                          "MS Client side question randomization group1section2 question14",
                                          "MS Client side question randomization group1section2 question15",
                                          "MS Client side question randomization group1section2 question16",
                                          "MS Client side question randomization group1section2 question17",
                                          "MS Client side question randomization group1section2 question18",
                                          "MS Client side question randomization group1section2 question19",
                                          "MS Client side question randomization group1section2 question20"]

        self.section1_group2_questions = ["MS Client side question randomization group2section1 question21",
                                          "MS Client side question randomization group2section1 question22",
                                          "MS Client side question randomization group2section1 question23",
                                          "MS Client side question randomization group2section1 question24",
                                          "MS Client side question randomization group2section1 question25",
                                          "MS Client side question randomization group2section1 question26",
                                          "MS Client side question randomization group2section1 question27",
                                          "MS Client side question randomization group2section1 question28",
                                          "MS Client side question randomization group2section1 question29",
                                          "MS Client side question randomization group2section1 question30"]

        self.section2_group2_questions = ["MS Client side question randomization group2section2 question31",
                                          "MS Client side question randomization group2section2 question32",
                                          "MS Client side question randomization group2section2 question33",
                                          "MS Client side question randomization group2section2 question34",
                                          "MS Client side question randomization group2section2 question35",
                                          "MS Client side question randomization group2section2 question36",
                                          "MS Client side question randomization group2section2 question37",
                                          "MS Client side question randomization group2section2 question38",
                                          "MS Client side question randomization group2section2 question39",
                                          "MS Client side question randomization group2section2 question40"]

        self.group1_questions = self.section1_group1_questions + self.section2_group1_questions
        self.group2_questions = self.section1_group2_questions + self.section2_group2_questions

        self.expected_questions = self.section1_group1_questions + self.section2_group1_questions + \
                                  self.section1_group2_questions + self.section2_group2_questions

    def is_randomized(self, qn_details):
        for all_qns_with_index in self.qp_qn_index:
            if qn_details.get('question') == all_qns_with_index.get("qn"):
                if qn_details.get('index') != all_qns_with_index.get("index"):
                    self.overall_randomization = "Yes"
                    if 1 <= qn_details.get('index') <= 20:
                        if qn_details.get('question') in self.group1_questions:
                            self.g1_randomization = "Yes"
                    elif 21 <= qn_details.get('index') <= 40:
                        if qn_details.get('question') in self.group2_questions:
                            self.g2_randomization = "Yes"
                break

    def verify_questions(self, tu_details, login_user, login_pass, candidate_id, tu_id):
        self.overall_randomization = "No"
        self.test_level_randomization = "No"
        self.group_randomization = "No"
        self.g1_randomization = "No"
        self.g2_randomization = "No"
        self.color = write_excel_object.green_color
        self.status = 'pass'
        self.row = self.row + 1
        self.delivered_questions = []
        self.relogin_questions = []
        self.actual_g1_questions = []
        self.actual_g2_questions = []
        self.browser = assess_ui_common_obj.initiate_browser(amsin_automation_assessment_url, chrome_driver_path)
        login_details = assess_ui_common_obj.ui_login_to_test(login_user, login_pass)
        if login_details == 'SUCCESS':
            i_agreed = assess_ui_common_obj.select_i_agree()
            if i_agreed:
                start_test_status = assess_ui_common_obj.start_test_button_status()
                assess_ui_common_obj.start_test()
                for question_index in range(1, int(tu_details.get('expectedTotalQuestionsCount') + 1)):
                    assess_ui_common_obj.next_question(question_index)
                    qn_string = assess_ui_common_obj.find_question_string_v2()
                    print(qn_string)
                    self.delivered_questions.append(qn_string[0])
                    self.qn_details = {'question': qn_string[0], 'group': qn_string[1], 'section': qn_string[2],
                                       'index': question_index}
                    client_side_randomization.is_randomized(self.qn_details)
                    if self.qn_details.get('group') == 'Group1':
                        self.actual_g1_questions.append(self.qn_details.get('question'))
                        if 21 <= self.qn_details.get('index') <= 40:
                            self.test_level_randomization = "Yes"
                        if self.qn_details.get('section') == 'Group1Section1':
                            if 11 <= self.qn_details.get('index') <= 20:
                                self.group_randomization = "Yes"
                        elif self.qn_details.get('section') == 'Group1Section2':
                            if 1 <= self.qn_details.get('index') <= 10:
                                self.group_randomization = "Yes"
                    elif self.qn_details.get('group') == 'Group2':
                        self.actual_g2_questions.append(self.qn_details.get('question'))
                        if 1 <= self.qn_details.get('index') <= 20:
                            self.test_level_randomization = "Yes"
                        if self.qn_details.get('section') == 'Group1Section1':
                            if 31 <= self.qn_details.get('index') <= 40:
                                self.group_randomization = "Yes"
                        elif self.qn_details.get('section') == 'Group1Section2':
                            if 21 <= self.qn_details.get('index') <= 30:
                                self.group_randomization = "Yes"

                self.overall_randomization_status = client_side_randomization.is_randomized(self.qn_details)
                print("1st Login")
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])
                time.sleep(1)
                self.browser.execute_script(
                    '''window.open("https://amsin.hirepro.in/assessment/#/assess/login/eyJhbGlhcyI6ImF1dG9tYXRpb24ifQ%3D%3D", "_blank");''')
                time.sleep(2)
                self.browser.switch_to.window(self.browser.window_handles[1])
                login_details = assess_ui_common_obj.ui_login_to_test(login_user, login_pass)
                if login_details == 'SUCCESS':
                    i_agreed = assess_ui_common_obj.select_i_agree()
                    if i_agreed:
                        start_test_status = assess_ui_common_obj.start_test_button_status()
                        assess_ui_common_obj.start_test()
                        for question_index in range(1, int(tu_details.get('expectedTotalQuestionsCount') + 1)):
                            assess_ui_common_obj.next_question(question_index)
                            qn_string = assess_ui_common_obj.find_question_string_v2()
                            self.relogin_questions.append(qn_string[0])
                self.browser.quit()
                write_excel_object.compare_results_and_write_vertically(tu_details.get('testCases'), None, self.row, 0)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('testID'), None, self.row, 2)
                write_excel_object.compare_results_and_write_vertically(candidate_id, None, self.row, 3)
                write_excel_object.compare_results_and_write_vertically(tu_id, None, self.row, 4)
                write_excel_object.compare_results_and_write_vertically(login_user, None, self.row, 5)
                write_excel_object.compare_results_and_write_vertically(login_pass, None, self.row, 6)

                mismatched_questions = set(self.delivered_questions) - set(self.expected_questions)
                if len(mismatched_questions) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    mismatched_questions = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 7, str(mismatched_questions),
                                            write_excel_object.current_status_color)
                group1_mismatched = set(self.group1_questions) - set(self.actual_g1_questions)
                if len(group1_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    group1_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 8, str(group1_mismatched),
                                            write_excel_object.current_status_color)

                group2_mismatched = set(self.group2_questions) - set(self.actual_g2_questions)
                if len(group2_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    group2_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 9, str(group2_mismatched),
                                            write_excel_object.current_status_color)

                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedOverallRandomization'),
                                                                        self.overall_randomization, self.row, 10)
                write_excel_object.compare_results_and_write_vertically(
                    tu_details.get('expectedTestLevelRandomization'),
                    self.test_level_randomization, self.row, 12)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedGroupRandomization'),
                                                                        self.group_randomization, self.row, 14)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedGroup1Randomization'),
                                                                        self.g1_randomization, self.row, 16)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedGroup2Randomization'),
                                                                        self.g2_randomization, self.row, 18)
                col = 20
                for index in range(0, int(tu_details.get('expectedTotalQuestionsCount'))):
                    print(index)
                    write_excel_object.compare_results_and_write_vertically(self.delivered_questions[index],
                                                                            self.relogin_questions[index], self.row,
                                                                            col)
                    col = col + 2
                write_excel_object.compare_results_and_write_vertically(write_excel_object.current_status, None,
                                                                        self.row, 1)


client_side_randomization = QPVerification()
excel_read_obj.excel_read(input_path_ui_mcq_client_section_random, 3)
candidate_details = excel_read_obj.details
token = crpo_common_obj.login_to_crpo(cred_crpo_admin.get('user'), cred_crpo_admin.get('password'),
                                      cred_crpo_admin.get('tenant'))
test_id = 15251
event_id = 11625
jobrole_id = 30439
sprint_id = input('Enter Sprint ID ')
next_cand = 2000
for current_excel_row in candidate_details:
    next_cand = next_cand + 1
    sprint_id = sprint_id + str(next_cand)
    print(sprint_id)
    candidate_id = crpo_common_obj.create_candidate(token, sprint_id)
    tag_candidate = crpo_common_obj.tag_candidate_to_test(token, candidate_id, test_id, event_id, jobrole_id)
    time.sleep(5)
    test_userid = crpo_common_obj.get_all_test_user(token, candidate_id)
    print(test_userid)
    tu_cred = crpo_common_obj.test_user_credentials(token, test_userid)
    login_id = tu_cred['data']['testUserCredential']['loginId']
    password = tu_cred['data']['testUserCredential']['password']
    client_side_randomization.verify_questions(current_excel_row, login_id, password, candidate_id, test_userid)
write_excel_object.write_overall_status(1)
