from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    (0, _("Male")),
    (1, _("Female")),
    (2, _("Other"))
)

ROLE_TYPE_CHOICES = (
    (0, _("Patient")),
    (1, _("Practice")),
    (2, _("Institution")),
    (3, _("Emergency Services")),
    (4, _("Health Insurance Providers"))
)

SPECIALISATION_TYPE_CHOICES = (
    (0, _("Ayurvedic Medicine")),
    (1, _("Anaesthesiologist")),
    (2, _("Cardiologist")),
    (3, _("Chiropractor")),
    (4, _("Cosmetic Surgeon")),
    (5, _("Dentist")),
    (6, _("Dermatologist")),
    (7, _("Ear-Nose-Throat(otolaryngologists)")),
    (8, _("Endocrinologist")),
    (9, _("Gastroenterologist")),
    (10, _("Gynaecologist Obstetrician")),
    (11, _("General Practitioner")),
    (12, _("General Surgeon")),
    (13, _("Nephrologist")),
    (14, _("Neurologist & Neuro Surgeon")),
    (15, _("Oncologist")),
    (16, _("Ophthalmologist")),
    (17, _("Optometrics")),
    (18, _("Orthopaedist")),
    (19, _("Paediatrist")),
    (20, _("Pathologist")),
    (21, _("Pulmonologist")),
    (22, _("Physiotherapist")),
    (23, _("Podiatrist")),
    (24, _("Psychologist & Psychiatrist")),
    (25, _("Radiologist")),
    (26, _("Rheumatologists")),
    (27, _("Sports Medicine Specialist")),
    (28, _("Urologist")),
)

INSTITUTION_TYPE_CHOICES = (
    (0, _("Private Hospital")),
    (1, _("Public Hospital")),
    (2, _("Clinic")),
    (3, _("Area Health Center")),
    (4, _("Pharmacy")),
    (5, _("Medical Laboratories")),
)

SERVICES_TYPE_CHOICES = (
    (0, _("Private Ambulance Independent")),
    (1, _("Private Ambulance")),
    (2, _("Public Ambulance "))
)

Day_CHOICES = (
    (0, _("Mon")),
    (1, _("Tue")),
    (2, _("Wed")),
    (3, _("Thu")),
    (5, _("Fir")),
    (6, _("Sat")),
    (7, _("Sun"))
)

STATUS_CHOICES=(
    (0, _("Open")),
    (1, _("Close")),
)

PROFILE_STATUS_CHOICES=(
    (0, _("Pending")),
    (1, _("Active")),
    (2, _("Deactive"))
)