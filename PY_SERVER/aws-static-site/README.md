# aws-static-site
A collection of files that can be used to automate the provisioning and deployment of static websites to AWS S3. 

Some requirements to use the cloudfomration template:

1. You need a hosted zone configured for your domain within route 53
2. You'll need access to the email for the domain (depending on the domain type and various settings you may need one of the following emails)
  * administrator@example.com
  * webmaster@example.com
  * hostmaster@example.com
  * admin@example.com
  * postmaster@example.com

After you have met the requirements simply upload the template to AWS cloudformation, enter the stack name, and the root domain when prompted.
After a few minutes of launching the cloud formation stack you should get an email requesting authorization for the TLS certificate. Approve the request and wait for the rest of the stack to complete it's provisioning. 

Once the stack is created edit the deployment script to match the details of your deployment. 

Once you run the deployment script it may take some time for cloudfront to register the uploaded files.
