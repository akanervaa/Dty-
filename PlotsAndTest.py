from pyomo.environ import *
import matplotlib.pyplot as plt
import myData
import json
from flex_index_plot import flex_index
from ProcessModel import optimize_power_system
from ProcessLimitCalculation import power_calc
import numpy as np
#Calculations for flexibility criteria:
def FlexibilityCriteriaCalculation(max_energy_flex, min_energy_flex, duration):
    total_upward_flex = sum(max_energy_flex)/duration
    average_upward_flex = total_upward_flex/len(max_energy_flex)
    total_downward_flex = sum(min_energy_flex)/duration
    average_downward_flex = total_downward_flex/len(max_energy_flex)
    robustness_flex = []
    gain_in_euros = 0
    for t in myData.Time:
        if myData.flex_energy_allocation[t] != 0:
            gain_in_euros += sum((CurrentConsumption[t+d]-PreviousConsumption[t+d])*(myData.day_ahead_price[t+d]-myData.intraday_price[t+d]) for d in range (myData.duration))
        robustness_flex.append(min(max_energy_flex[t],abs(min_energy_flex[t])))
    robustness_flex.sort()
    robustness_mean = ((robustness_flex[int(len(myData.Time)/2)]+robustness_flex[int(len(myData.Time)/2-1)])/2)/duration
    print(total_upward_flex, average_upward_flex, total_downward_flex, average_downward_flex,robustness_mean,gain_in_euros/1000)
#plots consumption of energy, and also temporarily total waste flow (ignore wording of waste flow plot, its made for energy consumption)
def ConsumptionComparisonPlot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length.")
    x_values = np.arange(len(vector1))
    plt.plot(x_values, vector1, label='Previous consumption pattern')
    plt.plot(x_values, vector2, label='Current consumption pattern')
    plt.xlabel('number of timestep')
    plt.ylabel('Energy consumption (kWh)')
    plt.legend()
    plt.title('Total aeration usage in kWh per time step')
    plt.show()
    
with open('CurrentConsumption.json', 'r') as f:
    new_normal_behavior = json.load(f)

# with open('locked_flex_behavior.json', 'r') as f:
    # new_normal_behavior1 = json.load(f)
P1n_values, P2n_values, P3n_values, P4n_values, P5n_values, V1n_values, V2n_values, V3n_values, V4n_values, V5n_values, dV1n_values, dV2n_values, dV3n_values, dV4n_values, dV5n_values, SV1n_values, SV2n_values, SV3n_values, SV4n_values, SV5n_values,DO1n_values,results_n, model_n= optimize_power_system(myData, myData.day_ahead_price)
CurrentConsumption = []
PreviousConsumption = []
# Calculates the consumption in new normal conditions i.e. with flexibility allocation
for i in myData.Time:
    # print((P1n_values[i]+P2n_values[i]+P3n_values[i]+P4n_values[i]+P5n_values[i])*myData.powerfactor)
    PreviousConsumption.append(new_normal_behavior[i]['Consumption'])
    new_normal_behavior[i]= {'Timestep': i, 'Consumption': (P1n_values[i]+P2n_values[i]+P3n_values[i]+P4n_values[i]+P5n_values[i])*myData.powerfactor}
    CurrentConsumption.append(new_normal_behavior[i]['Consumption'])
# writes this behavior in flex_behavior.json
with open('CurrentConsumption.json', 'w') as f:
    json.dump(new_normal_behavior, f, indent=1)

consumption_sum = 0
for t in range(36):
    consumption_sum = sum(CurrentConsumption)

print("36h consumption is", consumption_sum, "kWh")

temp_storage = []
to_EMS = {}

max_energy_flex = power_calc(CurrentConsumption,cost_value=-150, duration=1)
min_energy_flex = power_calc(CurrentConsumption,cost_value=150, duration=1)
flex_index(max_energy_flex, min_energy_flex, "1-timestep energy flexibility scenarios")
FlexibilityCriteriaCalculation(max_energy_flex, min_energy_flex,1)
for i in range(len(max_energy_flex)):
    temp_storage.append((max_energy_flex[i], min_energy_flex[i]))
to_EMS['up/down 1 time-step energy flexibility service scenarios']=temp_storage

temp_storage = []
max_energy_flex = power_calc(CurrentConsumption,cost_value=-150, duration=2)
min_energy_flex = power_calc(CurrentConsumption,cost_value=150, duration=2)
#flex_index(max_total_flex, miCurrentConsumption_flex, "2power")
flex_index(max_energy_flex, min_energy_flex, "2-timestep energy flexibility scenarios")
FlexibilityCriteriaCalculation(max_energy_flex, min_energy_flex,2)
for i in range(len(max_energy_flex)):
    temp_storage.append((max_energy_flex[i], min_energy_flex[i]))
to_EMS['up/down 2 time-step energy flexibility service scenarios']=temp_storage

temp_storage = []
max_energy_flex = power_calc(CurrentConsumption,cost_value=-150, duration=3)
min_energy_flex = power_calc(CurrentConsumption,cost_value=150, duration=3)
FlexibilityCriteriaCalculation(max_energy_flex, min_energy_flex,3)
#flex_index(max_total_flex, miCurrentConsumption_flex, "3power")
flex_index(max_energy_flex, min_energy_flex, "3-timestep energy flexibility scenarios")
for i in range(len(max_energy_flex)):
    temp_storage.append((max_energy_flex[i], min_energy_flex[i]))
to_EMS['up/down 3 time-step energy flexibility service scenarios']=temp_storage
temp_storage = []

max_energy_flex = power_calc(CurrentConsumption, cost_value=-150, duration=4)
min_energy_flex = power_calc(CurrentConsumption, cost_value=150, duration=4)
#flex_index(max_total_flex, miCurrentConsumption_flex, "4power")
flex_index(max_energy_flex, min_energy_flex, "4-timestep energy flexibility scenarios")
FlexibilityCriteriaCalculation(max_energy_flex, min_energy_flex,4)
for i in range(len(max_energy_flex)):
    temp_storage.append((max_energy_flex[i], min_energy_flex[i]))
to_EMS['up/down 4 time-step energy flexibility service scenarios']=temp_storage
temp_storage = []
PreviousConsumption= [value for value in PreviousConsumption]
CurrentConsumption = [value for value in CurrentConsumption]

ConsumptionComparisonPlot(PreviousConsumption, CurrentConsumption)


