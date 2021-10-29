### devops-10 student

### HW-7.2. Облачные провайдеры и синтаксис Terraform

---

1.</br>

```
[~/Documents/education/terraform/aws]$ aws configure list                                               *[main]
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************DZRY              env
secret_key     ****************pGcx              env
    region                us-west-2      config-file    ~/.aws/config
```

2.</br>
В данном задании будет использоваться провайдер *aws*</br>

```
[~/Documents/education/terraform_netology]$ terraform apply              [main]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.my_aws_ubuntu will be created
  + resource "aws_instance" "my_aws_ubuntu" {
      + ami                                  = "ami-03d5c68bab01f3496"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "name"  = "netology_terraform"
          + "owner" = "Nikita Vinogradov"
        }
      + tags_all                             = {
          + "name"  = "netology_terraform"
          + "owner" = "Nikita Vinogradov"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification {
          + capacity_reservation_preference = (known after apply)

          + capacity_reservation_target {
              + capacity_reservation_id = (known after apply)
            }
        }

      + ebs_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + snapshot_id           = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }

      + enclave_options {
          + enabled = (known after apply)
        }

      + ephemeral_block_device {
          + device_name  = (known after apply)
          + no_device    = (known after apply)
          + virtual_name = (known after apply)
        }

      + metadata_options {
          + http_endpoint               = (known after apply)
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = (known after apply)
        }

      + network_interface {
          + delete_on_termination = (known after apply)
          + device_index          = (known after apply)
          + network_interface_id  = (known after apply)
        }

      + root_block_device {
          + delete_on_termination = (known after apply)
          + device_name           = (known after apply)
          + encrypted             = (known after apply)
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags                  = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = (known after apply)
          + volume_type           = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_network         = (known after apply)
  + instance_private_ip_addr = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.my_aws_ubuntu: Creating...
aws_instance.my_aws_ubuntu: Still creating... [10s elapsed]
aws_instance.my_aws_ubuntu: Still creating... [20s elapsed]
aws_instance.my_aws_ubuntu: Still creating... [30s elapsed]
aws_instance.my_aws_ubuntu: Still creating... [40s elapsed]
aws_instance.my_aws_ubuntu: Creation complete after 43s [id=i-054770af67a71cd13]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

instance_account_id = "094316163368"
instance_network = "subnet-014f920c4641b1a15"
instance_private_ip_addr = "172.31.27.203"
instance_region = "us-west-2"
instance_user_id = "094316163368"
```
Консоль *aws* позволяет создать свой образ ami </br>

[git: terraform_netology](https://github.com/vinnirus/terraform_netology)

