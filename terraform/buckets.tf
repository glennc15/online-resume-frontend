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

# This bucket is an endpoint for a redirect from www.glennc15.com => glennc15.com:
resource "aws_s3_bucket" "redirect" {
  bucket = "www.glenn15.com"
}

resource "aws_s3_bucket_website_configuration" "redirect" {
  bucket = aws_s3_bucket.redirect.id

  redirect_all_requests_to {
    host_name = "glenn15.com"
  }

}


