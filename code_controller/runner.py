import os
import csv


MAX_ITR=10
MIN_ACC=85

def get_last_accuracy():
    input_file = open("code/Data/accuracy.csv","r+")
    reader_file = csv.reader(input_file)
    row = list(reader_file)[-1]
    print(row)
    return float(row[1])*100
def tweak():
    import re
    with open("code/app.py", "r") as in_file:
        buf = in_file.readlines()

    with open("code/app.py", "w") as out_file:
        for line in buf:
            if line == "model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))\n":
                line = line + "model.add(layers.Conv2D(64, (3, 3), activation='relu'))\nmodel.add(layers.MaxPooling2D((2, 2)))\n"
            if "model.fit" in line:
                prev=re.findall(r'epochs=(.+?),', line)[0]
                num=str(int(prev)+5)
                line=line.replace(prev, num)
                
            out_file.write(line)


with open("code/Data/accuracy.csv", "w") as fp:
    wr = csv.writer(fp)
    wr.writerow(['No Of Iterations',"Test Accuracy","Model Path"])

for i in range(MAX_ITR):
    print(i)
    os.system("cd code && python3 app.py")
    if (get_last_accuracy() > MIN_ACC):
        break
    tweak()
    
#Emailer
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("server@gmail.com", "password")

#Send the mail
msg = "Model Trained with Final Accuracy : " + str(get_last_accuracy())

server.sendmail("server@gmail.com", "user@gmail.com", msg)