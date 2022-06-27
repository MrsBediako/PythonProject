# PythonProject
In this project I went through the basics of python to provision AMI in the assigned regions(eu-west-2 - ami- 0d729d2846a86a9e7, eu-west-1 this ami- ami-0c1bc246476a5572b us-east-1 this ami ami-0022f774911c1d690) This project is for CloudRock Ltd is a multinational consultancy company that already has some infrastructure in AWS.

The below tasks were created in variable.py which is the main file for executing the project. 

#list of all the 3 amis and assign it to a variable called ami_list

#a for loop and loop through the ami_list variable and print each ami out

#atuple of all the 3 amis and assign it to a variable called regions_tuple

#a for loop and loop through the regions_tuple variable and print out the ami name if the region is equal to us-east-1

#a dictionary which is a key-value pair of region to ami and assign it to a variable called region_ami_dict

#a for loop and loop through the regions_tuple variable and print each region Import the boto3 library and get a list of available resources from your aws account using the get_available_resources() function
