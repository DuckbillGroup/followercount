import requests
import os
import boto3
import time

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

ssm_client = boto3.client('ssm')
ssm_parameter = ssm_client.get_parameter(Name='TWITTER_BEARER_TOKEN', WithDecryption=True)

def set_bearer_token():
    return ssm_parameter['Parameter']['Value']


def create_url(twooters):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=" + twooters
    user_fields = "user.fields=public_metrics"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = f"https://api.twitter.com/2/users/by?{usernames}&{user_fields}"
    return url


def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()


table = boto3.resource('dynamodb').Table(os.environ.get("TABLE_NAME"))
twooters = os.environ.get("TWITTER_ACCOUNTS")
url = create_url(twooters)
headers = create_headers(set_bearer_token())

def handler(event=None, context=None):
    json_response = connect_to_endpoint(url, headers)
    with table.batch_writer() as batch:
        for item in json_response['data']:
            batch.put_item(
                Item={
                    'twitter_handle': item['username'],
                    'EpochTime': int(time.time()),
                    'followers': item['public_metrics']['followers_count']
                }
            )


if __name__ == "__main__":
    handler()
