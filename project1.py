# SI 201 Project 1
# Your name: Vanessa Adan
# Your student id: 23627585
# Your email: vadan@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv

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
    
    print (f"The state {highest_name_state} receives the most orders from the Category Technology and Segment Corporate with a max number of {highest_num_state}.")



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
    
    print(f"The ship mode {name_highest_mode} is the most requested in the category Furniture ordered by Consumers, with a high number {highest_mode_num}.")


#Test Functions

def





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
    num_ship_modes = number_ship_mode(consumer_furniture_data)
    most_requested(num_ship_modes)

if __name__ == "__main__":
    main()
