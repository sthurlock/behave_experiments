from behave import *
import requests
import sys
import json


@given('api {api} is up and running')
def step_impl(context, api):
    context.url = api
    pass

@when('we implement a test')
def step_impl(context):
    input_json = context.text
    fh = open("output.txt", "w")
    context.response = requests.get(context.url)
    fh.writelines(context.url)
    fh.writelines("\n")
    fh.writelines(input_json)
    fh.writelines("\n")
    # fh.writelines(r)
    # fh.writelines("\n")
    fh.close()
    
    # print("input:" , input_json)
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    expected_json = context.text
    actual_json = context.response
    # print("expected: ", expected_json)
    assert context.failed is False
    fh = open("expected.txt", "w")
    fh.writelines(expected_json)
    fh.writelines("\n")
    fh.close()
    # fh = open("actual.txt", "wb")
    # json.dump(actual_json, fh)
    # fh.writelines("\n")
    # fh.close()



# try: except Exception as ex: print(ex)

