import json
import os

facts ={
    "inventory" : {
            "device": [
                {
                    "name" :  "csr1kv1",
                    "version" : "16.09",       
                    "vendor" : "cisco",
                    "uptime" : "2 days",
                    "serial" : "XB96861",
                    "snmp" : [
                             { "name" : "public" , "permission" : "ro" },
                             {"name" : "private" , "permission" : "rw" }
                    ],
                    "vlan_id" : [
                        {"name" : "HR" , "id" : "100"}  
                    ]
                    }
            ]
        }
   }

facts_str = json.dumps(facts)
print(facts)
print(type(facts))
print(facts['inventory']['device'][0]['uptime'])
print(facts_str)
print(type(facts_str))
print(json.dumps(facts, indent = 4))

vlan_id = '{"name" : "HR" , "id" : "100"}'
interfaces = '[ "Gig0/1" , "Gig0/2" ,"Gig0/3","Gig0/4" ]'
print(vlan_id)
print(interfaces)
vlan_num = json.loads(vlan_id) 
print(vlan_num['id'])
print(type(vlan_num))
interface_names = json.loads(interfaces)

for i in range(0,4):
    print(interface_names[i])

