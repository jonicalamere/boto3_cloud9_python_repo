import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='jlamere-boto-06212023')
    
print(response)