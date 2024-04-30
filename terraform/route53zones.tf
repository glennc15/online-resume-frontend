# My AWS hosted zone in Route 53:
data "aws_route53_zone" "glenn15" {
  name         = var.site_domain
  private_zone = false
}

# Added a certificate for https:
resource "aws_route53_record" "glenn15" {
  for_each = {
    for dvo in aws_acm_certificate.domain.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.glenn15.zone_id
}

# Alias record for glenn15.com -> cloudfront site distribution
resource "aws_route53_record" "domain" {
  zone_id = "Z05623773J60BNV4GEW5X"
  name    = "glenn15.com"
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.domain.domain_name
    zone_id                = aws_cloudfront_distribution.domain.hosted_zone_id
    evaluate_target_health = false
  }
}



# ACM Certificates:
resource "aws_acm_certificate" "domain" {
  domain_name               = var.site_domain
  subject_alternative_names = ["*.${var.site_domain}"]
  validation_method         = "DNS"

  tags = {
    name = var.site_domain
  }
}

resource "aws_acm_certificate_validation" "cert" {
  certificate_arn         = aws_acm_certificate.domain.arn
  validation_record_fqdns = [for record in aws_route53_record.glenn15 : record.fqdn]
}

