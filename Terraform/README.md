#Installation of terraform on ubuntu

step-1: sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

step-2: wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null


step-3: gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint


step-4: echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list


step-5: sudo apt update

step-6: sudo apt-get install terraform


#Now Configure aws

step-1: create aws Access_Key_Id and Secret_Access_Key from aws console

step-2: aws configure
       Access_Key_Id: <"Access key which you got from aws conole">
       Secret_Access_Key: <"secret key which you got aws console">
       Region: <"Enter the region you need">
       Output: json

#now create the infrastructure using terraform

terraform init  --> To initialize your Terraform project

terraform validate --> checks the syntax and internal consistency of your Terraform files

terraform plan --> Running shows you a preview of what Terraform will do

terraform apply --> It will create the infrastructure
