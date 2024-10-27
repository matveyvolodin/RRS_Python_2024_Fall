from RRS_Python_2024_Fall.Python_project.lesson1_hw.api_tests.case.data.case import create_case_dict, updated_data
from RRS_Python_2024_Fall.Python_project.lesson1_hw.api_tests.utils.api_client import client


def test_get_reed_root():
    response = client.make_request("/",method="GET")
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})


def test_read_cases():
    response = client.make_request("/testcases", method="GET")
    response.status_code_should_be_eq(200)


def test_create_test_case():
    response = client.make_request("/testcases", method="POST",json=create_case_dict)
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(create_case_dict)


def test_read_test_case_by_id():
    tc_id = 22
    response = client.make_request(f"/testcases/{tc_id}", method="GET")
    response.status_code_should_be_eq(200)
    response.json_should_contains({"id": 22})


def test_update_test_case_via_put_method():
    tc_id = 22
    response = client.make_request(f"/testcases/{tc_id}", method="PUT", json=updated_data)
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(updated_data)


def test_delete_test_case():
    tc_id = 24
    response = client.make_request(f"/testcases/{tc_id}", method="DELETE")
    response.status_code_should_be_eq(200)
    response_get_by_id = client.make_request(f"/testcases/{tc_id}", method="GET")
    response_get_by_id.status_code_should_be_eq(404)

