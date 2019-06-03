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
    (0, _("General Practitioner")),
    (1, _("Dentist")),
    (2, _("Cardiologist")),
    (3, _("Dermatologist")),
    (4, _("Ear-Nose-Throat")),
    (5, _("Endocrinologist")),
    (6, _("General Surgeon")),
    (7, _("Gynaecologist")),
    (8, _("Nephrologist")),
    (9, _("Oncologist")),
    (10, _("Ophthalmologist")),
    (11, _("Paediatrist")),
    (12, _("Physiotherapist")),
    (13, _("Podiatrist")),
    (14, _("Psychologist")),
    (15, _("Radiologist"))
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