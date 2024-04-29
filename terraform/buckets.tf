# This bucket holds all the site files:
resource "aws_s3_bucket" "domain" {
  bucket = "glenn15.com"
}

resource "aws_s3_bucket_policy" "domain" {
    bucket = aws_s3_bucket.domain.id
    policy = <<EOF
    {
        "Version": "2012-10-17",
        "Statement": {
            "Sid": "AllowCloudFrontServicePrincipalReadOnly",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "${aws_s3_bucket.domain.arn}/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "${aws_cloudfront_distribution.domain.arn}"
                }
            }
        }
    }
    EOF
}