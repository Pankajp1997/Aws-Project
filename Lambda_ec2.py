import boto3

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    
    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        InstanceType={
            'Value': 't2.medium'
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'Instance type modified successfully'
    }
