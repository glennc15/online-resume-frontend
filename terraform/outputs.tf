output "site_bucket_name" {
  description = "Name of the S3 bucket used for the site CDN."
  value       = aws_s3_bucket.domain.id
}

# output "www_site_bucket_name" {
#   description = "Name of the S3 bucket used for www redirects to the site CDN."
#   value       = aws_s3_bucket.www.id
# }


output "cloudfront_domain_name" {
  description = "The Cloudfront domain name"
  value       = aws_cloudfront_distribution.domain.domain_name
}


output "cloudfront_redirect_name" {
  description = "The Cloudfront redirect name"
  value = aws_cloudfront_distribution.redirect.domain_name
}

output "redirect_bucket_name" {
  value = aws_s3_bucket.redirect.website_endpoint
}

output "redirect_bucket_website_config" {
  value = aws_s3_bucket_website_configuration.redirect.website_domain
}