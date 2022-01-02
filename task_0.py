#Written by: Liam Dwinnell
#Last Updated 7:20 PM November 21st 2021

#imports
import csv
import statistics



###Start Of Function Definitions###

#accepts the directory of a csv file
#returns a python list object of the csv file
def open_csv(dir):
    with open(dir, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

#accepts a single value 
#returns if it is an int float or string accordingly
def convert(val):
    constructors = [int, float, str]
    for c in constructors:
        try:
            return c(val)
        except ValueError:
            pass

#accepts a list of lists of strings 
#returns a list of lists of appropriate values (i.e floats, int, str, chr)
def render_values(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = convert(data[i][j])
    return data

#accepts a list of lists and col number
#returns a col due to [row][col] format not working with iterablity
def get_col(data, col):
    col_data = []
    for i in range(len(data)):
        col_data.append(data[i][col])
    return col_data

#accepts a python list of data 
#returns a python list of variable names
def get_variable_names(data):
    variable_names = data[0]
    return variable_names

#accepts a python list of data
#returns a python list of variable data types
def get_variable_types(data):
    variable_types = []
    #loop each variable
    for variable in range(len(data[0])):
        temp_types = []
        
        #loop each row
        for row in range(len(data)):
            #if not title row
            if row != 0:
                #get the data type and append it to the variable's type list if it is not already there
                elementType = type(data[row][variable]).__name__
                if elementType not in temp_types and data[row][variable] != "":
                    temp_types.append(elementType)
        #script to test for character variables
        if temp_types[0] == 'str':
            max_length = max(get_col(data, variable)[1:], key = len)
            if len(max_length) == 1: 
                temp_types[0] = 'chr'

        variable_types.append(temp_types[0])

    return variable_types

#accepts a 2d python list, the col number
#returns the number of missing values in the col
def get_missing_col(data, col):
    
    count = 0
    col_data = get_col(data, col)

    for row in col_data:
        if row == '':
            count += 1
    
    return count 

#accepts a python list of lists
#returns the total missing values for each variable
def get_missing(data):
    missing_count = []
    for col in range(len(data[0])):
        missing_count.append(get_missing_col(data, col))
    return missing_count

#accepts a list of lists and a list of data types
#returns the number of unique values in each list with data type str
def get_unique_strings(data, types):
    unique_counts = []

    #loop the variables
    for variable in range(len(types)):
        #if the variable is a string/character variable then get the number of unique values
        if types[variable] == "str" or types[variable] == "chr":
            temp = get_col(data, variable)[1:]
            unique_vals = set(temp)
            unique_counts.append(len(unique_vals))
        #if it is not a string.character leave it empty
        else:
            unique_counts.append("")
    return unique_counts

#accepts a list of lists, a col number, and a number of modes to retrieve
#returns a list of the top n modes for the given col of data
def get_mode(data, col, modes):
    top_modes = []
    temp = get_col(data,col)[1:]
    for i in range(modes):
        #get the mode of the col
        mode_string = max(set(temp), key=temp.count)
        #see how many instances there are
        mode_count = temp.count(mode_string)
        #add this to the returned list
        top_modes.append([mode_string, mode_count])
        #remove the mode element to find the next most frequent
        temp = list(filter((mode_string).__ne__, temp))
    return top_modes

#accepts a list of lists, the number of unique values, and the max modes to calculate for each col
#returns max_modes number of modes for each variable
def get_modes(data, uniques, max_modes):
    mode_list = []
    #loop each variable
    for variable in range(len(uniques)):
        #if the number of unique values is not empty
        if uniques[variable] != "":
            #if there are fewer unique values than asked for modes
            if uniques[variable] < max_modes:
                #set the modes to get to the number of unique values
                modes = uniques[variable]
            else:
                #set the modes to get to the max modes asked for
                modes = max_modes
            #get the modes
            temp_modes = get_mode(data, variable, modes)
            
            #append the empties if there is any remainder between max_nodes and modes
            for i in range(max_modes-modes):
                temp_modes.append("")
            mode_list.append(temp_modes)
        #if there is no modes make a list of empties for max_nodes length (for int and floats)
        else:
            temp = []
            for i in range(max_modes):
                temp.append("")
            mode_list.append(temp)
    return mode_list

#accepts a list of lists and a list of data types
#returns a list of the number of values under zero for int and float variables
def get_under_zero(data, types):
    under_zero_count = []

    for variable in range(len(types)):
        if types[variable] == 'int' or types[variable] == 'float':
            temp = get_col(data, variable)[1:]
            count = 0
            for i in range(len(temp)):
                try:
                    if float(temp[i]) < 0:
                        count += 1
                except:
                    pass
            under_zero_count.append(count)
        else:
            under_zero_count.append("")

    return under_zero_count

#accepts a list of lists and a list of data types
#returns a list of the number of values equal to zero for int and float variables
def get_equal_zero(data, types):
    equal_zero_count = []

    for variable in range(len(types)):
        if types[variable] == 'int' or types[variable] == 'float':
            temp = get_col(data, variable)[1:]
            count = 0
            for i in range(len(temp)):
                try:
                    if float(temp[i]) == 0:
                        count += 1
                except:
                    pass
            equal_zero_count.append(count)
        else:
            equal_zero_count.append("")

    return equal_zero_count

#accepts a list
#returns the mean of the list with empties removed
def get_mean(data):
    data = list(filter(("").__ne__, data))
    return sum(data)/len(data)

#accepts a list
#returns the median of the list with empties removed
def get_median(data):
    data = list(filter(("").__ne__, data))
    return statistics.median(data)

#accepts a list of lists and data types
#returns mean, median, min, and max of each numeric variable
def get_stats(data, types):

    means = []
    medians = []
    mins = []
    maxs = []
    
    for variable in range(len(types)):
        if types[variable] == 'int' or types[variable] == 'float':
            temp = get_col(data, variable)[1:]
            means.append(get_mean(temp))
            medians.append(get_median(temp))
            temp = list(filter(("").__ne__, temp))
            mins.append(min(temp))
            maxs.append(max(temp))
        else:
            means.append("")
            medians.append("")
            mins.append("")
            maxs.append("")
    return means, medians, mins, maxs


###End Of Function Definitions###



###Start Of Main Code###

#define the directory of the csv file
#dir = './example_csv.csv'
dir = input("Enter The CSV's Directory: ")

#open the given directory and load into python list
data = open_csv(dir)
data = render_values(data)

#get the first row of each collumn and store in python list
variable_names = get_variable_names(data)
print(variable_names)

#get the data types contained in each variable
variable_types = get_variable_types(data)
print(variable_types)

#count the number of empties for each variable
missing_counts = get_missing(data)
print(missing_counts)

#get the unique valeus for each variable
unique_strings = get_unique_strings(data, variable_types)
print(unique_strings)

#returns the top n modes and leaves nonstring blank [[[var1_val1, occurences],[var1_val2, occurences]],[[var2_val1, ocur][var2_val2, ocur]]]
string_modes = get_modes(data, unique_strings, 5)
print(string_modes)

#get a count of values under zero for float/int variables
under_zero_count = get_under_zero(data, variable_types)
print(f"Less Than Zero: ", under_zero_count)

#get a count of values equal to zero for float/int variables
equal_zero_count = get_equal_zero(data, variable_types)
print(f"Equals Zero: ", equal_zero_count)

#calculate the basic statistics 
means, medians, mins, maxs = get_stats(data, variable_types)
print(f"Means: ", means)
print(f"Medians: ", medians)
print(f"Mins: ", mins)
print(f"Maxs: ", maxs)

#code to export a csv (exported into the working directory)
out_dir = input("Enter The Export Directory: ")
out_name = input("Enter The Report's Name: ")
with open(out_dir + '/' + out_name + '.csv', mode='w', newline='') as report:
    report_writer = csv.writer(report, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    title_list = ["Variable Names", "Data Type", "Missing Count", "Unique Values"]
    for i in range(len(string_modes[0])):
        title_list.append("Mode Val " + str(i+1))
        title_list.append("Mode Count " + str(i+1))
    
    title_list.append("Under Zero")
    title_list.append("Equals Zero")
    title_list.append("Mean")
    title_list.append("Median")
    title_list.append("Min")
    title_list.append("Max")

    report_writer.writerow(title_list)
    
    for i in range(len(variable_names)):
        temp_list = []
        temp_list.append(variable_names[i])
        temp_list.append(variable_types[i])
        temp_list.append(missing_counts[i])
        temp_list.append(unique_strings[i])
        
        for j in range(len(string_modes[i])):
            try:
                temp_list.append(string_modes[i][j][0])
                temp_list.append(string_modes[i][j][1])
            except:
                temp_list.append("")
                temp_list.append("")

        temp_list.append(under_zero_count[i])
        temp_list.append(equal_zero_count[i])
        temp_list.append(means[i])
        temp_list.append(medians[i])
        temp_list.append(mins[i])
        temp_list.append(maxs[i])

        report_writer.writerow(temp_list)

###End Of Main Code###