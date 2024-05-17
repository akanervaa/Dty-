import myData
from ProcessModel import optimize_power_system
import pandas as pd
from plot_function import plot
def power_calc(CurrentConsumption,cost_value=0, duration=1):
    energy_flex_list = []
    power_costs_list = []
    image_paths= []
    # Creates the scenarios for the storage behavior for all time steps at some price point at one time step at a time, or duration time steps at a time.
    for i in range(len(myData.Time)):
        scenario = {j: (cost_value+myData.day_ahead_price[i] if j in range(i, i+duration) else myData.day_ahead_price[i]) for j in range(len(myData.Time))}
        power_costs_list.append(scenario)
    # while len(power_costs_list) < len(myData.Time):
        # power_costs_list.append({i: 50 for i in range(len(myData.Time))})

    for i, PowerCosts in enumerate(power_costs_list):
        # Extracts the values from pyomo model.
        # print(len(power_costs_list))
        # print(PowerCosts)
        P1_values, P2_values, P3_values, P4_values, P5_values, V1_values, V2_values, V3_values, V4_values, V5_values, dV1_values, dV2_values, dV3_values, dV4_values, dV5_values, SV1_values, SV2_values, SV3_values, SV4_values, SV5_values, DO1_values,results, model= optimize_power_system(myData, PowerCosts)
        #P1p_values, P2p_values, P3p_values, P4p_values, P5p_values, V1_values, V2_values, V3_values, V4_values, V5_values, dV1_values, dV2_values, dV3_values, dV4_values, dV5_values, results, model= optimize_power_system(myData, PowerCosts, i, duration, n_total)
        # Print results or perform further analysis as needed
        # adds min or max values at studied time step to a list for the storage flexibility potential plot

        if i <= len(power_costs_list):
            if cost_value == -150:
                try:
                    if (all((myData.locked_power_flex[i+du]['up/down'] != 'down') and myData.locked_energy_flex[i+du]['up/down'] != "down" for du in range(duration))):
                        #max_flex = min((P1p_values[i+d]+P2p_values[i+d]+P3p_values[i+d]+P4p_values[i+d]+P5p_values[i+d])*myData.powerfactor - n_total[i+d] for d in range(duration))
                        # max_flex = (P1p_values[i]+P2p_values[i]+P3p_values[i]+P4p_values[i]+P5p_values[i])*myData.powerfactor - n_total[i]
                        energy_flex = sum((P1_values[i+d]+P2_values[i+d]+P3_values[i+d]+P4_values[i+d]+P5_values[i+d])*myData.powerfactor - CurrentConsumption[i+d] for d in range(duration))
                    else:
                        energy_flex = 0
                        #max_flex = 0

                    # print(energy_flex)
                    energy_flex_list.append(energy_flex)
                    #max_total_flex.append(max_flex)
                except:
                    energy_flex_list.append(0)
                    #max_total_flex.append(0)


            elif cost_value == 150:
                try:
                    # Calculates minimum flexibility and energy
                    # if 0 > max(P1_values[i+d]+P2_values[i+d]+P3_values[i+d]+P4_values[i+d]+P5_values[i+d] - n_total[i+d] for d in range(duration)):
                    if (all(myData.locked_power_flex[i+du]['up/down'] != 'up' and myData.locked_energy_flex[i+du]['up/down'] != "up" for du in range(duration))):
                        # min_flex = (P1p_values[i]+P2p_values[i]+P3p_values[i]+P4p_values[i]+P5p_values[i])*myData.powerfactor - n_total[i]
                        energy_flex = sum((P1_values[i+d]+P2_values[i+d]+P3_values[i+d]+P4_values[i+d]+P5_values[i+d])*myData.powerfactor - CurrentConsumption[i+d] for d in range(duration))
                        #min_flex = max((P1p_values[i+d]+P2p_values[i+d]+P3p_values[i+d]+P4p_values[i+d]+P5p_values[i+d])*myData.powerfactor - n_total[i+d] for d in range(duration))
                    else:
                        min_flex = 0
                        energy_flex = 0
                    # else:
                        # min_flex = min(P1_values[i+d]+P2_values[i+d]+P3_values[i+d]+P4_values[i+d]+P5_values[i+d] - n_total[i+d] for d in range(duration))
                    # print(min_flex)

                    # print(energy_flex)
                    energy_flex_list.append(energy_flex)
                    #min_total_flex.append(min_flex)
                except:
                    energy_flex_list.append(0)
                    #min_total_flex.append(0)
        #plot(0, myData.P_max, myData.V_max,image_paths,i, model, PowerCosts, list(myData.Time), 0, V1_values, P1_values,dV1_values, 'red', 'green', 'purple', '1', cost_value_scen=cost_value)
        #data = {'TimeStep': myData.Time[0:], 'P3': P1_values[0:], 'V3': V1_values[0:], 'dV3': dV1_values[0:], 'SV3 ': SV1_values[0:],'DO1': DO1_values[0:]}
        #table = pd.DataFrame(data)
        #Print the table
        #print(table)
    return energy_flex_list
        