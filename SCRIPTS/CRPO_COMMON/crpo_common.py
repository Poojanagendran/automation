import requests
import json
import time


class CrpoCommon:
    domain = 'https://amsin.hirepro.in'
    pearson_domain = 'https://pearsonstg.hirepro.in'

    @staticmethod
    def login_to_crpo(login_name, password, tenant):
        header = {"content-type": "application/json"}
        data = {"LoginName": login_name, "Password": password, "TenantAlias": tenant, "UserName": login_name}
        response = requests.post(crpo_common_obj.domain + "/py/common/user/login_user/", headers=header,
                                 data=json.dumps(data), verify=False)
        login_response = response.json()

        headers = {"content-type": "application/json", "APP-NAME": "CRPO", "X-APPLMA": "true",
                   "X-AUTH-TOKEN": login_response.get("Token")}
        print(headers)
        return headers

    @staticmethod
    def candidate_web_transcript(token, test_id, test_user_id):
        request = {"testId": int(test_id), "testUserId": int(test_user_id),
                   "reportFlags": {"eduWorkProfilesRequired": True, "testUsersScoreRequired": True,
                                   "fileContentRequired": False, "isProctroingDetailsRequired": True,
                                   "testUserItemRequired": True}, "print": False}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/report/api/v1/candidatetranscript/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response.json()

    @staticmethod
    def force_evaluate_proctoring(token, tu_ids):
        request = {
            "testUserIds": tu_ids, "isForce": True}
        response = requests.post(crpo_common_obj.domain +
                                 "/py/assessment/htmltest/api/v1/initiate-test-proc/?isSync=false",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response.json()

    # interviews Grid
    @staticmethod
    def run_proctoring(token, ir_id):
        print(token)
        request = {"interviewId": int(ir_id)}
        response = requests.post(crpo_common_obj.domain +
                                 "/py/crpo/api/v1/interview/interviewer/view_proctored_data/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response.json()

    # interviews Grid
    @staticmethod
    def lip_sync(token, ir_id):
        print(token)
        request = {"irId": int(ir_id)}
        response = requests.post(crpo_common_obj.domain +
                                 "/py/crpo/api/v1/interview/lipsync/get_lipsync_samples/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response.json()

    @staticmethod
    def job_status(token, contextguid):
        request = {"ContextGUID": contextguid}
        response = requests.post(crpo_common_obj.domain + "/py/crpo/api/v1/getStatusOfAsyncAPI",
                                 headers=token, data=json.dumps(request, default=str), verify=False)
        resp_dict = json.loads(response.content)
        return resp_dict

    @staticmethod
    def upload_files(token, file_name, file_path):
        token.pop('content-type', None)
        token.pop('X-APPLMA', None)
        request = {'file': (file_name, open(file_path, 'rb'))}
        token.update({'x-guid': file_name + '12_20_2021_5'})
        url = crpo_common_obj.domain + '/py/common/filehandler/api/v2/upload/.doc,.rtf,.dot,.docx,' \
                                       '.docm,.dotx,.dotm,.docb,.pdf,.xls,.xlt,.xlm,.xlsx,.xlsm,.xltx,.xltm,.xlsb,.xla,.xlam,.xll,' \
                                       '.xlw,.ppt,.pot,.pps,.pptx,.pptm,.potx,.potm,.ppam,.ppsx,.ppsm,.sldx,.sldm,.zip,.rar,.7z,.gz,.jpeg,' \
                                       '.jpg,.gif,.png,.msg,.txt,.mp4,.mvw,.3gp,.sql,.webm,.csv,.odt,.json,.ods,.ogg,.p12,/5000/'

        api_request = requests.post(url, headers=token, files=request, verify=False)
        resp_dict = json.loads(api_request.content)
        return resp_dict

    @staticmethod
    def untag_candidate(token, data1):
        for request in data1:
            response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/un-tag/",
                                     headers=token,
                                     data=json.dumps(request, default=str), verify=False)

    @staticmethod
    def proctor_evaluation_detail(token, testuser_id):
        token.pop('X-APPLMA', None)
        request = {"testUserId": testuser_id}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/get_proctor_detail/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        time.sleep(10)
        tu_proctor_details = response.json()
        return tu_proctor_details

    @staticmethod
    def save_apppreferences(token, content, id, type):
        data = {"AppPreference": {"Id": id, "Content": content, "Type": type}, "IsTenantGlobal": True}

        response = requests.post("https://amsin.hirepro.in/py/common/common_app_utils/save_app_preferences/",
                                 headers=token, data=json.dumps(data, default=str), verify=False)
        return response.json()

    @staticmethod
    def re_initiate_automation(token, test_id, candidate_id):
        token.pop('X-APPLMA', None)
        request = {"testId": test_id, "candidateId": candidate_id}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/re_initiate_automation/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)

    @staticmethod
    def get_all_questions(token, request_data):
        response = requests.post(crpo_common_obj.domain + "/py/assessment/authoring/api/v1/getAllQuestion/",
                                 headers=token,
                                 data=str(request_data.get('request')), verify=False)
        get_all_questions_resp = json.loads(response.content)
        return get_all_questions_resp

    @staticmethod
    def generate_applicant_report(token, request_payload):
        response = requests.post(crpo_common_obj.domain + "/py/common/xl_creator/api/v1/generate_applicant_report/",
                                 headers=token, data=json.dumps(request_payload, default=str), verify=False)
        resp_dict = json.loads(response.content)
        return resp_dict

    @staticmethod
    def generate_plagiarism_report(token, request_payload):
        response = requests.post(crpo_common_obj.domain + "/py/assessment/report/api/v1/plagiarismreport/",
                                 headers=token, data=json.dumps(request_payload, default=str), verify=False)
        resp_dict = json.loads(response.content)
        return resp_dict

    @staticmethod
    def initiate_vendor_score(crpotoken, cid, test_id):
        url = crpo_common_obj.domain + '/py/assessment/assessmentvendor/api/v1/initiateVendorScore/'
        data = {"testId": test_id, "candidateIds": [cid], "isForced": True}

        response = requests.post(url,
                                 headers=crpotoken,
                                 data=json.dumps(data, default=str), verify=False)
        it_vendor_resp = response.json()
        return it_vendor_resp

    @staticmethod
    def untag_candidate_by_cid(token, test_id, candidate_ids):
        data1 = [{"testId": test_id, "candidateIds": candidate_ids}]
        for request in data1:
            response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/un-tag/",
                                     headers=token,
                                     data=json.dumps(request, default=str), verify=False)

    @staticmethod
    def create_candidate(token, usn):
        request = {"PersonalDetails": {"FirstName": usn, "Email1": "S1N1J1E1V11111" + usn + "@gmail.com", "USN": usn,
                                       "DateOfBirth": "2022-02-08T18:30:00.000Z"}}
        response = requests.post(crpo_common_obj.domain + "/py/rpo/create_candidate/", headers=token,
                                 data=json.dumps(request), verify=False)
        response_data = response.json()
        candidate_id = response_data.get('CandidateId')
        if response_data.get('status') == 'OK':
            print("candidate created in crpo")
            url = 'https://automation-in.hirepro.in/?candidate=%s' % candidate_id
        else:
            print("candidate not created in CRPO_COMMON due to some technical glitch")
            print(response_data)
        return candidate_id

    @staticmethod
    def create_candidate_v2(token, request):
        response = requests.post(crpo_common_obj.domain + "/py/rpo/create_candidate/", headers=token,
                                 data=json.dumps(request), verify=False)
        response_data = response.json()
        print(response_data)
        candidate_id = response_data.get('CandidateId')
        if response_data.get('status') == 'OK':
            print("candidate created in crpo")
        else:
            print("candidate not created in CRPO_COMMON due to some technical glitch")

        return candidate_id

    @staticmethod
    def tag_candidate_to_test(token, cid, testid, eventid, jobroleid):
        request = {"CandidateIds": [int(cid)], "TestIds": [int(testid)], "EventId": int(eventid),
                   "JobRoleId": int(jobroleid), "Sync": "True"}
        response = requests.post(crpo_common_obj.domain +
                                 "/py/crpo/applicant/api/v1/tagCandidatesToEventJobRoleTests/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response

    @staticmethod
    def test_user_credentials(token, tu_id):
        request = {"testUserId": tu_id}
        response = requests.post(crpo_common_obj.domain +
                                 "/py/assessment/testuser/api/v1/getCredential/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response.json()

    @staticmethod
    def get_all_test_user(token, cid):
        request = {"isMyAssessments": False, "search": {"candidateIds": [cid]}}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/getAllTestUser/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        data = response.json()
        test_user_id = data['data']['testUserInfos'][0]['id']
        return test_user_id

    @staticmethod
    def get_candidate_by_id(token, cid):
        request = {"CandidateId": cid, "RequiredDetails": [1]}
        response = requests.post(crpo_common_obj.domain + "/py/rpo/get_candidate_details_by_id/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        candidate_details = response.json()

        return candidate_details

    @staticmethod
    def create_question(token, request):
        response = requests.post(crpo_common_obj.domain + "/py/assessment/authoring/api/v1/createQuestion/",
                                 headers=token, data=json.dumps(request), verify=False)
        question_id_resp = response.json()
        question_id = question_id_resp['data']['questionId']
        return question_id

    @staticmethod
    def get_question_for_id(token, question_id):
        request = {"id": question_id}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/authoring/api/v1/getQuestionForId/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        question_id_details = response.json()
        return question_id_details

    @staticmethod
    def calculate_question_statistics(token, question_ids):
        request = {"isPagingRequired": True, "questionIds": question_ids, "isComputeOnly": False,
                   "questionConfig": {"dontUpdateSystemDifficulty": False}}
        response = requests.post(
            crpo_common_obj.domain + "/py/assessment/report/api/v1/question_statistics/?isSync=false",
            headers=token,
            data=json.dumps(request, default=str), verify=False)
        question_status = response.json()
        question_status_context_id = question_status['data']['ContextId']
        return question_status_context_id

    @staticmethod
    def calculate_hirepro_question_statistics(token, question_ids):
        request = {"questionIds": question_ids, "isComputeOnly": False}
        print(request)
        response = requests.post(
            crpo_common_obj.domain + "/py/assessment/report/api/v1/hirepro_question_stats_api/",
            headers=token,
            data=json.dumps(request, default=str), verify=False)
        question_status = response.json()
        question_status_context_id = question_status['data']['ContextId']
        return question_status_context_id

    @staticmethod
    def calculate_question_statistics_for_tests(token, test_ids):
        request = {"testIds": [test_ids]}
        response = requests.post(
            crpo_common_obj.domain + "/py/assessment/report/api/v1/question_statistics_for_tests/?isSync=false",
            headers=token,
            data=json.dumps(request, default=str), verify=False)
        question_stats = response.json()
        test_question_stats_context_id = question_stats['data']['ContextId']
        return test_question_stats_context_id

    @staticmethod
    def get_test_user_infos(token, payload):
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/info/",
                                 headers=token,
                                 data=json.dumps(payload, default=str), verify=False)
        test_user_infos = response.json()
        return test_user_infos

    @staticmethod
    def search_test_user_by_cid_and_testid(token, cid, test_id):
        request = {"isPartnerTestUserInfo": True, "testId": test_id,
                   "search": {"status": 6, "candidateSearch": {"ids": [cid]}}}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/getTestUsersForTest/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        data = response.json()
        if 'testInfo' in data['data']:
            test_user_id = data['data']['testUserInfos'][0]['applicantBasicInfos'][0]['testUserId']
            copied_test_user_id = data['data']['testUserInfos'][0]['copiedTestUserId']
            offline_attended = data['data']['testUserInfos'][0]['isOffline']
            # total_score = int(data['data']['testUserInfos'][0]['totalScore'])
            test_user_data = {'testUserId': test_user_id, 'parentTestUserId': copied_test_user_id,
                              'Offline': offline_attended}
        else:
            test_user_data = {'testUserId': "NotExist", 'parentTestUserId': "EMPTY",
                              'Offline': "EMPTY"}

        return test_user_data

    @staticmethod
    def get_test_user_infos_v2(token, tuid):
        payload = {"testUserId": tuid, "requiredFlags": {"isGroupSectionWiseMarks": True, "isVendorDetails": True,
                                                         "isCodingSummary": False}}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/info/",
                                 headers=token,
                                 data=json.dumps(payload, default=str), verify=False)
        test_user_infos = response.json()
        return test_user_infos

    @staticmethod
    def change_applicant_status(token, applicant_id, event_id, jobrole_id, status_id):

        payload = {"ApplicantIds": [applicant_id], "EventId": event_id, "JobRoleId": jobrole_id,
                   "ToStatusId": status_id,
                   "Sync": "False", "Comments": "", "InitiateStaffing": False}
        response = requests.post(crpo_common_obj.domain + "/py/crpo/applicant/api/v1/applicantStatusChange/",
                                 headers=token,
                                 data=json.dumps(payload, default=str), verify=False)
        test_user_infos = response.json()
        return test_user_infos

    @staticmethod
    def get_applicant_infos(token, candidate_id):
        payload = {"CandidateIds": [candidate_id]}
        response = requests.post(crpo_common_obj.domain + "/py/crpo/applicant/api/v1/getApplicantsInfo/",
                                 headers=token,
                                 data=json.dumps(payload, default=str), verify=False)
        applicant_infos = response.json()
        return applicant_infos

    @staticmethod
    def force_untag_testuser(token, test_user_id):
        request = {"testUserIds": [test_user_id], "isForced": True}
        response = requests.post(crpo_common_obj.domain + "/py/assessment/testuser/api/v1/un-tag/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        return response

    @staticmethod
    def persistent_save(token, s3_url):
        request = [{
            "origFileUrl": s3_url,
            "relativePath": "at/proctor/image/10324/1367938", "isSync": True, "targetBucket": "recording-bucket",
            "metaData": None}]
        response = requests.post(crpo_common_obj.pearson_domain +
                                 "/py/common/filehandler/api/v2/persistent-save/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        resp = json.loads(response.content)
        return resp

    @staticmethod
    def check_audio_distortion(token, s3_persistent_url):
        request = {"FileUrl": s3_persistent_url}
        response = requests.post(crpo_common_obj.pearson_domain +
                                 "/py/common/voice_distortion/check_audio_distortion/",
                                 headers=token,
                                 data=json.dumps(request, default=str), verify=False)
        resp = json.loads(response.content)
        return resp


crpo_common_obj = CrpoCommon()
