from datetime import date
import face_recognition
import os
import cv2


#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

train_dir = "imagens/"

known_face_encodings = []
# Loop through images in folder
for filename in os.listdir (train_dir):
    #take the image inside the filename in train_dir
    rosto = face_recognition.load_image_file(train_dir + filename)
    #encode that face
    rostoTreinado = face_recognition.face_encodings(rosto)[0]
    #push it in the list
    known_face_encodings.insert(len(known_face_encodings),rostoTreinado)

known_face_names = []
with open('alunos.txt', 'r') as my_file:
    filerows =my_file.read().split("\n")
    for line in filerows:
        known_face_names.append(line)
        #print(line)


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

data =date.today()
datastr = data.strftime('%d|%m|%Y')
nomeLista= 'lista_chamada_'+ datastr + '.txt'

lista = open(nomeLista,'w') 
lista.close

end = False

#check if the name had alread been saved on the txt
def pesquisaChamada(name):
    arq = open(nomeLista, 'r')
    texto = arq.read().split("\n")
    for linha in texto:
        if (linha == name):
            result = True
            arq.close
            break    
        else:
            result= False
    arq.close
    return result

#write name on the txt
def assinaLista(name):
    #print("escrito")
    lista = open(nomeLista, 'a')
    lista.write(name + "\n")
    lista.close
                
while True:

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown [X]"
            fname = name
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                #print("mach")
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                fname = name
                # if name is new in the list save
                if (pesquisaChamada(name)!=True):
                    fname += "[X]"    
                    assinaLista(name)
                #else show the [V] after the name
                    fname += "[V]"    
            face_names.append(fname)    
                
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()