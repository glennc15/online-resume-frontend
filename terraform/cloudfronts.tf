# This cloudfront distribution is for glenn15.com:
resource "aws_cloudfront_distribution" "domain" {
  origin {
    domain_name              = aws_s3_bucket.domain.bucket_regional_domain_name
    origin_id                = aws_s3_bucket.domain.id
    origin_access_control_id = aws_cloudfront_origin_access_control.domain.id
  }

  enabled             = true
  default_root_object = "index.html"

  aliases = ["glenn15.com"]

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = aws_s3_bucket.domain.id

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl     = 0
    default_ttl = 3600
    max_ttl     = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["US", "CA", "GB", "DE"]
    }
  }

  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate_validation.cert.certificate_arn
    ssl_support_method  = "sni-only"
  }
}

resource "aws_cloudfront_origin_access_control" "domain" {
  name                              = "s3-OAC"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"

}

# This cloudfront distribution is for www.glenn15.com redirect bucket:
resource "aws_cloudfront_distribution" "redirect" {
  origin {
    # when using the bucket URL you have to specify "custom_origin_config" too:
    origin_id = aws_s3_bucket.redirect.id
    domain_name = aws_s3_bucket.redirect.website_endpoint
    custom_origin_config {
      origin_protocol_policy = "http-only"
      http_port = "80"
      https_port = "443"
      origin_ssl_protocols = [ "TLSv1.2" ]

    }
  }

  enabled             = true

  aliases = ["www.glenn15.com"]

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = aws_s3_bucket.redirect.id

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl     = 0
    default_ttl = 3600
    max_ttl     = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "whitelist"
      locations        = ["US", "CA", "GB", "DE"]
    }
  }

  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate_validation.cert.certificate_arn
    ssl_support_method  = "sni-only"
  }
}
