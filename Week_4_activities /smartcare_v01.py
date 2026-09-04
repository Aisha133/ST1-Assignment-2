#Create a simple python file with basic inputs and outputs.
#the program must allow a receptionist to record each patients name, practitioner name and appointment time.

#what data must be stored -> Names and times
#what functions might be useful -> Inserting names, times. displaying booking times.
#what could go wrong -> Blank names, wrong times displayed, double bookings.
#unclear requirements -> How many patients can a practitioner have, how are appointments cancelled, ect.

#Code below was provided via the lab student handbook, any errors that appeared where fixed.
#Task 1:
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time:"
      f"{appointment1_time}") #Had to change the indentation and add f (float)
# Second Appointment
patient2_name = 'Bob Johnson'#the second patient recorded by the receptionist.
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time:"
      f"{appointment2_time}") #Had to change the indentation and add f (float)

#five limitations -> Is limited in it's functionality, as information is only displayed and cannot be inputted or searched. No cancellation process present. Has nothing in place for possible error. Limited booking's. No prior appointment history.


#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file
appointments = []
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

appointment = {
    "patient": patient1_name, #had to define
    "practitioner": practitioner1_name, #had to define
    "time": appointment1_time #had to define
}

appointments.append(appointment)
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

for appointment in appointments:
    print(f"Patient: {appointment['patient']} | Practitioner:"
          f"{appointment['practitioner']} | Time: {appointment['time']}")
    print("Welcome to SmartCare: The Clinical Appointment Booking System!")
    book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
    book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
    display_appointments()
#indentations had to be fixed

#limitations -> Data still cannot be entered, no code that will allow cancellation, limited bookings shown, no appointment history, limited visibility of practitioner availability