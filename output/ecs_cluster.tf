{
  "data": {
    "aws_availability_zones": {
      "all": {}
    }
  },
  "resource": {
    "aws_alb": {
      "alb": {
        "availability_zones": [
          "${data.aws_availability_zones.all.names}"
        ],
        "lifecycle": {
          "create_before_destroy": true
        },
        "name": "myEcsCluster",
        "security_groups": [
          "${aws_security_group.sg-alb.id}"
        ]
      }
    },
    "aws_ecs_cluster": {
      "cluster": {
        "name": "myEcsCluster"
      }
    },
    "aws_launch_configuration": {
      "lc": {
        "image_id": "ami-091bf462afdb02c60",
        "instance_type": "t2.nano",
        "lifecycle": {
          "create_before_destroy": true
        },
        "security_groups": [
          "${aws_security_group.sg-instance.id}"
        ]
      }
    },
    "aws_security_group": {
      "sg-alb": {
        "name": "myEcsCluster-alb"
      },
      "sg-instance": {
        "name": "myEcsCluster-instance"
      }
    },
    "aws_security_group_rule": {
      "all_outbound": {
        "cidr_blocks": [
          "0.0.0.0/0"
        ],
        "from_port": 0,
        "protocol": "-1",
        "security_group_id": "${aws_security_group.sg-alb.id}",
        "to_port": 0,
        "type": "egress"
      },
      "http_inbound": {
        "cidr_blocks": [
          "0.0.0.0/0"
        ],
        "from_port": 80,
        "protocol": "tcp",
        "security_group_id": "${aws_security_group.sg-alb.id}",
        "to_port": 80,
        "type": "ingress"
      },
      "server_http_inbound": {
        "cidr_blocks": [
          "0.0.0.0/0"
        ],
        "from_port": 8080,
        "protocol": "tcp",
        "security_group_id": "${aws_security_group.sg-instance.id}",
        "to_port": 8080,
        "type": "ingress"
      }
    }
  }
}