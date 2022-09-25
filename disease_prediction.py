from ast import Delete
from curses.panel import bottom_panel
from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
from turtle import pen
import numpy as np
import pandas as pd
root = Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
def signin():
    username=user.get()
    password=code.get()
    if username == 'admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("Disease Predictor")
        screen.config(bg="#fff")
        l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

        disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Corona',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo',]

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)
# TESTING DATA
        tr=pd.read_csv("Testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Corona':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40,}},inplace=True)
        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)
# TRAINING DATA
        df=pd.read_csv("Training.csv")
        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Corona':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)
        X= df[l1]
        y = df[["prognosis"]]
        np.ravel(y)
        def message():
            if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
                messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
            else :
                NaiveBayes()
        def NaiveBayes():
            from sklearn.naive_bayes import MultinomialNB
            gnb = MultinomialNB()
            gnb=gnb.fit(X,np.ravel(y))
            from sklearn.metrics import accuracy_score
            y_pred = gnb.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1
            inputtest = [l2]
            predict = gnb.predict(inputtest)
            predicted=predict[0]
            h='no'
            for a in range(0,len(disease)):
                if(disease[predicted] == disease[a]):
                    h='yes'
                    break
            if (h=='yes'):
                t3.delete("1.0", END)
                t3.insert(END, disease[a])
            else:
                t3.delete("1.0", END)
                t3.insert(END, "No Disease")
        Symptom1 = StringVar()
        Symptom1.set(None)
        Symptom2 = StringVar()
        Symptom2.set(None)
        Symptom3 = StringVar()
        Symptom3.set(None)
        Symptom4 = StringVar()
        Symptom4.set(None)
        Symptom5 = StringVar()
        Symptom5.set(None)
        w2 = Label(screen, justify=LEFT, text=" Disease Prediction From Symptoms",borderwidth=1, relief="solid")
        w2.config(font=("Microsoft Yahei UI Light", 30))
        w2.grid(row=1, column=0, columnspan=2, padx=100)
        NameLb1 = Label(screen, text="")
        NameLb1.config(font=("Microsoft Yahei UI Light", 20))
        NameLb1.grid(row=5, column=1, pady=10,  sticky=W)
        S1Lb = Label(screen,  text="Symptom 1",borderwidth=1, relief="solid")
        S1Lb.config(font=("Microsoft Yahei UI Light", 15))
        S1Lb.grid(row=7, column=1, pady=10 , sticky=W)
        S2Lb = Label(screen,  text="Symptom 2",borderwidth=1, relief="solid")
        S2Lb.config(font=("Microsoft Yahei UI Light", 15))
        S2Lb.grid(row=8, column=1, pady=10, sticky=W)
        S3Lb = Label(screen,  text="Symptom 3",borderwidth=1, relief="solid")
        S3Lb.config(font=("Microsoft Yahei UI Light", 15))
        S3Lb.grid(row=9, column=1, pady=10, sticky=W)
        S4Lb = Label(screen,  text="Symptom 4",borderwidth=1, relief="solid")
        S4Lb.config(font=("Microsoft Yahei UI Light", 15))
        S4Lb.grid(row=10, column=1, pady=10, sticky=W)
        S5Lb = Label(screen,  text="Symptom 5",borderwidth=1, relief="solid")
        S5Lb.config(font=("Microsoft Yahei UI Light", 15))
        S5Lb.grid(row=11, column=1, pady=10, sticky=W)
        lr = Button(screen, text="Predict",height=2, width=20, command=message,bg='#57a1f8',fg='white',relief="sunken")
        lr.config(font=("Microsoft Yahei UI Light", 15))
        lr.grid(row=15, column=1,pady=20)
        OPTIONS = sorted(l1)
        S1En = OptionMenu(screen, Symptom1,*OPTIONS)
        S1En.grid(row=7, column=2)
        S2En = OptionMenu(screen, Symptom2,*OPTIONS)
        S2En.grid(row=8, column=2)
        S3En = OptionMenu(screen, Symptom3,*OPTIONS)
        S3En.grid(row=9, column=2)
        S4En = OptionMenu(screen, Symptom4,*OPTIONS)
        S4En.grid(row=10, column=2)
        S5En = OptionMenu(screen, Symptom5,*OPTIONS)
        S5En.grid(row=11, column=2)
        NameLb = Label(screen, text="")
        NameLb.config(font=("Microsoft Yahei UI Light", 20))
        NameLb.grid(row=13, column=1, pady=10,  sticky=W)
        NameLb = Label(screen, text="")
        NameLb.config(font=("Microsoft Yahei UI Light", 15))
        NameLb.grid(row=18, column=1, pady=10,  sticky=W)
        t3 = Text(screen, height=2, width=30)
        t3.config(font=("Microsoft Yahei UI Light", 20))
        t3.grid(row=20, column=1 , padx=10)
    elif username!='admin' and password!='1234':
        messagebox.showerror('Invalid','Invalid Username and Password')
img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50, y=50)
frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font =('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=100,y=5)
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width = 25, fg ='black',border=0,bg="white",font =('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295, height= 2,bg='black').place(x=25,y=107)
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width = 25, fg ='black',border=0,bg="white",font =('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295, height= 2,bg='black').place(x=25,y=177)
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame, text="Don't have an account?",fg ='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
sign_up  =Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
sign_up.place(x=215,y=270)
root.mainloop()
