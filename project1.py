# SI 201 Project 1
# Your name and partners name: Vanessa Adan
# Your student id: 23627585
# Your email: vadan@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): Emma Blando
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv
import os
import unittest

def results_to_txt(filename,text):
    with open(filename,"w") as file:
        file.write(text)

def load_superstore_data(csv_file):

    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        headers = next(reader)

        for row in reader: 
            new_dict = {}
            for i in range(len(headers)):
                new_dict[headers[i]] = row[i]
            data.append(new_dict)

        return data

#--------------------------------------------------------------------------------------

#Code Calculation #1

def organize_to_corporate(data):

    corporate_data = []

    for row in data:
        if row["Segment"] == "Corporate":
            corporate_data.append(row)
    return corporate_data

def organize_to_technology(corporate_data):

    corporate_tech_data = []

    for row in corporate_data:
        if row["Category"] == "Technology":
            corporate_tech_data.append(row)

    return corporate_tech_data

def number_of_states(corporate_tech_data):

    num_states = {}

    for row in corporate_tech_data:
        state = row['State']
        
        if state != "":
            if state in num_states:
                num_states[state] += 1
            else: 
                num_states[state] = 1
    
    return num_states

def max_state(num_states):

    highest_num_state = 0
    highest_name_state = "" 

    for state, num in num_states.items():
        if highest_num_state < num:
            highest_num_state = num
            highest_name_state = state
        else: 
            continue
    
    return f"The state {highest_name_state} receives the most orders from the Category Technology and Segment Corporate with a max number of {highest_num_state}."


#--------------------------------------------------------------------------------------

#Code Calculation #2

def organize_to_consumer(data):
    consumer_data = []

    for row in data:
        if row["Segment"] == "Consumer":
            consumer_data.append(row)
    return consumer_data
    pass

def organize_to_furniture(consumer_data):
    consumer_furniture_data = []

    for row in consumer_data:
        if row["Category"] == "Furniture":
            consumer_furniture_data.append(row)

    return consumer_furniture_data
    pass
def number_ship_modes(consumer_furniture_data):

    num_ship_modes = {}

    for row in consumer_furniture_data:
        ship_mode = row["Ship Mode"]
        if ship_mode != "":
            if ship_mode in num_ship_modes:
                num_ship_modes[ship_mode] += 1
            else: 
                num_ship_modes[ship_mode] = 1
        
    return num_ship_modes
    pass
def most_requested(num_ship_modes):

    highest_mode_num = 0 
    name_highest_mode = ""

    for ship_mode, num in num_ship_modes.items():
        if highest_mode_num < num:
            highest_mode_num = num
            name_highest_mode = ship_mode
        else: 
            continue
    
    return f"The ship mode {name_highest_mode} is the most requested in the category Furniture ordered by Consumers, with a high number {highest_mode_num}."


#Test Functions
#--------------------------------------------------------------------------------------


class TestFunctions(unittest.TestCase):

    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__), "test.csv")
        self.test_case_data = load_superstore_data(file_path) 

    def test_num_states_gen1(self):
        corporate_data = organize_to_corporate(self.test_case_data)
        corporate_tech_data = organize_to_technology(corporate_data)
        num_states = number_of_states(corporate_tech_data)

        self.assertEqual(num_states,{
            "California": 2,
            "Pennsylvania": 3,
            "Ohio": 1,
            "New York": 1,
            "Wisconsin": 1})
        self.assertIsInstance(num_states, dict)
    
    def test_num_states_gen2(self):
        
        data = [
            {"State": "Illinois"},
            {"State": "Illinois"},
            {"State": "California"},
            {"State": "Illinois"}
        ]
        self.assertEqual(number_of_states(data), {"Illinois": 3, "California": 1})

        pass
        

    def test_num_states_edge1(self):
        self.assertEqual(number_of_states([]), {})

    def test_num_states_edge2(self):
        edge_data_states = [
            {"State": "California"},
            {"State": "California"},
            {"State": ""}
        ]
        self.assertEqual(number_of_states(edge_data_states), {"California": 2})


    def test_num_ship_modes_gen1(self):
        consumer_data = organize_to_consumer(self.test_case_data)
        corporate_furniture_data = organize_to_furniture(consumer_data)
        num_ship_modes = number_ship_modes(corporate_furniture_data)

        self.assertEqual(num_ship_modes, {
            "Same Day": 1,
            "First Class": 1,
            "Standard Class": 5})
        self.assertIsInstance(num_ship_modes, dict)

    def test_num_ship_modes_gen2(self):

        gen2_data = [
            {"Ship Mode": "Same Day"},
            {"Ship Mode": "First Class"},
            {"Ship Mode": "Second Class"},
            {"Ship Mode": "Standard Class"}
        ]
        self.assertEqual(number_ship_modes(gen2_data), {"Same Day": 1, "First Class": 1, "Second Class": 1, "Standard Class": 1})
        pass

    def test_num_ship_modes_edge1(self):
        #the actual dataset doesn't have any missing values but this is to make sure the functions can still work
        self.assertEqual(number_ship_modes([]),{})

    def test_num_ship_modes_edge2(self):
        edge_data_ship_modes = [
            {"Ship Mode": "Standard Class"},
            {"Ship Mode": "First Class"},
            {"Ship Mode": ""}

        ]
        self.assertEqual(number_ship_modes(edge_data_ship_modes), {"Standard Class": 1, "First Class": 1})

#--------------------------------------------------------------------------------------
#Main Function 

def main():
    data = load_superstore_data("SampleSuperstore.csv")

    #Calculation 1

    corporate_data = organize_to_corporate(data)
    corporate_tech_data = organize_to_technology(corporate_data)
    num_states = number_of_states(corporate_tech_data)
    max_state(num_states)

    #Calculation 2

    consumer_data = organize_to_consumer(data)
    consumer_furniture_data = organize_to_furniture(consumer_data)
    num_ship_modes = number_ship_modes(consumer_furniture_data)
    most_requested(num_ship_modes)

if __name__ == "__main__":
    unittest.main()
    main()
#--------------------------------------------------------------------------------------
