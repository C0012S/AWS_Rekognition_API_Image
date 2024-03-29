import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'TomHolland_and_Zendaya.jpg'

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name="ap-northeast-2") # S3 Bucket의 AWS region과 동일하게 설정

response = client.recognize_celebrities(Image={'S3Object': {
            'Bucket': 'cookies-bucket',
            'Name': photo,
        }}
                                                    )

# print(response) # 한 사람의 결과만 출력한다
for key, value in response.items(): # 전체 사람의 결과를 출력한다
    if key == 'CelebrityFaces':
        for people in value:
            print(people)
