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

response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'cookies-bucket',
            'Name': 'JK.jpg' # Input Image
        }
    },
    TargetImage={
        'S3Object': {
            'Bucket': 'cookies-bucket',
            # 'Name': 'JiJinJung.jpg' # 비교 대상 이미지 # 같은 사람이 있는 사진 -> FaceMatches 값과 UnmatchedFaces 값이 출력된다
            'Name': 'JM_V2.jpg' # 같은 사람이 없는 사진 -> UnmatchedFaces 값만 출력된다  # JM_V 사진은 Input Image 속 사람과 사진이 비슷하게 나왔는지 FaceMatches 값도 출력됐다(원래는 다른 사람)
        }
    }
                                                    )

for key, value in response.items():
    if key in ('FaceMatches', 'UnmatchedFaces'):
        print(key)
        for att in value:
            print(att)
