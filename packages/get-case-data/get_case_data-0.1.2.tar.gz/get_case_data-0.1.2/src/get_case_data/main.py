import argparse
import datetime
import getpass

import tqdm

from get_case_data.funcs.apitools import get_bank_account_by_case_id, get_case_detail_by_case_id, get_case_detail_by_inst_id, get_related_cases_by_data_id
from get_case_data.funcs.auth import login
from get_case_data.funcs.exceltools import create_excel_file


def create_case_report(selected_case):
    # ============================= MAIN CASE DATA =============================
    case_informations_headers = ("เลขคดี", "จำนวนเคสที่เกี่ยวข้อง", "รายละเอียด", "Link", "Case ids ที่เกี่ยวข้อง")
    case_informations_body = [
        (
            selected_case.get("TrackingCode", ""),
            len(selected_case.get("related_cases", [])),
            selected_case.get("OptionalData", ""),
            f"(https://officer.thaipoliceonline.go.th/pct-in/officer/task-admin-view/{selected_case.get('InstId')}#task-admin)",
            ", ".join([itm.get("CASE_NO") for itm in selected_case.get("related_cases", [])]),
        )
    ]
    create_excel_file(case_informations_headers, case_informations_body, selected_case.get("TrackingCode", "selected_case"))
    # ============================= RELATED CASE DATA =============================
    related_cases_headers = ("เลขรับแจ้งความ", "ประเภท", "หน่วยงานที่รับผิดชอบ", "สถานะ", "มูลค่าความเสียหาย", "รายละเอียด")
    related_cases_body = [
        (itm.get("CASE_NO", ""), itm.get("CASE_TYPE_ABBR", ""), itm.get("ORG_NAME", ""), itm.get("COUNT_RATE", ""), itm.get("DAMAGE_VALUE", ""), itm.get("CASE_BEHAVIOR", ""))
        for itm in selected_case.get("related_cases", [])
    ]
    create_excel_file(related_cases_headers, related_cases_body, f"{selected_case.get('TrackingCode', '')}_related_cases")
    # ============================= RELATED CASE DATA =============================
    related_cases_headers = ("เลขรับแจ้งความ", "ประเภท", "หน่วยงานที่รับผิดชอบ", "สถานะ", "มูลค่าความเสียหาย", "รายละเอียด")
    related_cases_body = [
        (itm.get("CASE_NO", ""), itm.get("CASE_TYPE_ABBR", ""), itm.get("ORG_NAME", ""), itm.get("COUNT_RATE", ""), itm.get("DAMAGE_VALUE", ""), itm.get("CASE_BEHAVIOR", ""))
        for itm in selected_case.get("related_cases", [])
        if any(keyword in itm.get("ORG_NAME", "") for keyword in ["สอท.", "ตอท."])
    ]
    create_excel_file(related_cases_headers, related_cases_body, f"{selected_case.get('TrackingCode', '')}_ccib_related_cases")
    # ============================= BANK DATA =============================
    bank_account_headers = ["เลขบัญชี", "ชื่อบัญชี", "ธนาคาร"]
    bank_account_body = [(itm.get("BANK_ACCOUNT", ""), itm.get("BANK_ACCOUNT_NAME", ""), itm.get("BANK_NAME", "")) for itm in selected_case.get("bank_accounts", [])]
    create_excel_file(bank_account_headers, bank_account_body, f"{selected_case.get('TrackingCode', '')}_bank_account")


def process_case_details(selected_case, token):
    idx_related_case = 0
    for case in tqdm.tqdm(selected_case.get("related_cases", []), "Fetching related case with information"):
        case_id = case.get("CASE_ID", 0)
        if case_id:
            case_detail = get_case_detail_by_case_id(token, case_id)
            selected_case["related_cases"][idx_related_case] = {**case, **case_detail}
        idx_related_case += 1

    selected_case["bank_accounts"] = get_bank_account_by_case_id(token, selected_case.get("detail", {}).get("DATA_ID", 0))


def main():
    parser = argparse.ArgumentParser(description="Get data from API")
    parser.add_argument("-u", "--username", required=True, help="USERNAME")
    parser.add_argument("-p", "--password", type=str, help="PASSWORD")
    parser.add_argument("-c", "--case_id", help="XXXXXX")
    args = parser.parse_args()

    username = args.username
    password = args.password or getpass.getpass("Enter password: ")
    case_id = args.case_id

    token = login(username, password)

    if token:
        inst_id = case_id
        selected_case = {"InstId": case_id}
        case_detail = get_case_detail_by_inst_id(token, inst_id)

        selected_case["detail"] = case_detail[0] if case_detail else {}
        selected_case["TrackingCode"] = selected_case.get("detail", {}).get("TRACKING_CODE")

        data_id = selected_case["detail"].get("DATA_ID", 0)
        related_cases = get_related_cases_by_data_id(token, data_id) if data_id else []
        selected_case["related_cases"] = related_cases

        process_case_details(selected_case, token)
        create_case_report(selected_case)

        print(f"INFO: xlsx exported {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
