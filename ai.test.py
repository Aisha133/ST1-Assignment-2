# SmartCare Appointment Booking System

# List to store appointments
appointments = []

# Function to book an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):
    # Validate inputs
    if not patient_name:
        print("Patient name cannot be empty.")
        return

    if not practitioner_name:
        print("Practitioner name cannot be empty.")
        return

    if not appointment_time:
        print("Appointment time cannot be empty.")
        return

    # Create appointment dictionary
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Add appointment to list
    appointments.append(appointment)
    print(f"Appointment booked for {patient_name}.")

# Function to display appointments
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    print("\n--- Appointment List ---")

    for index, appointment in enumerate(appointments, start=1):
        print(f"\nAppointment {index}")
        print(f"Patient: {appointment['patient']}")
        print(f"Practitioner: {appointment['practitioner']}")
        print(f"Time: {appointment['time']}")

# Example appointments
print("Welcome to SmartCare!")

book_appointment("none", "Dr. John Roe", "20 July 2024, 11:30 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "20 July 2024, 11:30 AM")

# Display all appointments
display_appointments()