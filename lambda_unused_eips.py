import boto3
import json

def lambda_handler(event, context):
    region_list=['us-east-1','ap-south-1','us-west-1','us-east-2']
    for region in region_list:
        ec2 = boto3.client('ec2',region_name=region)
        addresses = ec2.describe_addresses()
        print(addresses)
        eip_list = addresses['Addresses']
        print(len(eip_list))
        if len(eip_list) != 0:
            for eip in eip_list:
                allocation_id = addresses['Addresses'][0]['AllocationId']
                print("Allocation id is",allocation_id)
                instance_id = addresses ['Addresses'][0]['InstanceId']
                print("Instance Id is",instance_id)
                network_interface_id = addresses['Addresses'][0]['NetworkInterfaceId']
                print("NetworkInterfaceId",network_interface_id)
        else:
            print("No EIP Found, region")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
