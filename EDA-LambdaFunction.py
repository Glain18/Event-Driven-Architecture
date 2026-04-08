import json
import boto3

# Create an SNS client
sns_client = boto3.client('sns')

# Your SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:997622531752:ImageUploadNotification"

def lambda_handler(event, context):
    # Triggered when a new object is added to S3.
    # Sends a notification to SNS.
    
    try:
        # Loop through all S3 records in the event
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            # Create a simple message
            message = f"New file uploaded to S3 bucket:\nBucket: {bucket}\nFile: {key}"
            
            # Publish message to SNS
            response = sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject="S3 File Upload Notification"
            )
            
            print(f"Notification sent for file: {key}, SNS Message ID: {response['MessageId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('SNS notification sent successfully!')
        }
        
    except Exception as e:
        print(f"Error sending SNS notification: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }