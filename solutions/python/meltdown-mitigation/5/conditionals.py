"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):

    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000
    


def reactor_efficiency(voltage, current, theoretical_max_power):

    generated_power = voltage * current
    percentage = int((generated_power/theoretical_max_power) * 100)

    if percentage >= 80:
        return 'green'
    elif 60 <= percentage < 80:
        return 'orange'
    elif 30 <= percentage < 60:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):

    if (temperature * neutrons_produced_per_second) < ((90 * threshold) / 100):
        return 'LOW'
    elif (threshold - ((10 * threshold) / 100)) <= (temperature * neutrons_produced_per_second) <= threshold :
        return 'NORMAL'
    elif threshold <= (temperature * neutrons_produced_per_second) <= (((10 * threshold) / 100) + threshold):
        return 'NORMAL'
    else:
        return 'DANGER'

    
