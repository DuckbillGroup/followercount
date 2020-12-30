# followercount

This project contains source code and supporting files for a app that's ostensibly counting how many Twitter followers a given Twitter account has over time, but in practice is a testbed serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- mr_popular - Code for the application's Lambda function.
- events - An invocation event that you can use to invoke the function.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and a DynamoDB table. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

You will need to get a Twitter [bearer token](https://developer.twitter.com/en/docs/authentication/overview) to query the Twitter API. This should be stored in Systems Manager Parameter Store with a key of `TWITTER_BEARER_TOKEN`. 

You will further be asked during a guided deployment what Twitter account you wish to monitor. Multiple accounts can be selected via the syntax `account1,account2,account3`. It will default to my account "Quinnypig" because it is the most important Twitter account of all.

## Licensing

This project is licensed under MongoDB's SSPL because I am shit-scared of AWS competing with me, and am suffering delusions of grandeur that AWS would:

a. care enough to fork this codebase to do it  
b. fail to understand how terrible the code itself is  
c. value a "counting twitter followers" app in the slightest


But licensing isn't about making things useful for others nearly so much as it is about my own ego stroking, so the SSPL is clearly the license choice for me. Therefore, you are welcome to do anything you'd like with this code EXCEPT FOR YOU, LARGE CLOUD PROVIDERS. 
