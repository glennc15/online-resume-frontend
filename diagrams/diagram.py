# diagram.py
from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

from diagrams.onprem.client import Users, User
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.security import ACM
from diagrams.generic.blank import Blank

from diagrams.aws.analytics import CloudsearchSearchDocuments

from diagrams.aws.network import APIGateway
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.database import DDB



with Diagram("AWS Architecture for glenn15.com", show=False):

    # Users() << Route53("www.glenn15.com") >> CloudFront("redirect") >> S3("redirects to glenn15.com")
    # Route53("glenn15.com") >> CloudFront("domain") >> S3("glenn15.com")


    this_route53 = Route53()
    this_acm = ACM()
    # index_html = CloudsearchSearchDocuments("index.html")
    # api_gateway = APIGateway()




    # Blank() >> Edge() << api_gateway << Edge() >> LambdaFunction() << Edge() >> DDB()


    # Users() >> this_route53

    Blank() >> this_acm >> Blank() >> Blank()

    this_acm >> this_route53

    User() << Edge() >> this_route53 << Edge() >> CloudFront("CDN") << Edge() >> S3("S3\nhttps://glenn15.com")

    # index_html << this_route53




    # index_html << this_route53

    # Edge(label="http://www.glenn15.com\nor\nhttps://www.glenn15.com")


    # index_html >> api_gateway



    # this_ACM << Edge() >> this_route53
    # Users() << Edge(label="http://glenn15.com\nor\nhttps://glenn15.com") >> Route53() << Edge() >> CloudFront("CDN") << Edge() >> S3("glenn15.com\nEndpoint")

    # ACM() << Edge() >> site_route53