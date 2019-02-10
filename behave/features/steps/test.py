from behave import *
import requests
import sys
import json

def write_debug_file(filename,var_list):
    fh = open(filename, "w")
    for var in var_list:
       fh.writelines(var)
       fh.writelines("\n")
    fh.close()

@given('api {api} is up and running')
def step_impl(context, api):
    context.url = api
    pass

@when(u'we call the api with this JSON request')
def step_impl(context):
    input_json = context.text
    response = requests.get(context.url)
    my_json = (response.content).decode('utf8').replace("'", '"')
    # Load the JSON to a Python list & dump it back out as formatted JSON, sorted for compare below
    data = json.loads(my_json)
    context.compare_response = json.dumps(data, sort_keys=True)
    # write_debug_file("output.txt",[context.compare_response])
    # todo: check call was successful
    assert True is not False

@then(u'we expect this JSON response')
def step_impl(context):
    # write_debug_file("expected.txt", [context.text, actual_json])
    assert (json.loads(context.text) == json.loads(context.compare_response)) is True

