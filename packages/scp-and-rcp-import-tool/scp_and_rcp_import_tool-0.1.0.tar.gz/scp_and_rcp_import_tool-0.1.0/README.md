**Existing AWS SCPs and RCPs import tool**

A command line tool to import existing SCPs and RCPs into AWS CloudFormation templates using CloudFormation infrastructure as code generator (IaC generator). This allows you to to automate the management of your SCPs and RCPs at scale.

**Important:** This solution is not designed for Control Tower managed policies. This solution should only be used for policies created outside of Control Tower. Changes made to Control Tower resourcesoutside of Control Tower can cause drift and affect AWS Control Tower functionality in unpredictable ways.