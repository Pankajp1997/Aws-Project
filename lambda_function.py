import boto3 
# For extraction of the volume id we are using new function 
def get_volume_id_from_arn (volume_arn):
    # split the ARN using the colon (':'') separator 
    arn_ports = volume_arn.split(':')
    # The volume ID is the last part of the ARN after the 'volume/'' prefix. 
    volume_id = arn_ports[-1].split('/')[-1]
    return volume_id
    
  def lambda_handler(event, context):
    # parsing the info
   volume_arn = event['resources'][0]
   volume_id = get_volume_id_from_arn(volume_arn)
   
   ec2_client = boto3.client('ec2')
   response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',      
)
