# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."
  type        = string
  default     = "us-east-1"
}

variable "stack_base_name" {
  default = "online-resume"
}

variable "site_domain" {
  default = "glenn15.com"
}

