import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

# photo = 'hot_air_balloon.jpg' # ModerationLabels 없다
photo = 'beyonce.jpg'

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name="ap-northeast-2") # S3 Bucket의 AWS region과 동일하게 설정

response = client.detect_moderation_labels(Image={'S3Object': {
            'Bucket': 'cookies-bucket',
            'Name': photo,
        }}
                                #, MinConfidence=9 # MinConfidence가 95보다 작으면 ModerationLabels 없다
                                                    )

print(response)