##  Python - Terraform - AWS

This repo uses [python-terrascript](https://github.com/mjuenema/python-terrascript) to generate Terraform scripts in an automated fashion using Python and uses [python-terraform](https://github.com/beelit94/python-terraform) to plan and apply the Terraform scripts against the AWS environment.


Basic idea:
```
usage: run.py [-h] [--plan <TEMPLATE_NAME>] [--apply <TEMPLATE_NAME>]
              {generate} ...

Generate, plan and apply terraform scripts in templates.

optional arguments:
  -h, --help            show this help message and exit
  --plan <TEMPLATE_NAME>, -p <TEMPLATE_NAME>
                        Plan given Terraform script.
  --apply <TEMPLATE_NAME>, -a <TEMPLATE_NAME>
                        Apply given Terraform script.

subcommands:
  Valid subcommands:

  {generate}
    generate            Generate Terraform scripts for the files listed in
                        templates/.
```

### Generate Terraform
```python
./run.py generate

```


## TO-DO:
### Planning and Applying Terraform


