Feature: showing off behave

Scenario: run a simple test
Given api https://jsonplaceholder.typicode.com/todos/1 is up and running
When we implement a test
'''
{
  "bucket": "jra.philadelphia.routes.s3bucket.useast.ohio",
  "directory": "dist_dec18",
  "inputfile": "dec18_test_input.csv"
}
'''
Then behave will test it for us!
'''
{
  "expected": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
'''
