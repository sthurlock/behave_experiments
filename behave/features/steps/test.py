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
    response = requests.get(context.url)
    my_json = (response.content).decode('utf8').replace("'", '"')

    # Load the JSON to a Python list & dump it back out as formatted JSON, sorted for compare below
    data = json.loads(my_json)
    context.compare_response = json.dumps(data, sort_keys=True)

    fh = open("output.txt", "w")
    fh.writelines(context.compare_response)
    fh.writelines("\n2")
    fh.close()
    # fh.writelines(input_json)
    # fh.writelines("\n3")
    # fh.writelines(r)
    # fh.writelines("\n4")
    # print("input:" , input_json)

    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    actual_json = context.compare_response

    expected_json = context.text
    ej1 = expected_json.replace('\\', '')
    exp = json.dumps(ej1, sort_keys=True)

    j = "{ 'glossary': { 'title': 'example glossary', 'GlossDiv': { 'title': 'S', 'GlossList': { 'GlossEntry': { 'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'Standard Generalized Markup Language', 'Acronym': 'SGML', 'Abbrev': 'ISO 8879:1986', 'GlossDef': { 'para': 'A meta-markup language, used to create markup languages such as DocBook.', 'GlossSeeAlso': ['GML', 'XML'] }, 'GlossSee': 'markup' } } } } }"


    d = json.loads(j.replace("'", '"'))
    t = d['glossary']['title']

    fh = open("expected.txt", "w")
    fh.writelines(t)
    # fh.writelines("\n")
    fh.writelines(context.text)
    # fh.writelines("\nexp['completed:']:")
    # fh.writelines(exp['completed'])
    fh.writelines("\nej1:")
    fh.writelines(ej1)
    # fh.writelines(type(ej1))
    fh.writelines("\nexp:")
    fh.writelines(exp)
    fh.writelines(exp)
    fh.writelines("\n")
    fh.writelines( actual_json )
    # fh.writelines( type(actual_json) )
    fh.writelines("\n")
    fh.close()

    assert (exp == actual_json) is True

    # # print("expected: ", expected_json)
    # assert context.failed is False
    # fh = open("actual.txt", "wb")
    # json.dump(actual_json, fh)
    # fh.writelines("\n")
    # fh.close()



# try: except Exception as ex: print(ex)

