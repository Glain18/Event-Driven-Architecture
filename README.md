AWS Event-Driven Architecture Project

Overview

This project demonstrates a serverless event-driven architecture on AWS.
When a file is uploaded to an Amazon S3 bucket, it automatically triggers an AWS Lambda function, which then publishes a notification using Amazon SNS.

This simulates real-time alerting and event-driven communication between services.

Architecture Flow:
S3 (File Upload) → Lambda (Processing) → SNS (Notification) → Email Subscriber

Technologies Used
 • Amazon S3
 • AWS Lambda
 • Amazon SNS
 • Amazon CloudWatch
 • AWS IAM

Features
 • Automatic trigger on file upload (S3 event notification)
 • Serverless processing using AWS Lambda
 • Real-time notifications via Amazon SNS
 • Email alerts for uploaded files
 • Scalable and loosely coupled architecture

 Implementation Steps
 1. Created an S3 bucket for file uploads
 2. Developed a Lambda function to process S3 events
 3. Configured S3 to trigger Lambda on file upload
 4. Created an SNS topic
 5. Subscribed an email endpoint to the SNS topic
 6. Updated Lambda to publish messages to SNS
 7. Tested by uploading files and receiving email alerts

 Testing
 • Uploaded files to S3
 • Verified Lambda execution in CloudWatch
 • Confirmed email notification via SNS

 Security
 • IAM roles configured with least-privilege access
 • Secure SNS topic and S3 permissions
