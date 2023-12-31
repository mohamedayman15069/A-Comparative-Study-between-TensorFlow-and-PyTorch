'''
This is an implementation for this API Parameter List Complexity Index (APXI) Metric that we are going to use to evaluate the usability of the API
We relied on the Some structural measures of API usability with some modification to fit in our research purpose

Measuring S2: the overall usability of an API with respect to the lengths of the parameter sequences and the
extent to which they occur in runs of data objects of the same type
'''
import numpy as np 
import pandas as pd
from ast import literal_eval

def g(x,y):
    if y >= x: 
        return np.exp(x-y)
    else:
        return 1.0


#Measure C_l
def MeasureGoodness(df):
    '''
    Given the dataframe, we calculate the goodness of the API: Getting the params
    '''
    #documentation_dataFrame should have the following columns: Name_Method, Parameters, Return_Type 
    #Get the parameters    
    parameters = df.apply(lambda x: literal_eval(x['param_names']), axis=1)
    C_L = 0.0
    
    N_d = 4 #Max Number of parameters in a method

    for i in range(len(parameters)):               
        C_L += g(N_d, len(parameters[i]))
    C_L = C_L/len(parameters)
    return C_L

def CalculateSpt(params_type_method):
    #Given the param Name and Type List we calculate the S_pt
    if params_type_method == None:
        return 0
    lens = len(params_type_method)
    Spt = 0
    for i in range(1,lens):
        if params_type_method[i] == params_type_method[i-1]:
            Spt += 1
        
    return Spt

def h(params_type_method):
    Spt = CalculateSpt(params_type_method)
    try:
        A_m = len((params_type_method))
    except:
        A_m = 0
    if A_m > 1: 
        return 1 - Spt/(A_m - 1)
    else:
        return 1

def ParameterSequenceComplexity(param_type_methods):
    
    C_s = 0 #Total C_s
    for param_type_method in param_type_methods:
        C_s += h(param_type_method)
    
    return C_s/len(param_type_methods)

def APXI(df):
    
    C_l = MeasureGoodness(df)
    #make df['param_types'] a list of lists
    param_types = df.apply(lambda x: literal_eval(x['param_types']), axis=1)
    C_s = ParameterSequenceComplexity(param_types)
    
    return (C_l + C_s)/2.0


# # Sample data
# data = {
#     'Name_Method': ['getUserInfo', 'setPassword', 'updateUserProfile', 'isUserAdmin', 'addUserRole', 'deleteUser'],
#     'Parameters_name': ['username, password', 'password', 'profileData', 'X', 'roleName', 'username'],
#     'Parameters_type': [['str', 'str'], ['str'], ['obj'], None, ['str'], ['str']]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Call the APXI function
# apxi_result = APXI(df)

# # Print the result
# print("APXI Result:", apxi_result)
