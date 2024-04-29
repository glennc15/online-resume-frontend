output "site_bucket_name" {
  description = "Name of the S3 bucket used for the site CDN."
  value = aws_s3_bucket.site.id
}

output "www_site_bucket_name" {
  description = "Name of the S3 bucket used for www redirects to the site CDN."
  value = aws_s3_bucket.www.id
}


output "cloudfront_domain_name" {
    description = "The Cloudfront domain name"
    value = aws_cloudfront_distribution.dist.domain_name
}
