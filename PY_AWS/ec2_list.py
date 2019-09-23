import boto3
#without session 

ec2_ob=boto3.resource('ec2')
 
for each_in in ec2_ob.instances.all():
    print(each_in.id)
