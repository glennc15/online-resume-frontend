'''

1. make two s3 buckets:
    a. 1st bucket name is glennc.com
    b. 2nd bucket name is www.glennc.com <- index page goes in this bucket.

2. in www.glennc.com bucket:
    a. disable block public access
    b. add a bucket policy that allows GET access:

    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::www.glennc.com/*"
            ]
        }
    ]
}

3. enable static website hosting on www.glennc.com bucket (under bucket properties).

4. enable static website hosting on glennc.com bucket (under bucket properties).
    For hosting type select:
    a. Redirect requests for an object
    b. Host name -> www.glennc.com
    c. Protocol -> http

5. create two new records for the domain name in Route 53
    - 1st record:
        a. use the simple routing wizard.
        b. define simple record.
        c. subdomain -> www
        d. Record type -> A - Routes traffic to an IPv4 address and some AWS resources
        e. Value/Route traffic to
            1) Alias to S3 website endpoint
            2) [same region as bucket]
            3) s3-website-us-east-1.amazonaws.com
        f. Evaluate target health -> No

    - 2nd record:
        a. use the simple routing wizard.
        b. define simple record.
        c. subdomain -> [blank]
        d. Record type -> A - Routes traffic to an IPv4 address and some AWS resources
        e. Value/Route traffic to
            1) Alias to S3 website endpoint
            2) [same region as bucket]
            3) s3-website-us-east-1.amazonaws.com
        f. Evaluate target health -> No

8. Create a certificate in AWS Certificate Manager
    a. select "Request a public certificate"
    b. Fully qualified domain name -> www.glenn15.com & glenn15.com
    c. keep the rest of the default configurations.

9. In ACM under the new certificate click "Create records in Route 53" -> should see 2 new records in Route 53 now.

10. Create a CloudFront distribution:
    a. Origin domain -> S3 bucket host name (under properties)
    b. Viewer protocol policy -> Redirect HTTP to HTTPS
    c. Custom SSL certificate -> should see the certificate we just created in the drop down.
    d. Alternate domain name (CNAME) -> www.glenn15.com
    e. Web Application Firewall (WAF) -> Do not enable security protections

11. Create a CloudFront distribution for the 2nd bucket
    a. Origin domain -> S3 bucket host name (under properties)
    b. Viewer protocol policy -> Redirect HTTP to HTTPS
    c. Custom SSL certificate -> should see the certificate we just created in the drop down.
    d. Alternate domain name (CNAME) -> glenn15.com
    e. Web Application Firewall (WAF) -> Do not enable security protections

13. Set S3 Protocol -> https (under S3 properties)

14. Update A records in Route 53
    a. Route traffic to -> Alias to CloudFront distribution
    b. CloudFrond distribution -> [distribution from CloudFront. Can be found under CloudFront Domain Name or is probably auto populated]

'''