import json
import pickle
import numpy as np
import pandas as pd
import config

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):

        self.age= age
        self.sex= sex
        self.bmi= bmi
        self.children= children
        self.smoker= smoker
        self.region = "region_"+region

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)



        # with open (r"C:\Users\ADMIN\Desktop\aws\Models\medical_ins_project_data.json","r") as f:
        #     self.json_data=json.load(f)

        # with open (r"C:\Users\ADMIN\Desktop\aws\Models\Linear_model_medical_ins.pkl","rb") as f:
        #     self.model=pickle.load(f)

    def get_predicted_price(self):
        self.load_model()

        array=np.zeros(len(self.json_data["columns"]))
        
        array[0] = self.age
        array[1] = self.json_data["sex"][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data["smoker"][self.smoker]
    
        region_index=self.json_data["columns"].index(self.region)

        array[region_index]=1

        print("Array ::",array )


        result=self.model.predict([array])[0]
        return round(result,2)


if __name__ == "__main__":
    age = 40
    sex = "male"
    bmi = 20.2
    children = 3
    smoker = "yes"
    region = "southwest"

    Obj = MedicalInsurance(age,sex,bmi,children,smoker,region)
    result1= Obj.get_predicted_price()
    print(f"The Insurance of claim is Rs. {result1}/- Only ")
