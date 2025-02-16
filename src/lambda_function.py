import boto3
import json
import os

# S3 クライアントを作成
s3 = boto3.client("s3")

# S3 バケット名（環境変数として Lambda に設定可能）
BUCKET_NAME = "7110-mybucket-9dd968df-ba1a-1cab-c01c-612410b09e42"

def lambda_handler(event, context):
    try:
        # リクエストからファイル名を取得
        body = json.loads(event["body"])
        file_name = body["file_name"]
        
        # Presigned URL を生成（有効期限: 1時間）
        presigned_url = s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": BUCKET_NAME, "Key": file_name, "ContentType": "image/jpeg"},
            ExpiresIn=3600,
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"upload_url": presigned_url}),
            "headers": {"Content-Type": "application/json"},
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }

