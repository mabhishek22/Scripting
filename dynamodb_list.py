
import boto.dynamodb
import boto.dynamodb.condition

#AWS setting

aws_region='us-west-2'

#connect to AWS
conn = boto.dynamodb.connect_to_region(aws_region)

#list all tables in dynamodb
awstables = conn.list_tables()



i=1

for item in awstables:
	
:quit

	c = "%d. %s"%(i,item)
	print c
	print ' '
	i+=1

# print awstables
