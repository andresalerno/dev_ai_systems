## My studies about API requests from OpenAi

### 1. Challenges of a production environment

- Error Handling
    - Displaying user-friendly error messages
    - Alternatives for when the service is unavailable

- Moderation and Safety
    - Control unwanted inputs
    - Minimizing the risk of data leaks

- Testing and Validation
    - hecking for responses that are out of topic
    - Testing for inconsistent behavior

- Testing and Validation
    - Checking for responses that are out of topic
    - Testing for inconsistent behavior

### 2. Handling errors

- Connection errors
    - Generally due to connection issues on either the user's or the service's side
    - Examples: InternalServerError , APIConnectionError , APITimeoutError
    - Potential solution:
        - Checking your connection configuration
        - Reaching out to support if that fails

- Resource limits erros
    - Generally due limits on the frequency of requests or the amount of text passed
    - Examples: ConflictError , RateLimitError
    - Potential solution:
        - Checking limit restrictions
        - Ensure requests are within limits

- Authentication errors
    - Definition: your API key or token was invalid, expired or revoked
    - Possible solution: check that your API key or token is correct and has not been revoked or expired

- Bad request errors
    - Definition: your request is missing required parameters or some of the parameters are invalid
    - Possible solution: double check the variables and parameters you are passing as input and ensure they are valid and in the correct format

- Rate limit errors
    - Definition: you have exceeded the number of requests you can send within a given time
    - Possible solution: decrease the number of requests you are sending to the API within a given time

Cenario:

You are working at a logistics company on developing an application that uses the OpenAI API to check the shipping address of your top three customers. The application will be used internally and you want to make sure that other teams are presented with an easy to read message in case of error.

To address this requirement, you decide to print a custom message in case the users fail to provide a valid key for authentication, and use a try and except block to handle that.

The message variable has already been imported.