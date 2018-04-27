import boto3

ec2 = boto3.client('ec2', region_name='us-east-2')


instances = ec2.describe_instances()

dev = []
qa = []
prod = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        for tags in instance['Tags']:
            if(tags['Value'][:3]=='Dev'):
                dev.append(instance['InstanceId'])
                print(tags['Value'])
            elif(tags['Value'][:2]=='QA'):
                qa.append(instance['InstanceId'])
                print(tags['Value'])
            elif(tags['Value'][:4]=='Prod'):
                prod.append(instance['InstanceId'])
                print(tags['Value'])

ec2.create_tags(
    Resources=dev,
    Tags=[
        {
        'Key':'Running Environment',
        'Value':'9/5'
        }
    ]
)

ec2.create_tags(
    Resources=qa,
    Tags=[
        {
        'Key':'Running Environment',
        'Value':'24/5'
        }
    ]
)

ec2.create_tags(
    Resources=prod,
    Tags=[
        {
        'Key':'Running Environment',
        'Value':'24/7'
        }
    ]
)
