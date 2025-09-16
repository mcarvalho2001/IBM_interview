import ibm_boto3
from ibm_botocore.client import Config

# HMAC credentials (use these, not the IAM apikey)
access_key_id = "b3715dee3eb64aa88c5db9ddc82bde05"
secret_access_key = "777913063c22c2375697a27c21dec0466f6ea573a44d4f93"

# COS info
bucket_name = "somebucket-for-interview"
filename = "README.md"

# ✅ Use the Madrid region → eu-madrid (not eu-de)
service_endpoint = "https://s3.eu-es.cloud-object-storage.appdomain.cloud"


# Create COS resource with HMAC
cos = ibm_boto3.resource(
    "s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    config=Config(signature_version="s3v4"),
    endpoint_url=service_endpoint
)

# Download file
try:
    cos.Object(bucket_name, filename).download_file(filename)
    print(f"Downloaded {filename} from bucket {bucket_name}")
except Exception as e:
    print("Error:", e)
