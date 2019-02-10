Feature: Testing API with JSON input/output

Scenario: test 1
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we call the api with this JSON request:
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then we expect this JSON response:
'''
{"userId": 1, "completed": false, "id": 1, "title": "delectus aut autem"}
'''

Scenario: test 2
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we call the api with this JSON request:
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then we expect this JSON response:
'''
{"userId": 1, 
"completed": false, 
"id": 1, "title": "delectus aut autem"}
'''

Scenario: test 3
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we call the api with this JSON request:
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then we expect this JSON response:
'''
{
   "userId": 1, 
   "completed": false, 
   "id": 1, 
   "title": "delectus aut autem"
}
'''

Scenario: test 4
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we call the api with this JSON request:
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then we expect this JSON response:
'''
{
   "completed": false, 
   "userId": 1, 
   "id": 1, 
   "title": "delectus aut autem"
}
'''

Scenario: test 5
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we call the api with this JSON request:
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then we expect this JSON response:
'''
{
   "userId": 1, 
   "completed": false, 
   "title": "delectus aut autem",
   "id": 1
}
'''
