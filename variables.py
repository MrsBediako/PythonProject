# AMI to be provisioned in
#eu-west-2: ami- 0d729d2846a86a9e7
#in eu-west-1: ami-0c1bc246476a5572b
#In, us-east-1: ami-0022f774911c1d690

 #list of all 3 amis assigned the variable called ami_list
ami_list =  ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
print (ami_list)

#for loop 
ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
for ami in ami_list :
      print ("ami list")
      print(ami)

#creating a tuple for regions
regions_tuple = ("eu-west-2","eu-west-1","us-east-1")

for region in regions_tuple:
     print (region)          
     if region == "us-east-1":
        print ("the region is equal to us-east-1")     

#creating a dictionary called region_ami_dict
region_ami_dict = {"eu-west-2" :"ami- 0d729d2846a86a9e7", "eu-west-1" : "ami-0c1bc246476a5572b", "us-east-1" : "ami-0022f774911c1d690"}
print (region_ami_dict)

#for loop and loop through the region_ami_dict and each key pair value
for dict in region_ami_dict.items():
     print (dict)