# Created by Mert Sevindik 08.08.2020

# A dict with key = question and value = vector

class DataModel:
    buildings = 1
    math = 1
    science = 1
    garedening = 1
    biology = 1
    nature = 1
    planning = 1
    culture = 1
    politics = 1
    social = 1
    people = 1
    speech = 1
    language = 1
    engineering = 1
    computer = 1
    graphics = 1
    programming = 1
    Systems = 1
    development = 1
    animation = 1
    communication = 1
    media  = 1
    design = 1
    aesthetics = 1
    art = 1
    chemistry = 1
    physics = 1
    anamoty = 1
    photography = 1
    history = 1
    painting = 1
    drawing = 1
    psychology = 1

    questions = {
        "Analysing and interpreting worksof art/literature": [photography, history, painting, drawing, psychology,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        "Intensive infested with speech": [], "Creatively prepare films and pho-tos on the computer": [],
        "Managing the budget of a depart-ment": [],
        "Install hardware (such as a harddisk or a processor) in a computer": [],
        "Get to know strategies for en-trepreneurial success": [],
        "formulate contracts and legal docu-ments precisely and without errors": [],
        "Use of technical equipment andmachinery": [], "Advising and supporting peoplewith personal problems": [],
        "Mediate conflicts between persons": [], "Setting up computer networks andbetween": [],
        "direct a play or film": [],
        "lead and drive a large project": [], "Create statistics and diagrams fordifferent business areas": [],
        "Develop vehicles and aircraft": [], "Formulate text attractively": [],
        "Creatively design buildings, interi-ors and landscapes": [],
        "Exploring the functionality of tech-nical devices": [], "Create computer simulations": [],
        "Develop guidelines for smooth or-ganizational processes": []
    }

    print(len(questions["Analysing and interpreting worksof art/literature"]))

    query = [4,5,2,3,4,0,3,3,3,5,2,3,4,4,3,4,2,5,2,4,2,1,5,3,1,0,5,2,5,1,0,2,3]

    studiengänge = {"Landscape Architecture": [], "Political and Social Studies": [], "Mediainformatics": [], "Communication design": [],
                    "Media and Communincations for Digital Businesses": [], "Medicine":[], "Marine Biology":[], "Philosophy": [],
                    "Industrial Engineering and Management":[], "Business Administration":[]
    }


class KNN(DataModel):
    data = DataModel()

    fif = 13

    def manhatten(self,a, b):

        return abs(a - b)

    def total_distance(self, q, d):
        dist_temp = 0
        for i in range(5):
            dist_temp = self.manhatten(q[i], d[i])
            return dist_temp



