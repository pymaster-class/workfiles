'''
It's a simple python script that takes the hb, mcv, and reticulocyte count values 
and returns the possible causes of the observed anaemia. The goal is to demonstrate 
the use of python aiding anaemia differential diagnosis.

'''
import time

hb = float(input('Enter hb: '))
mcv = float(input('Enter mcv: '))
retics_count = float(input('Reticulocyte count(%): '))
sex = str(input('Enter your sex - male or female '))

'''
def retics_count_eval(retics_count):
    if 10000 <= retics_count <= 30000:
        pass
'''
print('Analysing...')
time.sleep(5.0)

#mcv = 80-100fl
if sex == 'male':
    if (hb < 14.0 and retics_count < 0.2 and mcv <80):
        print('The observed anaemia could be due to one of the following: \n Iron deficiency secondary to chronic blood lose \n Thalassemia')
    elif ((hb < 14.0 and retics_count < 0.2) and (80 <= mcv <= 100)):
        print('The observed anaemia could be due to one of the following: \n ACD \n Antiviral drugs \n Tumor/Infection in bone marrow')
    elif ((hb < 14.0 and retics_count < 0.2) and (mcv >= 100)):
        print('The observed anaemia could be due to one of the following: \n Medication \n Cancer Chemotherapy \n Myelodysplasia \n Vitamin Bââ deficiency \n Alcohol abuse \n Liver disease ')
    else:
        print('To be determined soon')
elif sex == 'female':
    if (hb < 12.0 and retics_count < 0.2 and mcv <80):
        print('The observed anaemia could be due to one of the following: \n Iron deficiency secondary to chronic blood lose \n Thalassemia')
    elif ((hb < 12.0 and retics_count < 0.2) and (80 <= mcv <= 100)):
        print('The observed anaemia could be due to one of the following: \n ACD \n Antiviral drugs \n Tumor/Infection in bone marrow')
    elif ((hb < 12.0 and retics_count < 0.2) and (mcv >= 100)):
        print('The observed anaemia could be due to one of the following: \n Medication \n Cancer Chemotherapy \n Myelodysplasia \n Vitamin Bââ deficiency \n Alcohol abuse \n Liver disease ')
    else:
        print('To be determined soon')
else:
    print('Out of options for now')
    
