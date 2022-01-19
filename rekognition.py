import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'smiling_girl.jpg'

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name="ap-northeast-2") # S3 Bucket의 AWS region과 동일하게 설정

response = client.detect_faces(Image={'S3Object': {
            'Bucket': 'cookies-bucket',
            'Name': photo,
        }},
                                Attributes = ['ALL'] # AgeRange, Smile 포함시키기 위해 Attributes 설정
                                                    )

print(response)
