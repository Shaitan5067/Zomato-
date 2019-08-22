######  First you have to install pyzomato library ####
###### Then you should have a Zomato API KEY ######

from pyzomato import Pyzomato
p = Pyzomato(YOUR API)

##### To get the details of pune city #######
p.getCityDetails(q='pune')


#### Now we will find the Cuisines available in Pune ####

x=p.getCuisines(city_id=5)
y=x.get('cuisines')
z=[]
for i in range(len(y)):
    z.append(y[i].get('cuisine'))
    
    
#####  Now we will search restaurant with the search function of pyzomato #####



data=[]
for i in range(len(z)):
    data.append(p.search(entity_id=5,entity_type='city',cuisines=(z[i].get('cuisine_id'))))
    
 #### Here we will get data in form of json #####
 
latitude=[]
longitude=[]


### The data which we got is in the form of nested dictionary so we have to extract latitude and longitude from that nested dictionart ##### 


for i in range(len(data)):
    abc=data[i].get('restaurants')
    for j in range(len(abc)):
        pqr=abc[j].get('restaurant')
        xyz=pqr.get('location')
        latitude.append(xyz.get('latitude'))
        longitude.append(xyz.get('longitude'))
        
import pandas as pd
df=pd.DataFrame(latitude)
df['latitude']=df.to_csv(r"path.csv")
pf=pd.DataFrame(longitude)
pf['longitude']=pf.to_csv(r"path.csv")
