from terrascript import *
import terrascript.aws.r as r
import terrascript.aws.d as d

def ecs_cluster(cluster_name, instance_type, ami_id, min_size, max_size):
    """ECS Cluster Module"""

    # Cluster ECS
    #
    ecs_cluster = r.aws_ecs_cluster('cluster', name=cluster_name)

    # Security Group for the Application Load Balancer
    #
    sg_alb = r.aws_security_group('sg-alb', name='{}-alb'.format(cluster_name))

    r.aws_security_group_rule('http_inbound', security_group_id=sg_alb.id,
                              type='ingress', from_port=80, to_port=80,
                              protocol='tcp', cidr_blocks = ["0.0.0.0/0"])

    r.aws_security_group_rule('all_outbound', security_group_id=sg_alb.id,
                              type='egress', from_port=0, to_port=0,
                              protocol='-1', cidr_blocks = ["0.0.0.0/0"])
    
    # Security Group for the EC2 Instances in the Cluster
    #
    sg_cluster = r.aws_security_group('sg-instance', name='{}-instance'.format(cluster_name))

    r.aws_security_group_rule('server_http_inbound', security_group_id=sg_cluster.id,
                              type='ingress', from_port=8080, to_port=8080,
                              protocol='tcp', cidr_blocks = ["0.0.0.0/0"])

    # Launch configuration
    #
    launch_config = r.aws_launch_configuration('lc', image_id=ami_id,
                                               instance_type=instance_type,
                                               security_groups=[sg_cluster.id],
                                               lifecycle={
                                                   'create_before_destroy': True
                                               })

    # Availability zones
    #
    az = d.aws_availability_zones('all')


    # Application Load Balancer
    #
    alb = r.aws_alb('alb', name=cluster_name,
                    availability_zones=[az.names],
                    security_groups=[sg_alb.id],
                    lifecycle={
                        'create_before_destroy': True
                    })



    return ecs_cluster, sg_alb, sg_cluster, launch_config
