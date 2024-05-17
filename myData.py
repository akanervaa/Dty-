import json
Time = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
Powers = [
    'Power 1',
    'Power 2',
    'Power 3',
    'Power 4',
    'Power 5'
    ]
realPowers = [
    'rPower 1',
    'rPower 2',
    'rPower 3',
    'rPower 4',
    'rPower 5'
    ]
wastePowers = [
    'wPower 1',
    'wPower 2',
    'wPower 3',
    'wPower 4',
    'wPower 5'
    ]
Storages = [
    'Storage 1',
    'Storage 2',
    'Storage 3',
    'Storage 4',
    'Storage 5'
    ]

Sewage_Storage = [
    'Sewage 1',
    'Sewage 2',
    'Sewage 3',
    'Sewage 4',
    'Sewage 5'
    ]
Diluted_Oxygen = [
    'Oxygen 1',
    'Oxygen 2',
    'Oxygen 3',
    'Oxygen 4',
    'Oxygen 5'
    ]

#day_ahead_price = [40] * 36


day_ahead_price = {
    0: 82.72,
    1: 81.63,
    2: 80.17,
    3: 78.31,
    4: 77.51,
    5: 90.00,
    6: 103.77,
    7: 117.00,
    8: 120.68,
    9: 104.72,
    10: 106.19,
    11: 105.79,
    12: 102.36,
    13: 102.71,
    14: 105.30,
    15: 111.85,
    16: 122.05,
    17: 133.00,
    18: 135.58,
    19: 128.97,
    20: 122.00,
    21: 107.19,
    22: 103.07,
    23: 98.01,
    24: 82.72,
    25: 81.63,
    26: 80.17,
    27: 78.31,
    28: 77.51,
    29: 90.00,
    30: 103.77,
    31: 117.00,
    32: 120.68,
    33: 104.72,
    34: 106.19,
    35: 105.79,
}

intraday_price = {
    0: 82.72,
    1: 81.60,
    2: 78.65,
    3: 75.81,
    4: 77.14,
    5: 91.00,
    6: 104.68,
    7: 119.33,
    8: 111.00,
    9: 101.00,
    10: 102.19,
    11: 104.20,
    12: 95.19,
    13: 102.20,
    14: 104.20,
    15: 113.00,
    16: 113.00,
    17: 130.00,
    18: 125.20,
    19: 111.00,
    20: 98.20,
    21: 91.50,
    22: 90.00,
    23: 88.00,
    24: 82.72,
    25: 81.60,
    26: 78.65,
    27: 75.81,
    28: 77.14,
    29: 91.00,
    30: 104.68,
    31: 119.33,
    32: 111.00,
    33: 101.00,
    34: 102.19,
    35: 104.20,
}
#demand = {i: original_demand[i % 24] for i in range(168)}
daily_septic=9865
septic_sewage = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: daily_septic/13,
    7: daily_septic/13,
    8: daily_septic/13,
    9: daily_septic/13,
    10: daily_septic/13,
    11: daily_septic/13,
    12: daily_septic/13,
    13: daily_septic/13,
    14: daily_septic/13,
    15: daily_septic/13,
    16: daily_septic/13,
    17: daily_septic/13,
    18: daily_septic/13,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0,
    27: 0,
    28: 0,
    29: 0,
    30: daily_septic/13,
    31: daily_septic/13,
    32: daily_septic/13,
    33: daily_septic/13,
    34: daily_septic/13,
    35: daily_septic/13,
}
daily_municipal = 13844
municipal_ww = {
    0: 0.03*daily_municipal,
    1: 0.03*daily_municipal,
    2: 0.03*daily_municipal,
    3: 0.03*daily_municipal,
    4: 0.03*daily_municipal,
    5: 0.03*daily_municipal,
    6: 0.03*daily_municipal,
    7: 0.048*daily_municipal,
    8: 0.048*daily_municipal,
    9: 0.048*daily_municipal,
    10: 0.048*daily_municipal,
    11: 0.048*daily_municipal,
    12: 0.048*daily_municipal,
    13: 0.048*daily_municipal,
    14: 0.048*daily_municipal,
    15: 0.048*daily_municipal,
    16: 0.048*daily_municipal,
    17: 0.048*daily_municipal,
    18: 0.048*daily_municipal,
    19: 0.048*daily_municipal,
    20: 0.048*daily_municipal,
    21: 0.048*daily_municipal,
    22: 0.048*daily_municipal,
    23: 0.03*daily_municipal,
    24: 0.03*daily_municipal,
    25: 0.03*daily_municipal,
    26: 0.03*daily_municipal,
    27: 0.03*daily_municipal,
    28: 0.03*daily_municipal,
    29: 0.03*daily_municipal,
    30: 0.03*daily_municipal,
    31: 0.048*daily_municipal,
    32: 0.048*daily_municipal,
    33: 0.048*daily_municipal,
    34: 0.048*daily_municipal,
    35: 0.048*daily_municipal,
}
septic_BOD = 533.928
municipal_BOD = 109.64286
flex_power_allocation = {i: 0 for i in range(len(Time))}
flex_energy_allocation = {i: 0 for i in range(len(Time))}
# initial values for parameters

duration = 3
reset=True
with open('Locked_power_flex.json', 'r') as f:
    locked_power_flex = json.load(f)
with open('Locked_energy_flex.json', 'r') as f:
    locked_energy_flex = json.load(f)
with open('CurrentConsumption.json', 'r') as f:
    normal_behavior = json.load(f)     
for d in range(duration):
    flex_power_allocation[0+d] += 0
    #Would possible to implement if condition here to make sure that if flexibility is allocated, it cannot be different direction than allocated at that specific time step
    flex_power_allocation[6+d] += 0
flex_energy_allocation[18] += 1500
for i, flex in enumerate(flex_power_allocation.items()):
    key, val = flex
    try:
        if val > 0 and locked_power_flex[i]["up/down"] != "down":
            locked_power_flex[i] = {"Duration":duration,"Amount":  val+normal_behavior[i]['Consumption'], "Time step": i, "up/down":"up"}
        elif val < 0 and locked_power_flex[i]["up/down"] != "up":
            locked_power_flex[i] = {"Duration":duration,"Amount":  val+normal_behavior[i]['Consumption'], "Time step": i, "up/down":"down"}
        if reset:
            locked_power_flex[i] = {"Duration":duration,"Amount":  0, "Time step": i, "up/down":"N/A"}
    except IndexError:
        locked_power_flex.append({"Duration":duration,"Amount":  0, "Time step": i, "up/down":"N/A"})
for i, flex in enumerate(flex_energy_allocation.items()):
    key, val = flex
    try:
        if val > 0 and locked_energy_flex[i]["up/down"] != "down":
            locked_energy_flex[i] = {"Duration":duration,"Amount":  val+sum(normal_behavior[i+d]['Consumption'] for d in range(duration)), "Time step": i, "up/down":"up"}
        elif val < 0 and locked_energy_flex[i]["up/down"] != "up":
            locked_energy_flex[i] = {"Duration":duration,"Amount":  val+sum(normal_behavior[i+d]['Consumption'] for d in range(duration)), "Time step": i, "up/down":"down"}
        if reset:
            locked_energy_flex[i] = {"Duration":duration,"Amount":  0, "Time step": i, "up/down":"N/A"}
    except IndexError:
        locked_energy_flex.append({"Duration":duration,"Amount":  0, "Time step": i, "up/down":"N/A"})

with open('Locked_power_flex.json', 'w') as f:
    json.dump(locked_power_flex, f, indent=1)
with open('Locked_energy_flex.json', 'w') as f:
    json.dump(locked_energy_flex, f, indent=1)
        
            
V_max = 50
V_max_ox = 2
V_min_ox = 0
P_max = 168
P_min = 0
efficiency = 1.01
#ratio between diluted oxygen in oxygen storage and sewage storage, i.e. tells how much sewage the oxygen removes
alfa = 1
#The ratio between used power of aerators and generated oxygen. 168 kW of aeration generates 69,25 mg/lt of oxygen per h
max_production = 69.25
powerfactor = P_max/max_production
#roc of oxygen
#O_transfer_max = 69
#O_transfer_min = 13
O_transfer_max = 69.25
O_transfer_min = 0
Tank_volume = 4228