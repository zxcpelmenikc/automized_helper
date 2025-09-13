class employees():
    def __init(self, id, last_name, first_name, middle_name, tab_number, inn, snils, gender, birth_date, birth_place, address, education, profession, marital_status, hire_date, dismissal_date, is_active):
        self.id=id
        self.last_name=last_name
        self.first_name=first_name
        self.middle_name=middle_name
        self.tab_number=tab_number
        self.inn=inn
        self.snils=snils
        self.gender=gender
        self.birth_date=birth_date
        self.birth_place=birth_place
        self.address=address
        self.education=education
        self.profession=profession
        self.marital_status=marital_status
        self.hire_date=hire_date
        self.dismissal_date=dismissal_date
        self.is_active=is_active


    def __repr__(self):
        return(employees({self.id}, {self.last_name}, {self.first_name},{self.middle_name},{self.tab_number},
                         {self.inn},{self.snils},{self.gender},{self.birth_date},{self.birth_place},{self.address},
                         {self.education},{self.profession},{self.marital_status},{self.hire_date},{self.dismissal_date},{self.is_active}))
