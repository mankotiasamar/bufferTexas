import random


class SimpleLogicBuffer:
    """Represents a simple logic buffer device with one input and one output.

    Depending on the input value the device switches the output on or off:
      - If `input_voltage > on_threshold` then `Output = True`
      - Else `Output = False`

    There is no hysteresis.

    A noisy input signal, can be simulated as well.
    Then the output value depends on the input value and a gaussian distributed random number.
    """

    def __init__(self, on_threshold=1.8, random_seed=1):
        """
        create an instance of the Device-under-test with the specified threshold and initialize the random number
        generator with a known value to have reproducible test outcomes.

        :param on_threshold: (optional) Threshold above which an input signal will produce an Output Signal `True`
        :param random_seed: (optional) initializes the random generator so that a reproducible (pseudo-) random
                            sequence will be produced. Only needed if a noisy input signal is simulated.
        """
        random.seed(a=random_seed)
        self.on_threshold = on_threshold
        self.output_state = False

    def apply_input_voltage(self, value, noise_sigma=0.0):
        """
        Apply input voltage to device and update output state.

        :param value: Input voltage level.
        :param noise_sigma: (optional) Simulate a noisy input signal by adding a random number with `mu=0.0` and
                            `sigma=noise_sigma` to the specified `value`.
        :return: `None`
        """
        self.output_state = (value + random.gauss(mu=0.0, sigma=noise_sigma)) > self.on_threshold
        

    def is_on(self):
        """
        Read output state of Buffer.

        :return: `True` if the previously applied input voltage is greater than `self.on_threshold`, otherwise `False`.
        """
        return self.output_state
		

"""
Creating the object of class SimpleLogicBuffer
"""
obj= SimpleLogicBuffer() 

"""
If input voltage is less than 1.8 volts, the buffer output will be in false state
i.e. Test Pass
"""
print("Test for input voltage = 1.2 Volts is")
obj.apply_input_voltage(1.2)
if obj.is_on() == False:			
 print("Test Pass");
else : 
 print("Test Fail") ;   

"""
If input voltage is greater than 1.8, the buffer output will be in True state
i.e. Test Pass
"""
print("Test for input voltage = 2.5 Volts is")
obj.apply_input_voltage(2.5)
if obj.is_on() == True:			
 print("Test Pass");
else : 
 print("Test Fail") ; 

"""
User can enter the maximum value of buffer voltage manually
Incrementing the value by 9
Calling the function apply_input_voltage and passing the value of input voltage
While passing the input voltage value as param, divide i by 1000 such that float values are passed as input voltage values 
Checking the threshold voltage
Printing the threshold voltage
Breaking the for loop inside if condition
""" 
MaxVolt = int(input("Enter the Maximum Voltage of the Buffer in Volts"))
for i in range(0, MaxVolt*1000, 9):
  obj.apply_input_voltage(i/1000)
  if obj.is_on() == True:
    print("Threshold Voltage is =", i/1000, "Volts")
    break



