class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def create_record(self):
        pass

    def search_by_name(self):
        pass

    def update_details(self):
        pass

    def retrieve_information(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, doctor):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialisation = doctor
        self.availability = []

    def view_schedule(self):
        pass

    def view_availability(self):
        pass


class Appointment:
    def __init__(self, appointment_id, date_time, patient, practitioner, reason_for_visit):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.patient = patient
        self.practitioner = practitioner
        self.reason_for_visit = reason_for_visit
        self.status = "Booked"

    def book(self):
        pass

    def cancel(self):
        pass

    def update_status(self):
        pass

    def release_booking_slot(self):
        pass
