from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.write_excel_new import *
from SCRIPTS.CRPO_COMMON.crpo_common import *
from SCRIPTS.ASSESSMENT_COMMON.assessment_common import *
from SCRIPTS.COMMON.io_path import *
from SCRIPTS.DB_DELETE.sanitizeapi_resetuser import *
import urllib3

urllib3.disable_warnings()


class SanitizeAutomation:
    def __init__(self):
        self.row_size = 2
        write_excel_object.save_result(output_path_sanitize_automation)
        header = ["Sanitize relogin automation"]
        write_excel_object.write_headers_for_scripts(0, 0, header,
                                                     write_excel_object.black_color_bold)
        header1 = ["Testcases", "Status", "Test ID", "Candidate ID", "Test User ID", "ExpectedMessage", "ActualMessage",
                   "ExpectedScoreStatus", "ActualScoreStatus", "ExpectedUsecase", "Actual Usecase", "isVendorTest",
                   "IsSLCEnabled"]
        write_excel_object.write_headers_for_scripts(1, 0, header1,
                                                     write_excel_object.black_color_bold)

    def excel_write(self, data):
        write_excel_object.current_status_color = write_excel_object.green_color
        write_excel_object.current_status = "Pass"
        write_excel_object.compare_results_and_write_vertically(data.get('testCaseInfo'), None, self.row_size, 0)
        write_excel_object.compare_results_and_write_vertically(data.get('primaryTestId'), None, self.row_size, 2)
        write_excel_object.compare_results_and_write_vertically(data.get('candidateId'), None, self.row_size, 3)
        write_excel_object.compare_results_and_write_vertically(data.get('testUserID'), None, self.row_size, 4)
        write_excel_object.compare_results_and_write_vertically(data.get('message'), message, self.row_size, 5)
        write_excel_object.compare_results_and_write_vertically(data.get('scoreStatus'), score_status, self.row_size, 7)
        write_excel_object.compare_results_and_write_vertically(data.get('useCase'), usecase, self.row_size, 9)
        write_excel_object.compare_results_and_write_vertically(data.get('isVendorTest'), None, self.row_size, 11)
        write_excel_object.compare_results_and_write_vertically(data.get('IsSLCEnabled'), None, self.row_size, 12)
        write_excel_object.compare_results_and_write_vertically(write_excel_object.current_status, None, self.row_size,
                                                                1)
        self.row_size = self.row_size + 1


re_initiate_obj = SanitizeAutomation()
reset_test_user_obj.reset_test_users()
excel_read_obj.excel_read(input_path_sanitize_automation, 0)
excel_data = excel_read_obj.details
crpo_headers = crpo_common_obj.login_to_crpo(cred_crpo_admin.get('user'), cred_crpo_admin.get('password'),
                                             cred_crpo_admin.get('tenant'))
n = 4
for data in excel_data:
    test1 = int(data.get('untagUserFromT2'))
    if test1 != 0:
        candidate_id = int(data.get('candidateId'))
        test_id = test1
        test_user_details = crpo_common_obj.search_test_user_by_cid_and_testid(crpo_headers, candidate_id, test_id)
        if test_user_details.get('testUserId'):
            test_user_id_old = test_user_details.get('testUserId')
            untag_candidates_details = [{"testUserIds": [test_user_id_old]}]
            crpo_common_obj.untag_candidate(crpo_headers, untag_candidates_details)
            # untag_candidates = crpo_common_obj.untag_candidate2(crpo_headers, test_user_id_old)

    test_user_id = int(data.get('testUserID'))
    candidate_id_2 = int(data.get('candidateId'))
    print("Case no : ", n)
    n += 1
    result = crpo_common_obj.sanitise_tu_automation(crpo_headers, test_user_id)
    message = "NULL"
    score_status = "null"
    if 'Message' in result['data']:
        message = result['data']['Message']
    else:
        context_id = result['data']['ContextId']
        print(context_id)
        current_job_status = 'Pending'

        while current_job_status == 'Pending':
            current_job_status = CrpoCommon.job_status(crpo_headers, context_id)
            current_job_status = current_job_status['data']['JobState']
            print("_________________ sanitize automation is in Progress _______________________")
            print(current_job_status)
            time.sleep(40)
        print(current_job_status)
        if current_job_status == 'SUCCESS':
            response = crpo_common_obj.tests_against_candidate(crpo_headers, candidate_id_2)
            score = response['data']['TestsAgainstCandidate'][0]['TotalScore']
            if score != "null":
                score_status = "Available"
            else:
                score_status = "null"

    usecase = result['data']['UseCasePassed']
    time.sleep(5)
    re_initiate_obj.excel_write(data)
write_excel_object.write_overall_status(testcases_count=4)
