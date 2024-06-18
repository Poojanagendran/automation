from SCRIPTS.COMMON.dbconnection import *
import datetime


class ResetTestUser:

    def __init__(self):
        print(datetime.datetime.now())

    def reset_test_users(self):
        # resetting test users to there previous state
        db_connection = ams_db_connection()
        cursor = db_connection.cursor()

        # CASE 4 (PASSWORD_EXPIRED_TO_PASSWORD_DISABLED) Attending_to_Password_Disabled
        # Test level is_password_never_expire flag should not be enabled
        update_tuser4 = "update test_users set status = 4, is_password_disabled = 0  where id = 3741833 and test_id = "\
                        "19299 and candidate_id = 1552023; "
        print(update_tuser4)
        cursor.execute(update_tuser4)
        db_connection.commit()

        # CASE 5 (SUBMIT_PASSWORD_NEVER_EXPIRED) Attending_to_Attended
        # Test level is_password_never_expire flag should be enabled
        update_tuser5 = "update test_users set status = 4, log_out_time = NULL where id = 3741983 and test_id = 19313 "\
                        "and candidate_id = 1551969; "
        print(update_tuser5)
        cursor.execute(update_tuser5)
        db_connection.commit()

        # CASE 6 (SUBMIT_PASSWORD_DISABLED) Password_Disabled_to_Attended
        # Test level is_password_never_expire flag should not be enabled
        update_tuser6 = "update test_users set status = 5, is_password_disabled = 1, log_out_time = NULL where id = " \
                        "3741837 and test_id = 19299 and candidate_id = 1552027; "
        print(update_tuser6)
        cursor.execute(update_tuser6)
        db_connection.commit()

        # CASE 7 (ATTENDED_INITIATE_AUTOMATION) Attended_to_Attended_With_Inititate_Automation
        update_tuser7 = "update test_users set total_score = NULL, percentage = NULL, correct_answers = NULL, " \
                        "in_correct_answers = NULL, un_attended_questions=NULL, is_partially_evaluated = NULL, " \
                        "eval_status = NULL, eval_by = NULL, eval_on = NULL, json_config = NULL, automation_task_id = "\
                        "NULL, automation_info = NULL, evaluation_info = NULL where id = 3741839 and test_id = 19299 " \
                        "and candidate_id = 1552029 "
        print(update_tuser7)
        cursor.execute(update_tuser7)
        db_connection.commit()

        update_applicant_status7 = "update applicant_statuss set comments = NULL where id = 1330487 and candidate_id ="\
                                   "1552029 and tenant_id= 1787; "
        print(update_applicant_status7)
        cursor.execute(update_applicant_status7)
        db_connection.commit()

        db_connection.close()


reset_test_user_obj = ResetTestUser()
# print(datetime.datetime.now())
